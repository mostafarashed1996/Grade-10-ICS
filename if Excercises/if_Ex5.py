#BMI Calculator
#Mostafa Rashed
#Last Rev. 21 March 2012
#Calculate's a person's BMI and tells them if they ar within the normal range. This program can take both in imperial and metric.

#Import os to clear the screen later
import os
#Asks the user to enter use either metric or imperial
scale = input("What mesurement would you like to use? \n 1)Imperial (pounds and inches) \n \t OR \n 2)Metric (kilograms and meters) ")
#Clears the screen
os.system("clear")
#Makes an if statement to see what scale of mesurment he would use
if scale == 1:
    lbs = input("What is your weight in pounds? ")
    inch = input("What is your height in inches? ")
    bmi = lbs * (703/inch**2)
#Makes an if statment to figure out if the BMI is in range, or out of range
    if bmi >= 18.5 and bmi <= 25:
        print "Your BMI %.2f is within normal range " %bmi
    elif bmi < 18:
        print "Your BMI %.2f is lower than normal range " %bmi
    elif bmi >25:
        print "Your BMI %.2f is higher than normal range " %bmi
#Repeating the above steps but for metric
elif scale == 2:
    kg = input("What is your weight in kilograms? ")
    m = input ("What is your hight in meters? ")
    bmi = kg/m**2
    if bmi >= 18.5 and bmi <= 25:
        print "Your BMI %.2f is within normal range " %bmi
    elif bmi < 18:
        print "Your BMI %.2f is lower than normal range " %bmi
    elif bmi >25:
        print "Your BMI %.2f is higher than normal range " %bmi
raw_input()
