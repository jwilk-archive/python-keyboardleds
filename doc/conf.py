import os

source_suffix = '.txt'
master_doc = 'index'

project = 'python-keyboardleds'

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        'changelog',
    )
    with open(path) as changelog:
        return changelog.readline().split()[1].strip('()')

release = version = get_version()

html_theme = 'haiku'
html_show_copyright = False
pygments_style = 'sphinx'

# vim:ts=4 sw=4 et
