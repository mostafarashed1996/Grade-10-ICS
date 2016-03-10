# pay program
#Marko Alhamadani
#14/05/2012
# this program will ask the user how much they worked and how much they get paid hourly, it will then show them the amount of tax union fee will cost, as well as how much money they have left over

#import modules 
import time
import os
#ask to enter the program
ask=raw_input("DO you want to enter [Y/N]?")
time.sleep(2)
os.system("CLS")
#set up a loops
while ask[0].lower()=="y":
    # ask them for the amount of hours the worked
    hours = input("how many hours did you work this week? ")
    # ask the user their hourly pay rate
    payRate = input("what is your hourly pay rate? ")
    # make net pay function 
    def netPay(payRate,hours):
    # make a total 
        total = payRate*hours
    # subtract the tax and union fee to get left over 
    # multiply the total by 0.02 ot get union fee
        union_fee = total*0.02
        print "your union fee is", union_fee
    # multiply the total by 0.20 to get tax
        tax = total*0.20
        print "your tax fee is", tax
        # subtract the tax and union fee to get left over
        left_over = total - union_fee - tax
        print "your net pay is equal to ",left_over
        return " "
    #print the total pay
    print "Your total pay in",hours,"hours is equal to",hours*payRate,"$"
    print netPay(payRate,hours)
    #ask if user wants to go again to restart the loop
    ask=raw_input("\nWould you like to go again [Y/N]? ")
    time.sleep(1)
    os.system("CLS")

if ask[0].lower()!="y":
    raw_input("Press enter to leave")
else:
    raw_input("This is not an option, please try again.")
    ask="y"
raw_input()
