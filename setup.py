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
'''.strip().split('\n')

import os
import distutils.core

os.putenv('TAR_OPTIONS', '--owner root --group root --mode a+rX')

distutils.core.setup(
	name = 'python-keyboardleds',
	version = '0.1',
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
