'''
With *python-keyboardleds* you can interact with your keyboard's LEDs
(scroll lock, caps lock, num lock).
'''

classifiers = '''\
Development Status :: 4 - Beta
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Operating System :: POSIX :: Linux
Programming Language :: Python
Programming Language :: Python :: 2
Topic :: System :: Hardware\
'''.split('\n')

from distutils.core import setup

setup(
	name = 'python-keyboardleds',
	version = '0.1',
	license = 'MIT',
	description = 'keyboard leds manipulation',
	long_description = __doc__.strip(),
	classifiers = classifiers,
	url = 'http://jwilk.net/software/python-keyboardleds.html',
	author = 'Jakub Wilk',
	author_email = 'ubanus@users.sf.net',
	py_modules = ['keyboardleds']
)

# vim:ts=4 sw=4 et
