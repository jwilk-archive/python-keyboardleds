import os

source_suffix = '.txt'
master_doc = 'index'

project = u'python-keyboardleds'
copyright = u'2012, Jakub Wilk'

extensions = ['sphinx.ext.autodoc']

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        os.pardir,
        os.pardir,
        'doc', 'changelog',
    )
    with open(path) as changelog:
        return changelog.readline().split()[1].strip('()')

release = version = get_version()

html_theme = 'haiku'
pygments_style = 'sphinx'

# vim:ts=4 sw=4 et
