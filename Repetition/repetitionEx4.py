#10 Second Countdown
#Mostafa Rashed
#Last Rev. 25 March 2012
#It counts down from 10 seconds before the blast off

#Imports time to delay execution of each number by a second, like a real countdown
import time
#Sets a count variable
count = 11
#Prints "This is a final countdown"
print "This is the final countdown"
#Sets up the loop
while True:
    #Subtracts 1 from count for every loop execution
    count -=1
    #Delays execution of the number by one second
    time.sleep(1)
    #Displays the numbers on the screen
    print count,
    #Breaks the loop after the number one
    if count == 1:
        break
#Delays the "Blastoff" printing
time.sleep(1)
#Prints "Blastoff!"
print "\nBlastoff!"
raw_input()
