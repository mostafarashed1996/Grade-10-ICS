#TDSB Password Maker
#Mostafa Rashed
#Last Rev. 12 April 2012
#Makes the user have to make a password under certain guidelines

#Imports the os
import os
#Sets up variables needed to verify the password later on
uppercase = ""
lowercase = ""
numbers = ""
length = 0
#Sets up a redo variable so incase they get they make the password incorrectly, they can re-input the password and go through the loop again.
redo = "Y"
#A welcome message
print "Welcome to the Toronto District School Board computer systems. If you want to access this computer, you must enter your username and password"
#For the bonus - enter any username for TDSB
username = raw_input("Please input your username: ")
#Sets a while loop for the bonus
while True:
    #Sets to ask the 'default' password for the bonus which is "ICS2Carter"
    intropassword = raw_input("Please enter your current password: ")
    if intropassword == "ICS2Carter":
        break
    else:
        print "That was the wrong password. Please try again"
#Tells you your password has expired and tells you to make one with 4 rules they need to follow
print "Error! %s your password has expired, and you must make a new one. We have changed the security guidelines recently, and now to make the password it must:\n1: Must be at least 8 characters long\n2: Have at least one lower case letter\n3: Have at least one uppercase character\n4: Have at least one digit" %username
#Sets up a while loop for the password making process
while redo.upper()=="Y":
    #Sets up the 'boolean' control for the uppercase, lowercase, length, and numbers variables to verify the password
    uppercase=False
    lowercase=False
    length=False
    numbers=False
    #Asks for the password from the user
    password = raw_input("Please enter your new password ")
    #Sets a 'for' loop for the password
    for char in password:
        #Checks if there is a character that is lowercase or not, and if it is lower, then it would be set as 'True'
        if char.islower():
            lowercase = True
        #Checks if there is a character that is uppercase or not, and if it is upper, then it would be set as 'True'
        if char.isupper():
            uppercase = True
        #Checks if there is a character that is a digit or not, and if there is one, then it would be set as 'True'
        if char.isdigit():
            numbers = True
    #Checks the password's length, and if it is 8 characters or longer then it is set as 'True'
    if len(password)>=8:
        length = True
    #Checks if all the 'rules' are set for true, and if it is, then it will terminate the loop and exit
    if length==True and uppercase==True and lowercase==True and numbers==True:
        print "You have changed your password! Thank you for following the guidelines, and have fun learning in TDSB!"
        break
    #If there is still one thing that is 'False' and the password for some reason did not pass the 'rules' then it would notify you about what wemt wrong. Then it will automatically restart and ask for a password again, and it re enters the loop
    else:
        if length!=True:
            print "Your password is too short, please try again. Remember it has to be at least 8 characters"
        if lowercase!=True:
            print "Your password has no lowercase letters, please try again. Remember it has to have at least 1 lowercase letter"
        if uppercase!=True:
            print "Your password has no uppercase letters, please try again. Remember it has to have at least 1 uppercase letter"
        if numbers!=True:
            print "Your password has no digits, please try again. Remember it needs to have at least one digit "
        redo=="Y"
raw_input()
