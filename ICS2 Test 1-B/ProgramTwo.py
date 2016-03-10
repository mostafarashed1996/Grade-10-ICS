#ICS2 Test 1-B - Program Two -
#Mostafa Rashed
#Last Rev. March 9, 2012
#Gives the user's income after income tax is detucted

#"Import OS" to clear the screen
import os
#Asks the user for his name
name = raw_input("Please enter your name. ")
#Asks the user for his income
income = input("Please enter your income in numbers. ")
#Clears the screen
os.system("clear")
#Uses "if" to find out how much tax he has, starting with less than or equal to $10,000 income
if income <= 10000
    print name + ", here is your tax bill: \n \t Tax income \t %.2f \n \t Income tax \t 0 \n \t \t \t \t \t ----------- \n Income after tax \t %.2f" %income
#Uses "elif" to find out how much tax he has, if he has more than $10,000 but less than or equal too $40,000 income which he would get 10% tax
elif income >10000 and <= 40000:
    income2=(income-10000) - ((income-10000)*.10)
    tax = (income-10000)*.10 
    print name + ", here is your tax bill: \n \t Tax income \t %.2f \n \t Income tax \t %2.f \n \t \t \t \t \t ----------- \n Income after tax \t %.2f" %income, tax, income2
#Uses "elif" to find out how much tax he has, if he has more than $40,000 but less than or equal too $70,000 income which he would get 25% tax
elif income >40000 and <=70000:
    income2=(income-10000) - ((income-10000)*.25) + (income-40000) - ((income-40000)*.25)
    tax = ((income-10000)*.10 + ((income - 40000)*.25)
    print name + ", here is your tax bill: \n \t Tax income \t %.2f \n \t Income tax \t %2.f \n \t \t \t \t \t ----------- \n Income after tax \t %.2f" %income, tax, income2
