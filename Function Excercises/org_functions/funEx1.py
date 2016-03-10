#Hypotenuse calculator
#Marko Alhamadani
#14/04/2012
# this program will ask the user for the 2 side lengths of a right angled triangle and find the hypotenuse
print"""
    **************
    * Welcome to *
    *     My     *
    *  Program   *
    **************
this program measures the hypotenuse of a triangle
"""
# make hypotenuse function using pythagorean theorem
def hypotenuse(side1, side2):
    side3=(side1**2+side2**2)**0.5
    return side3
# ask them for the side lengths
side1 = input("what is your 1st side's length? ")
side2 = input("what is your seccond side's length? ")
# output answers with placeholders 
print "Your hypotenuse is equal to %.2f" %hypotenuse(side1, side2)
raw_input("Press enter to leave ") 
