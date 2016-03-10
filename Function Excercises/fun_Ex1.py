#Hypotenuse calculator
#Mostafa Rashed
#Last Rev. 14 May 2012
#This program will, with the help of functions, ask the user for the length of two sides to get the hpotenuse

#Creates a function for hypotenuse for sides 'a' and 'b'
def hyp(a,b):
    #Hypotenuse formula for variable 'c'
    c = (a**2+b**2)**0.5
    #Prints 'c' when the hypotenuse gets both a and b sides from the user
    return c
#Asks the user for the first side's length
a = input("What is the length of the first side? (In CM) ")
#Asks the user for the second side's length
b = input("What is the length of the second side? (In CM) ")
#Prints out back to the user the measurements and the hypotenuse
print "The hypotenuse with the sides %.2f and %.2f is %.2f cm" %(a, b, hyp(a,b))
raw_input("Have a nice day!")
