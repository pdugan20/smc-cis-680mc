#lab2.1.py mostly finished, not quite though. the table isn't aligned correclty, but the characters are all there.

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

# Define a main() function
def main():
  readFile()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()

#----------------------------visible-divider----------------------------#

#lab2.2.py I was able to complete this one correctly, displays first 50 numbers

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

  print("<p><b>lab2.2.py</b>")
  print("<br>The First 50 Numbers in the Fibonacci Sequence")

  print('<p><table>')
  while writeCount <=50:
    print('<tr>')
    print('<td>'+ str(writeCount) + '</td><td>' + str(fibList[writeCount]) + '</td>')
    print('</tr>')
    writeCount = writeCount + 1
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
