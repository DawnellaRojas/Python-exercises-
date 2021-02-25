'''As an exercise, use incremental development to write a function calledhypotenusethatreturns the
length of the hypotenuse of a right triangle given the lengths of the other two legs as arguments.
Record each stage of the development process as you go.'''

import math
# Function definition hypotenuse with 2 argument as legs of a triangle
def hypotenuse(leg1, leg2):
    '''Both arguments being in the second power in separated variables'''
    leg1_powered = leg1**2
    leg2_powered = leg2**2
    '''Adding both varialbles with a addition operator in a single variable'''
    sum_powered_leg1_leg2 = leg1_powered + leg2_powered
    '''Using a math.sqrt with the last result'''
    hypotenuse_result = math.sqrt(sum_powered_leg1_leg2)
    print("The result of the hypotenuse is", hypotenuse_result)
    return hypotenuse_result

#first function call with 3 and 4 parameters.
hypotenuse(3,4)
#Second function call with 5 and 6 parameters.
hypotenuse(5,6)
#Third function call with 10 and 9 parameters.
hypotenuse(10,9)
