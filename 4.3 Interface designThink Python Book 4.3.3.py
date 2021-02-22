"""4.3.3 Make a copy of square and change the name to polygon. Add another parameter
named n and modify the body so it draws an n-sided regular polygon. Hint: The
exterior angles of an n-sided regular polygon are 360/n degrees."""

import turtle

bob = turtle.Turtle()

def polygon(t,length,n):
    for i in range(5):
        t.fd(length)
        t.lt(360/n)

turtle.mainloop()
