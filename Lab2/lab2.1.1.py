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
  oliverFull = oliverTemp[:]
  oliverFull.reverse()
  del oliverFull[100:]
  del oliverTemp[100:]

  globalCount = 0
  tempCount = 0
  print('<table>')
  while globalCount <=100:
    if globalCount % 6 == 0:
      print('<tr>')

    try:
      print('<td>' + "{0:>12}".format(str(oliverTemp[globalCount])) + '</td>')
    except IndexError:
      print("</tr>")

    tempCount = tempCount + 1

    if globalCount % 6 == 0:
      if tempCount == 6:
        print('</tr>')
        tempCount = 0
      
    globalCount = globalCount + 1
  print('</table>')

  uniqueWordsFirst = set(oliverTemp)
  uniqueWordsLast = set(oliverFull)
  print("<p>The first set of 100 words has " + repr(len(uniqueWordsFirst)) + " unique words.<br>")
  print("The second set of 100 words has " + repr(len(uniqueWordsLast)) + " unique words.<br>")

  oliverUnion = (repr(len(uniqueWordsFirst | uniqueWordsLast)))
  print("The two sets together (UNION) have " + oliverUnion + " unique words.<br>")

  oliverSharedSet = (uniqueWordsFirst ^ uniqueWordsLast)
  oliverShared = (repr(len(uniqueWordsFirst ^ uniqueWordsLast)))
  oliverSharedInt = int(oliverShared)
  oliverUnion = int(oliverUnion)
  uniqueCount = (oliverUnion - oliverSharedInt)
  print(str(uniqueCount) + " words occur in both sets. They are:<br>")

  splitDifference = (oliverUnion - uniqueCount)
  print("There are " + str(splitDifference)  + " words that are in one or the other but not both (Symmetric difference):<br>")

  firstUnique = (uniqueWordsFirst ^ oliverSharedSet)
  print(repr(len(firstUnique)))

# Define a main() function
def main():
  readFile()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
