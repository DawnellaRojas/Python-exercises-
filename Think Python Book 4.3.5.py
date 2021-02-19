"""4.3.5 Make a more general version of circle called arc that takes an additional parameter
angle, which determines what fraction of a circle to draw. angle is in units of degrees,
so when angle=360, arc should draw a complete circle."""

import turtle
import math

bob = turtle.Turtle()

def arc(t,radius,angle):
    circumference = 2.0*math.pi*radius
    frac = angle/360.0
    arclength = circumference*frac
    n = 30
    length = arclength/n
    turnAng = angle/n
    for i in range(n):
        t.fd(length)
        t.lt(turnAng)
arc(bob, 120,360)

turtle.mainloop()