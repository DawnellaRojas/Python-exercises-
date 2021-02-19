"""4. Write a function called circle that takes a turtle, t, and radius, r, as parameters and
that draws an approximate circle by calling polygon with an appropriate length and
number of sides. Test your function with a range of values of r.
Hint: figure out the circumference of the circle and make sure that length * n =
circumference."""

import math
import turtle

bob = turtle.Turtle()

# Polygon fun

def polygon(t,length,n):
    for i in range(30):
        t.fd(length)
        t.lt(360/n)

def circle(t,r):
    circunference = 2.0*math.pi*r
    n = 30
    length = circunference/n
    polygon(t,length,n)


circle(bob,80)

turtle.mainloop()



