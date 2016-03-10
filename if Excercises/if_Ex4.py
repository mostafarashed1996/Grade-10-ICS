#Second converting
#Mostafa Rashed
#Last Rev. 21 March 2012
#Converts seconds to the nearest mesurments of time

#Imports os to clear the screen
import os
#The number of seconds are going to be inputed by the user
time = input("What is the length in seconds you want to use ")
#Clears the screen
os.system("clear")
#Makes if functions to convert the seconds
if time < 60:
    print "Your time is %2d second(s)" %time
elif time >= 60 and time < 3600:
    mins = time/60
    secs = time%60
    print "Your time is %2d minute(s) and %2d second(s)" %(mins, secs)
elif time >=3600 and time < 86400:
    hrs = time/3600
    mins = (time%3600)/60
    secs = mins%60
    print "Your time is %3d hour(s), %2d minute(s), and %2d second(s)" %(hrs, mins, secs)
elif time >=86400:
    days = time/86400
    hrs = (time%86400)/3600
    mins = (time%3600)/60
    secs = mins%60
    print "Yout time is %2d day(s), %2d hour(s), %2d minute(s), and %2d second(s)" %(days, hrs, mins, secs)
raw_input("Thanks for using this program! ")
