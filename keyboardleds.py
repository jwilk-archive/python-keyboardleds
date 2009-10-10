import sys

_p_linux = sys.platform == 'linux2'

if not _p_linux:
    raise NotImplementedError

if _p_linux:

    import fcntl
    import os
    import struct

    _KDGETLED = 0x4B31
    _KDSETLED = 0x4B32
    _LED_SCR = 1
    _LED_NUM = 2
    _LED_CAP = 4

class ControlPanel(object):

    if _p_linux:

        def __init__(self):
            self._fd = os.open('/dev/console', os.O_WRONLY)
            self._leds = {}

        def __del__(self):
            try:
                os.close(self._fd)
            except AttributeError:
                pass

        def _set(self, n):
            fcntl.ioctl(self._fd, _KDSETLED, n)

        def _get(self):
            bytes = struct.pack('I', 0)
            bytes = fcntl.ioctl(self._fd, _KDGETLED, bytes)
            [result] = struct.unpack('I', bytes)
            return result

    def set(self, lights):
        n = 0
        for light in lights:
            n |= light._n
        self._set(n)

    def get(self):
        n = self._get()
        result = []
        i = 1
        while i <= n:
            if n & i != 0:
                try:
                    result.append(self._leds[i])
                except KeyError:
                    pass
            i *= 2
        return result

    def __repr__(self):
        return '%s.%s' % (self.__class__.__module__, 'control_panel')

class Led(object):

    def __init__(self, control, name, n):
        self._control = control
        self._name = name
        self._n = n
        control._leds[n] = self

    def set(self):
        c = self._control
        c._set(c._get() | self._n)

    def toggle(self):
        c = self._control
        c._set(c._get() ^ self._n)

    def reset(self):
        c = self._control
        c._set(c._get() & ~self._n)

    def get(self):
        c = self._control
        return c._get() & ~self._n != 0

    def __repr__(self):
        return '%s.%s' % (self.__class__.__module__, self._name)

control_panel = ControlPanel()
caps_lock = Led(control_panel, 'caps_lock', _LED_CAP)
scroll_lock = Led(control_panel, 'scroll_lock', _LED_SCR)
num_lock = Led(control_panel, 'num_lock', _LED_NUM)

ControlPanel.__init__ = None
Led.__init__ = None

# vim:ts=4 sw=4 et
