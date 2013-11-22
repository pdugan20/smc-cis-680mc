#!/usr/local/bin/python3
# Name: Patrick Dugan
# File name: lab3.2.py
# Date: July 05, 2011

import sys
import fileinput
import re

print('Content-type:text/html\n')

# Function used to split larger body of text into sentences
def splitSpeech(fullSpeech):
  sentenceEnders = re.compile('[.!?]')
  sentenceList = sentenceEnders.split(fullSpeech)
  return sentenceList

# Function used to read in the text file
def readFile(speechName):
  fullSpeech = open(speechName, "r").read()
  return fullSpeech

# Define a main() function
def main():
  speechTitle = ['clinton1st', 'froosevelt2nd', 'gwbush2nd', 'kennedy', 'lincoln1', 'lincoln2', 'nixon', 'obama', 'reagan', 'troosevelt', 'washington1st', 'washington2nd']
  for title in speechTitle:
    speechName = title + '.txt'
    fullSpeech = readFile(speechName)
    sentences = splitSpeech(fullSpeech)

    print("******************************************************************<p>")
    print("<br>File: speeches/" + speechName)
    print("<br>Characters: " + str(len(fullSpeech)))

    lineCount = fullSpeech.split("\n")
    print("<br>Lines: " + str(len(lineCount)-1))

    speechLines = fullSpeech.lower()
    speechLines = re.sub('\W', ' ', speechLines)
    speechLines = speechLines.split()
    print("<br>Words: " + str(len(speechLines)+1))
    print("<br>Sentences: " + str(len(sentences)))

# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
  main()
