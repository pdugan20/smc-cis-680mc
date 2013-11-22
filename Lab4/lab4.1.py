#!/usr/local/bin/python3
# Patrick DUgan
# lab4.1.py  Functions
# July 16, 2011

import circle
print('Content-type:text/html\n')

# Use code like this to pull out a variable from the module you are importing
# print(circle.Circle.pi)

c1a = circle.Circle(5, 15, 10)
c1b = circle.Circle(5, 15, 20)

c2a = circle.Circle(5, 35, 10)
c2b = circle.Circle(5, 20, 10)

c3a = circle.Circle(5, 8, 13)
c3b = circle.Circle(5, 5, 22)

c4a = circle.Circle(5, 2, 55)
c4b = circle.Circle(5, 33, 44)

c5a = circle.Circle(5, 22, 32)
c5b = circle.Circle(5, 5, 10)

c6a = circle.Circle(5, 38, 45)
c6b = circle.Circle(5, 24, 54)

c7a = circle.Circle(5, 22, 55)
c7b = circle.Circle(5, 23, 67)

c8a = circle.Circle(5, 1, 10)
c8b = circle.Circle(5, 6, 15)

c9a = circle.Circle(5, 89, 93)
c9b = circle.Circle(5, 84, 75)

c10a = circle.Circle(5, 67, 78)
c10b = circle.Circle(5, 14, 20)

# Store all of the circles in a tuple
circTup=[c1a, c1b, c2a, c2b, c3a, c3b, c4a, c4b, c5a, c5b, c6a, c6b, c7a, c7b, c8a, c8b, c9a, c9b, c10a, c10b]

# This section of code finds the area for each of the 20 circles.
areaCount = 0
while areaCount <= 19:
  (circTup[areaCount]).area()
  areaCount = areaCount + 1

# This is random test code not useful to the final output of the circle collision code
# c2.move(5, 6)
# print(c2)
# print(c2.location())

# This finds out if the circles actually collide or not
#print(circTup[areaCount])
#print(circTup[areaCount + 1])

circCount = 0
tryCount = 1
while circCount <= 19:
  circlePrint = circle.is_collision(circTup[circCount], circTup[circCount + 1], tryCount)
  tryCount = tryCount + 1
  circCount = circCount + 2



