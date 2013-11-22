#!/usr/local/bin/python3
# patdugan
# lab5.1.py # Copys and prints the HTML for a python image
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

#----------------------------visible-divider----------------------------#

#!/usr/local/bin/python3 -u  
# -u turns off output buffering
# Creator: the_professor
# File: python_logo.py
# Description: return a binary file to stdout (the web server)

# We need the sys module for this job
import sys

# Read binary data with ’rb’
data = open('/home/students/patridugan/public_html/images/python-logo-master-v3-TM-flattened.png','rb').read()

# Print image/png media type, and number of characters sent
print("Content-Type: image/png\nContent-Length: %d\n" % len(data))

# Print binary data to stdout
sys.stdout.buffer.write(data)

#----------------------------visible-divider----------------------------#

#!/usr/local/bin/python3
# Patrick Dugan
# lab5.2.py
# July 25, 2011

import os
import cgi
import base64

print('Content-type:text/html\n')

def back_img():
  backImg = base64.b64encode(open('./images/lego.png','rb').read())
  print('<body background="data:image/gif;base64,' + str(backImg) + '">')

def print_char():
  for i in range(33,128):
    char = cgi.escape(chr(i)).encode("ascii", "xmlcharrefreplace")
    print(char.decode(),end=' ')

def main():
  back_img()
  print_char()
  
# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
