#Pay Calculator 
#This program will allow the user to check the gross pay for each employee

#Create's empty list for hour's
#Ask's user the number of employees
#Ask's user for the hourly rate
#Float's hourly rate 
#Create's a for loop to ask the user the hours worked by each employee
#Append's hours to list
#Set's index to 0
#Create's for loop for calculating the pay

hourList=[]
num=0
from os import system
print "Hello!"
numEmploy = input("How many employees do you have? ")
system("CLS")
wage=float(raw_input("What is the hourly rate of pay? <No dollar sign> "))
for index in range(0,numEmploy):
    print "How many hours were worked by employee # " +str(index+1)
    hours = float(input())
    hourList.append(hours)
index=0
for num in range(0,numEmploy):
    pay=hourList[index]*wage
    print "Employee", num + 1, "makes $", pay
    index = index + 1
raw_input("Have a nice day")


