#3 number calculator
#Mostafa Rashed
#16 May 2012
#This program will use functions to add up 3 numbers to find out its sum. If it  is in the teen range (13,14,17,18,19) the it will equal zero

#Set up the adding function
def threenum(a,b,c):
    #Adds them
    total = a+b+c
    #Returns the answer
    return total
#Set up the "teen" checking function
def teenchek(threenum):
    #Checks if the total is equal to 13, 14, 17, 18, or 19, and if so...
    if threenum==13 or threenum==14 or threenum==17 or threenum==18 or threenum==19:
        #... print 0
        return 0
    #If not...
    else:
        #Return the total
        return threenum
#Asks the user for the 1st, 2nd, and 3rd numbers
a = input("Please input the 1st number ")
b = input("Please input the 2nd number ")
c = input("Please input the 3rd number ")
#Prints it back to the user
print "The sum of the three numbers are: %d" %teenchek(threenum(a,b,c))
raw_input("Have a nice day!")
