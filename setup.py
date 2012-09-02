'''
With *python-keyboardleds* you can interact with your keyboard's LEDs
(scroll lock, caps lock, num lock).
'''

classifiers = '''
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: POSIX :: Linux
Programming Language :: Python
Programming Language :: Python :: 2
Programming Language :: Python :: 3
Topic :: System :: Hardware
'''.strip().splitlines()

import distutils.core
import os

def get_version():
    with open(os.path.join('doc', 'changelog')) as changelog:
        return changelog.readline().split()[1].strip('()')

__version__ = get_version()

distutils.core.setup(
	name = 'python-keyboardleds',
	version = __version__,
	license = 'MIT',
	description = 'keyboard leds manipulation',
	long_description = __doc__.strip(),
	classifiers = classifiers,
	url = 'http://jwilk.net/software/python-keyboardleds',
	author = 'Jakub Wilk',
	author_email = 'jwilk@jwilk.net',
	py_modules = ['keyboardleds']
)

# vim:ts=4 sw=4 et
