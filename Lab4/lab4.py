#lab4.1.py implemented all required features except for the distance calculator function

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

#----------------------------visible-divider----------------------------#

#circle.py these classes work correctly and can be called from lab4.1.py correctly

#!/usr/local/bin/python3
# Patrick Dugan
# circle.py  Circle
# July 16, 2011

class Shape:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def move(self, deltaX, deltaY):
    self.x = self.x + deltaX
    self.y = self.y + deltaY

class Circle(Shape):
  pi = 3.14159
  def __init__(self, r=1, x=0, y=0):
    Shape.__init__(self, x, y)
    self.radius = r
  def area(self):
    self.a = self.radius * self.radius * self.pi
    # if you just return 'a', and not 'a.self' you are returning the default parameter where a=1
    return self.a
  def location(self):
    self.circLoc = (self.x, self.y)
    return self.circLoc
  def __str__(self):
    # %s refers to string, %d refers to the 2 digits of the x and y coordinates for said circle
    printStr = "A Circle of raidus %s at coordinates (%d, %d), with an area of %s" % (self.radius, self.x, self.y, self.a)
    return printStr

class is_collision:
  noTouch = 0
  
  def __init__(self, c1='circle 1', c2='circle 2', tryCount='1'):
    # determines the sum of the radius of both circles
    touchMsg = "None"
    colCount = 1

    print("<p><b>Collision Try: " + str(tryCount) + "</b>")
    print("<br>----------------------------------------------------------------")
  
    sumRad = c1.radius + c2.radius
    print("<br>Sum of the two radii: " + str(sumRad))

    # imports the location of both the circles
    circ1Loc = c1.location()
    circ2Loc = c2.location()
    print("<br>Circle a coordinates: " + str(circ1Loc))
    print("<br>Circle b coordinates: " + str(circ2Loc))

    if self.noTouch == 0:
      print("Try " + str(tryCount) + ": Collision? " + "<b>" + touchMsg + "</b>" + "\n<p>")
    

