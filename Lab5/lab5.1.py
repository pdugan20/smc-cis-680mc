#!/usr/local/bin/python3
# Patrick DUgan
# lab5.1.py  Functions
# July 25, 2011

import os
import shutil

print('Content-type:text/html\n')
shutil.copy2('/home/students/patridugan/public_html/images/python-logo-master-v3-TM-flattened.png', '/home/students/patridugan/public_html/images/copy_python_logo.png')
print('<img src=”/~patridugan/images/copy_python_logo.png” alt=”Python logo”>')

