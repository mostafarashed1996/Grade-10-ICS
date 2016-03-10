#Distance between two coordinants
#Mostafa Rashed
#Date of last rev. 15 Feb, 2012
#Program gets two coordinates, and calculates the distance between the two
x1 = input("Input the X value for the first coordinate ")
y1 = input("Input the Y value for the first coordinate ")
x2 = input("Input the X value for the second coordinate ")
y2 = input("Input the Y value for the second coordinate ")
length = ((x2-x1)**2 + (y2-y1)**2)**.5
print "The length between points " + "(" + str(x1) + ", " + str(y1) + ")" + " and " + "(" + str(x2) + ", " + str(y2) + ") is %.2f long" %length
raw_input()
