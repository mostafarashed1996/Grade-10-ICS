#Pay Calculator
#Mostafa Rashed
#Last Rev 16 May 2012
#Takes the user's hourly rate, amount of hours, and subtracts the union fee and tax from it to get the net income

#Import os to clear screen later
import os
#Sets up a redo variable for the loop later on
redo = "Y"
#While loop for asking the user for their pay and hours worked
while redo.upper()=="Y":
    #Defines income
    def income(salary, hours):
        #Total amount earned
        cash = salary * hours
        #Calculates the union fee
        unionfee = cash * 0.02
        #Calculates the tax
        tax = cash * 0.20
        #Substracts the union fee and the tax from the total to find the total earnings
        netincome = cash - unionfee - tax
        #Returns all info including your earnings before fees, the amount of tax and union fee to pay up, and the net income
        return "The amount you earned is: $%.2f/nThe fee that you owe to the union is: $%.2f/nThe tax you owe is: $%.2f/nYour total earnings are: $%.2f " %(unionfee, tax, netincome)
    #Prints the definition
    print income(salary, hours)
    #Sets a redo variable
    redo = raw_input("Do you want to try again? Y/N ")
    #Clears the screen
    os.system("CLS")
raw_input("Have a good day!")
