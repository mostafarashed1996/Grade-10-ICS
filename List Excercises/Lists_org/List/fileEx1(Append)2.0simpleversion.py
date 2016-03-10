#List Names 
#Last Revised: Dec 10, 2011
#Alisikander Ahmed 
#User enters name until 'stop', and is able to add and remove names and sort names. The names are added to a list

#Import the operating system
#Create's an empty string and assign's it to a variable
#Create's an empty list and assign's it to a variable
#Assign a variable to the boolean variable true
#Ask the user to enter a name and to enter 'stop' if they wish to stop
#Create a while loop where as long as the name entered is not equal to stop
#Create an if statement that as long as the name inserted isnot stop, it will append to the empty list
#Ask the user again to enter a name
#Once outside the first loop create another loop where as long answer==True
#Clear the screen and print the names
#Give the menu and ask the user to enter the number they wish to use
#If the selection equals one ask the user what name they want to append, append it to the list and assign answer to True
#If the selection equals two, ask the user what name they want to remove, remove it from the list and assign the answer to True
#If the selection equals three, sort the list and assign the answer variable to true
#Else, close the program

import os
keepGoing="y"
namelist= []
name=""

names=raw_input("Please enter names until your done, <type stop to end>: ")
os.system("CLS")
while names!="stop":
    if names.upper()[0]!="stop":
        namelist.append(names)
        names=raw_input("Please enter a name, <type stop to end>: ")
        os.system("CLS")

while True:
    os.system("CLS")
    print "\nThese are your names below: "
    for names in namelist:
        print names 
    option=0
    print "\nDo you want to:\n    1)Add a name to the list\n    2)Or exit the program"
    option=raw_input()
    if option=="1":
        addName=raw_input("Please enter a name: ")
        namelist.append(addName)
    
    elif option=="2":
        os.system("CLS")
        print "Menu has been exited"
        break
        raw_input()
raw_input()
