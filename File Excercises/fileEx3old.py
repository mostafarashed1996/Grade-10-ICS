import os
uppercase = ""
lowercase = ""
numbers = ""
length = 0
print "Welcome to the Toronto District School Board computer systems. If you want to access this computer, you must enter your username and password"
username = raw_input("Please input your username: ")
while True:
    intropassword = raw_input("Please enter your current password: ")
    if intropassword == "ICS2Carter":
        break
    else:
        print "That was the wrong password. Please try again"
print "Error! %s your password has expired, and you must make a new one. We have changed the security guidelines recently, and now to make the password it must:\n1: Must be at least 8 characters long\n2: Have at least one lower case letter\n3: Have at least one uppercase character\n4: Have at least one digit" %username
password = raw_input("Please enter your new password ")
for char in password:
    if len(password)>=8:
        length = True
    if char.islower():
        lowercase = True
    if char.isupper():
        uppercase = True
    if char.isdigit():
        numbers = True
    if length == True and lowercase == True and uppercase == True and numbers == True:
        print "You have changed your password! Thank you for following the guidelines, and have fun learning in TDSB!"
        break
    else:
        if length!=True:
            print "Your password is too short, please try again. Remember it has to be at least 8 characters"
        if lowercase!=True:
            print "Your password has no lowercase letters, please try again. Remember it has to have at least 1 lower case letter"
        if uppercase!=True:
            print "Your password has no uppercase letters, please try again. Remember it has to have at least 1 digit"
        if numbers!=True:
            print "Your password has no digits, please try again. Remember it needs to have at least one digit "
        break
