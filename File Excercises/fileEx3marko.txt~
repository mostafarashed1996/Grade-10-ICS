#Password Maker
#Marko Alhamadani
#last revised: April 10 2012 
#Makes a password with given requirements  

#import modules 
import os
import time
from os import system
from time import sleep
#setup necessary variables and strings 
up=""
down=""
digit=""
length=0
keepGoing="Y"
                                   
print". . .     |"                        
print"| | |,---.|    ,---.,---.,-.-.,---."
print"| | ||---'|    |    |   || | ||---'"
print"`-'-'`---'`---'`---'`---'` ' '`---'"

#set up the loop while telling the conditions that must be met in order for password granted.
#the keepgoing is used later on
while keepGoing[0].upper()=="Y":
    up=False
    down=False
    length=False
    digit=False    
    print"Your password must:\n\tContain at least 8 character's\n\tContain at least one number\n\tContain at least one uppercase\n\tContain at least one lowercase\n"
    password=raw_input("Please enter a password: ")

#for the individual characters in the password the user inputs
    for char in password:
        #if the character is uppercase then up=true
        if char.isupper():
            up=True
        #if a character is lowercase then down=true    
        if char.islower():
            down=True
        #if a character is a digit the digit=true
        if char.isdigit():
            digit=True
    # if the length of the password is greater than 8 then length=true      
    if len(password)>=8:
        length=True
    # the boolean logic has use here where if all of them are true it will give you access granted    
    if length==True and up==True and down==True and digit==True:
        system("CLS")
        print",---.                             ,---.               |             |" 
        print"|---|,---.,---.,---.,---.,---.    |  _.,---.,---.,---.|--- ,---.,---|"
        print"|   ||    |    |---'`---.`---.    |   ||    ,---||   ||    |---'|   |"
        print"`   '`---'`---'`---'`---'`---'    `---'`    `---^`   '`---'`---'`---'"
        raw_input()
        break    
    #if any of the above terms or conditions are not false then.....  
    else:
        #if the length is not greater than 8 notify the user 
        if length!=True:
            print "Error. Your password is too short"
        #if there is no capital in the password notify the user     
        if up!=True:
            print "Error. You need a capital"
        #if there is no lowercase in the password 
        if down!=True:
            print "Error. You need a lower case"
        #if there is'nt at least one digit notify the user
        if digit!=True:
            print "Error. You need a digit"
        #ask the user if he wants to try again
        #if he inputs yes then it takes him back through the whole loop again 
        keepGoing=raw_input("Do you want to try again(Y/N) ")
        #if the user inputs no then the user says bye and waits 2 seconds then clears system
        if keepGoing[0].lower()=="n":
            print "Bye Bye"
            sleep(1)
        system("CLS")
