import os

source_suffix = '.txt'
master_doc = 'index'

project = 'python-keyboardleds'
copyright = '2012, 2013, Jakub Wilk'

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        'changelog',
    )
    with open(path) as changelog:
        return changelog.readline().split()[1].strip('()')

release = version = get_version()

html_theme = 'haiku'
pygments_style = 'sphinx'

# vim:ts=4 sw=4 et
