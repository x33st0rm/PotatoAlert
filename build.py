"""
Copyright (c) 2019 razaqq

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import sys
import subprocess

ADDITIONAL_LIB_PATHS = 'C:\\Program Files (x86)\\Windows Kits\\10\\Redist\\ucrt\\DLLs\\x64'
QT5_LIBS_PATH = 'C:\\Users\\User\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\site - packages\\PyQt5\\Qt\\bin'


if __name__ == '__main__':
    root = os.path.abspath(os.path.dirname(__file__))
    main = os.path.join(root, 'potatoalert.py')
    assets = os.path.join(root, 'assets')
    icon = os.path.join(assets, 'potato.ico')
    assets_sep = ':' if os.name == 'posix' else ';'

    debug_flags = '-F -y'
    build_flags = '-F -y -w'

    build = f'{sys.executable} -m PyInstaller {build_flags} -i "{icon}" --add-data "{assets}"{assets_sep}"assets/" ' \
            f'--paths "{ADDITIONAL_LIB_PATHS}" --paths "{QT5_LIBS_PATH}" "{main}"'

    subprocess.call(
        build
    )

    os.remove(os.path.join(root, 'potatoalert.spec'))