#!/usr/local/bin/python3
# Patrick DUgan
# lab5.1.py  Functions
# July 25, 2011

import os
import shutil
import python_logo
print('Content-type:text/html\n')

def copy_img():
  # pyImg = open(os.path.join(os.getcwd(),'images','python-logo-master-v3-TM-flattened.png'), 'r')
  shutil.copy2('/home/students/patridugan/public_html/images/python-logo-master-v3-TM-flattened.png', '/home/students/patridugan/public_html/images/copy_python_logo.png')

def print_img():
  print('<img src=”/~patridugan/images/copy_python_logo.png” alt=”Python logo”>')

copy_img()
print_img()

def main():
  copy_img()
  print_img()
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()



