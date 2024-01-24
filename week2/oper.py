# python program to calculate area and circumference of a circle with radius given in terminal

r = int(input("Enter the radius of the circle: \n"))

import math

area = math.pi*r*r
circ = 2*math.pi*r
print("The area is %s and the circumference is %s"%(area,circ))
