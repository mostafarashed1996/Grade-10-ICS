#index calculator
#Marko Alhamadani
#14/05/2012
# this program converts list finding to string  finding

#import modules
import os
import time

print "REMEMBER: IF THE OUTPUT IS -1 THEN IT MEANS IT IS NOT IN THE LIST OF NUMBERS\n"
ask="y"
#set up loop
while ask[0].lower()=="y":
    # make a number list 
    num_list = range(1,20)
    # define the listFind function 
    def listFind(number, num_list):
    # make it a string
        num_list = str(num_list)
    # use the find function to get the index
        finding_number = num_list.find(number)
        print finding_number
    # ask them for the number they are looking for 
    number = str(int(raw_input("what number are you checking for? ")))
    # print the index 
    print "The index of that digit is: "
    listFind(number,num_list)
    print ""
    #ask to go again
    number=int(number)
    #ask to go again 
    ask=raw_input("Do you want to go again [Y/N]?\n")
    time.sleep(2)
    os.system("CLS")
if ask[0].lower()!="y":
    raw_input("Have a nice day")
else:
    print "this is not a valid option"
    ask="y"
raw_input()
