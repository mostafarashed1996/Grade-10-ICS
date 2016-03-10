#File Extenstion
#Mostafa Rashed
#Last Rev. March 20 2012
#Tells you the type of file you have

#Import os for clearing the screen later
import os
#Sees the length of the file name so if it under 12 chars, then it can be accepted
filename = raw_input("Enter the file name: ")
length = len(filename)
#If statments for the extentions to identify the users file type.
if length <= 12:
    dot=filename.find(".")
    ext = filename[dot:]
    if ext==".doc":
            print "It is a Word Document."
    if ext==".txt":
            print "It is a Text Document."
    if ext==".ppt":
            print "It is a Powerpoint Presentation."
    if ext==".xls":
            print "It is an Excel Document."
    if ext==".exe":
            print "It is a Windows Executable."
    else:
        print "You have entered an unacceptable file extention. Please try again"
else:
    print "You have entered a file name that is too long"
raw_input("Thank you for using the program! Have good day")
