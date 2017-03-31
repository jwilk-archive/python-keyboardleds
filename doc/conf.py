import io
import os

source_suffix = '.txt'
master_doc = 'index'

project = 'python-keyboardleds'

def get_version():
    path = os.path.join(
        os.path.dirname(__file__),
        'changelog',
    )
    with io.open(path, encoding='UTF-8') as file:
        line = file.readline()
    return line.split()[1].strip('()')

release = version = get_version()

html_theme = 'haiku'
html_show_copyright = False
html_show_sphinx = False
pygments_style = 'sphinx'

# vim:ts=4 sts=4 sw=4 et
