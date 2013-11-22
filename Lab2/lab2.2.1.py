#!/usr/local/bin/python3
# Name: Patrick Dugan
# File name: lab2.2.py
# Date: July 04, 2011

import sys
import fileinput
import re

print('Content-type:text/html\n')

listCount = 0

# Function used to read in the text file
def tableWrite(fibList):    
  writeCount = 0
  
  print('<table>')
  print('<tr>')
  while writeCount <=50:
    print('<td>'+ str(writeCount) + '</td><td>' + str(fibList[writeCount]) + '</td>')
    writeCount = writeCount + 1
  print('</tr>')
  print('</table>')
  #print(fibList)

def fib(n):
  global listCount
  fibList = []
  a, b = 0, 1
  while a < n:
    if listCount == 0:
      fibList.insert(listCount, a)
    listCount = listCount + 1
    fibList.insert(listCount, a)
    a, b = b, (a + b)
  return fibList

# Define a main() function
def main():
  fibList = fib(12586269026)
  tableWrite(fibList)

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
