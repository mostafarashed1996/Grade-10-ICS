#Mark Average Calculator
#Mostafa Rashed
#Last Rev. 24 March 2012
#Takes the student's marks and divides them to find out his/her average

#Import OS for later use of clearing the screen
import os
#Asks the user how many marks he/she will be entering
marks = input("Specify how many marks you would like to enter. ")
#Sets up count variable
count = 0
total = 0
#Starts the loop
while True:
    count += 1
    indi = input("Please enter mark #%2d " %count) 
    total = total + indi
    if count == marks:
        break
avg = float(total/marks)
print "Your average mark for the %2d marks you presented is %.1f percent" %(marks, avg)
raw_input()
