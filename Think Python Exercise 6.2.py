'''As an exercise, use incremental development to write a function called hypotenuse that
returns the length of the hypotenuse of a right triangle given the lengths of the other two
legs as arguments. Record each stage of the development process as you go.'''

import math
# Formula used to be coded c**2 = leg1**2 + leg2**2

def hypotenuse(leg1,leg2):

    sumOfSides = leg1**2 + leg2**2
    hypotenuse = math.sqrt(sumOfSides)
    return
    hypotenuse


hypotenuse(4,3)