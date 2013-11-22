#lab2.1.py Description goes here

#!/usr/local/bin/python3
# Name: Patrick Dugan
# File name: lab2.1.py
# Date: July 02, 2011
# print(’Content-type:text/html\n’)

import sys
import fileinput
import re

# Function used to read in the text file
def readFile():
# An array of things. Your array will be much larger, with
# multiple rows of 7 items. HINT: Use a counter variable
# and the remainder operator (%) to determine when 7
# cells have been printed and it’s time for a new row.
  things = ['thing one','thing two','thing 3','thing 4','thing 5','thing 6','thing 7']
  # Start the table
  print('<table>')
  
  # Start a row
  print('<tr>')

  # Create the TD cells
  for thing in things:
    print('<td>%s</td>' % thing)

  # Print the closing of row
  print('</tr>')

  # And close the TABLE
  print('</table>')
  
  # print(oliverTemp)
  # print(len(oliverTemp))

# Define a main() function
def main():
  readFile()

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
