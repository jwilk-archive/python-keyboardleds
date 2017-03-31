# encoding=UTF-8

# Copyright © 2009-2017 Jakub Wilk <jwilk@jwilk.net>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the “Software”), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

'''
With *python-keyboardleds* you can interact with your keyboard's LEDs
(scroll lock, caps lock, num lock).
'''

import distutils.core
import io
import os

try:
    import sphinx.setup_command as sphinx_setup_command
except ImportError:
    sphinx_setup_command = None

def get_version():
    with io.open(os.path.join('doc', 'changelog'), encoding='UTF-8') as changelog:
        return changelog.readline().split()[1].strip('()')

__version__ = get_version()

cmdclass = {}

if sphinx_setup_command is not None:
    cmdclass['build_doc'] = sphinx_setup_command.BuildDoc

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

distutils.core.setup(
    name='python-keyboardleds',
    version=__version__,
    license='MIT',
    description='keyboard LEDs manipulation',
    long_description=__doc__.strip(),
    classifiers=classifiers,
    url='http://jwilk.net/software/python-keyboardleds',
    author='Jakub Wilk',
    author_email='jwilk@jwilk.net',
    py_modules=['keyboardleds'],
    cmdclass=cmdclass,
)

# vim:ts=4 sts=4 sw=4 et
