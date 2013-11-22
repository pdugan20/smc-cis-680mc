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



