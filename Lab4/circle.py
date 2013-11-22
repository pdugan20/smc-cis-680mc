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
  def list(self):
    return False

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
    

