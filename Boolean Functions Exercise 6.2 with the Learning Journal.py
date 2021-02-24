'''As an exercise, use incremental development to write a function calledhypotenusethatreturns the
length of the hypotenuse of a right triangle given the lengths of the other twolegs as arguments.
Record each stage of the development process as you go.'''

import math
# Function definition hypotenuse with 2 argument as legs of a triangle
def hypotenuse(leg1, leg2):
    '''Both arguments being in hte second power in separated variables'''
    leg1_powered = leg1**2
    leg2_powered = leg2**2
    '''Adding both varialbles with a addition operator in a single variable'''
    sum_powered_leg1_leg2 = leg1_powered + leg2_powered
    '''Using a math.sqrt with the last result'''
    hypotenuse_result = math.sqrt(sum_powered_leg1_leg2)
    print("The result of the hypotenuse is", hypotenuse_result)
    return hypotenuse_result


hypotenuse(3,4)
hypotenuse(5,6)
hypotenuse(10,9)
