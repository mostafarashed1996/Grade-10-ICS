#Random class mark generator
#Mostafa Rashed
#Last Rev. 11 April 2012
#Takes the class list and makes initals which will generate marks for them from 50%-100% while outputting the average of the calls

#Imports randint module from random
from random import randint
#Opens the class list in read mode
classlist=open("ICS2_Class.txt", "r")
#Opens and creats a text file in write mode to put the marks in
marks=open("classmarks.txt", "w")
#Sets the variable for both number of marks and totak marks for finding the average later
numofmarks=0
totalmarks=0
#Creates the headers
print "         Initials                              Grade"
print "         --------                              -----"
#Makes a while loop to generate the marks
while True:
    #Creates the name variable and tells it to read each line from the class list
    names=classlist.readline()
    #Makes an if statment when it reaches the end to break
    if names == "":
        #Breaks the loop
        break
    #Makes the variable for initals taking the first part of the name
    init = names[0].upper()
    #While loop if there are spaces in the names
    while names.count(" ")>0:
        #Makes the initals of the people in the class
        init = init + names[names.find(" ")+1].upper()
        #Makes the rule incase there is an extra space in the name
        names = names [:names.find(" ")] + names[names.find(" ")+1:]
    #Random generation of marks between 50-100%
    randmark = randint (50, 100)
    #Prints the mark and initals line by line
    print "          " + init + "\t\t\t\t\t" + str(randmark)
    #Adds to the number of marks for the average later
    numofmarks += 1
    #Adds to the number of all the marks added together to get the average later
    totalmarks += randmark
#Makes the average veriable and in float format to make it decimal
avg = (totalmarks*1.0)/numofmarks
#Prints the header
print "                              Average"
print "                              -------"
#Prints the average with one decimal point
print "                               %2.1f" %avg
raw_input()
