#Lottery Number Generator
#Mostafa Rashed
#Generates lottery numbers for X amount of numbers

#Import 'os' to clear the screen later
import os
#Import 'random' to randomly generate a number later on
import random
#Sets up 'redo' variable for the lottery loop
redo = "Y"
#Sets up 'count' variable so we can count the numbers of the lottery number
count = 0
#Sets up a list 'lotterylist' to hold all the lottery numbers
lotterylist = []
#Welcoming statement
print "Welcome to Mostafa's amazing lottery number generator"
#Starts the loop
while redo.upper() == "Y":
    #Clears the screen everytime they specify lottery numbers
    os.system("CLS")
    #Asks how many #'s generated
    length = input("Please sepecify the length of the lottery number ")
    #For loop for generating #'s
    for num in range(length):
        #Makes a variable to generate a number from 0-9 for the number that was specified
        lotterynum = random.randint(0,9)
        #Counts how many numbers were added to display it to the user
        count += 1
        #Prints one of the numbers and the ',' is added to put them one behind another
        print lotterynum,
        #Appends numbers to the list
        lotterylist.append(lotterynum)
    #Asks the user if they want to go back through the loop
    redo = raw_input("Do you want to do it again? (Y/N) ")
#Prints out the # of numbers that were generated an the numbers themselves
print "Your %d lottery numbers are:\n%s" %(count,lotterylist)
raw_input()
