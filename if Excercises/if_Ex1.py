#HST and Fedral Tax on fast food
#Mostafa Rashed
#March 20, 2012
#Takes the purchase of fast food, and applies tax to it.

#Import OS to clear screen later
import os
#Asks the user to choose what meal he wants
choice = input("Welcome to the Camel's Hut! What would you like to order? \n 1) Shawerma Sandwich \t \t $3.50 \n 2) Shawerma Plate \t \t $9.00 \n 3) 5 peices of Falafel \t $4.25 \n 4) 10 peices of Falafel \t $7.95 \n ") 
#Clear the screen
os.system("clear")
#if function to find the total with tax
if choice == 1:
        cost = 3.50
        tax = (cost * 0.05)
        total = cost + tax
        print "\t The cost of your meal is %.2f \n \t Plus 5 percent GST \t %.2f \n \t \t \t \t -------- \n \t Total \t \t \t %.2f " %(cost, tax, total)
#elif functions to find the total for the other three options
elif choice == 2:
        cost = 9.00
        tax = (cost * 0.15)
        total = cost + tax
        print "\t The cost of your meal is %.2f \n \t Plus 15 percent HST \t %.2f \n \t \t \t \t -------- \n \t Total \t \t \t %.2f " %(cost, tax, total)
elif choice == 3:
        cost = 4.25
        tax = (cost * 0.15)
        total = cost + tax
        print "\t The cost of your meal is %.2f \n \t Plus 15 percent HST \t %.2f \n \t \t \t \t -------- \n \t Total \t \t \t %.2f " %(cost, tax, total)
elif choice == 4:
        cost = 9.00
        tax = (cost * 0.15)
        total = cost + tax
        print "\t The cost of your meal is %.2f \n \t Plus 15 percent HST \t %.2f \n \t \t \t \t -------- \n \t Total \t \t \t %.2f " %(cost, tax, total)
#An else function for options not avalible
else:
        print "Sorry but that was an invalid option, please try again. "
raw_input("Thank you for ordering from the Camel's Hut! Have a nice day! ")
