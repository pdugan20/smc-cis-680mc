#!/usr/local/bin/python3
# Name: Patrick Dugan
# File name: lab7.py
# Date: Aug 03, 2011

import sys
import fileinput
import re

print('Content-type:text/html\n')

# Function used to read in the text file
def tableWrite():    
  print("<p><b>lab7.py</b>")
  print("<br>Hello World & Guesbook AppEngine Apps")

  print('<p><a href="http://patduganhelloworld.appspot.com/">Hello World!</a>')
  print('<br><a href="http://patduganshout.appspot.com/">Guestbook</a>')

# Define a main() function
def main():
  tableWrite()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
