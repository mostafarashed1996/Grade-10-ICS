#Leap Year Calculator
#Mostafa Rashed
#Last Rev. 20 March 2012
#Calculates if a year is a leap year or not

#Import os for clearing the screen later
import os
#Asks the user for the year he wants to use
year=input("Please enter the year: ")
#Clears the screen
os.system("clear")
#Makes an if statment just incase someone uses the years 1700, 1800, and 1900
if year == 1700 or year == 1800 or year == 1900:
    print "Those years are acceptions to the rule; therefore, it is not a leap year "
#Makes an elif statment for the leap years other than the ones above
elif year%4==0:
    print "It is a leap year "
#Makes an else statment for the non-leap years
else: 
    print "It is not a leap year "
raw_input("Thank you for using this program! ")
