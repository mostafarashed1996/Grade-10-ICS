import os
import time
demhours=[]
count = 0
print "Always Fresh, Always Tim Hortons!"
print "Welcome to the Tim Hortons salary calculator John!\nPlease follow the next few steps!"
time.sleep(3)
os.system("CLS")
employeecount = input("How many employees do you have? ")
rate = input("What is the hourly rate of the employees ")
os.system("CLS")
for a in range (0,employeecount):
    a += 1
    hours = input("Please input employee %d's hours: " %a)
    demhours.append(hours)
    os.system("CLS")
a = 0
for count in range (0,employeecount):
    wages = demhours[a]*rate
    count += 1
    print "Employee %d makes $%d" %(count, wages)
    a = a + 1
raw_input("Have a nice day John!")
