#!/usr/local/bin/python3
# Name: Patrick Dugan
# File name: lab2.1.py
# Date: July 02, 2011

import sys
import fileinput
import re
count = 0

print('Content-type:text/html\n')

# Function used to read in the text file
def readFile():
  filename = 'oliver.txt'
  oliver = open(filename, "r").read()
  oliver = oliver.lower()
  oliver = re.sub('\W', ' ', oliver)
  oliverTemp = oliver.split()
  del oliverTemp[100:]

  globalCount = 0
  tempCount = 0
  print('<table>')
  while globalCount <=100:
    if globalCount % 6 == 0:
      print('<tr>')

    try:
      print('<td>' + str(oliverTemp[globalCount]) + '</td>')
    except IndexError:
      print("</tr>")

    tempCount = tempCount + 1

    if globalCount % 6 == 0:
      if tempCount == 6:
        print('</tr>')
        tempCount = 0
      
    globalCount = globalCount + 1
  print('</table>')

  oliverSevenRow = []
  print(oliverTemp)  

# Define a main() function
def main():
  readFile()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
