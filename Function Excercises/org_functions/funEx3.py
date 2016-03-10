# sum of 3 numbers
#Marko Alhamadani
#15/05/2012
# this program will ask the user to enter 3 numbers and if they are in the teens (except 16 & 16) they will count as 0, and it will output the sum of the 3 numbers

print "this program adds your numbers but make sure that they are not in the 'teens' \notherwise they will be considered as a value of zero\n"
#set up the functions
def sumOfThree(num1,num2,num3):
    total= num1+num2+num3
    return total
def Teenfix(num):
    #if the numbers are 13,14,17,18, or 19 then return zero
    if num==13 or num==14 or num==17 or num==18 or num==19:
        return 0
    #if else then it's just the regular pre assigned value
    else:
        return num
# ask them for the first number     
num1 = input("what is your first number?")
# ask them for the seccond number
num2 = input("what is your seccond number?")
# ask them for the third number
num3 = input("what is your third number?")
# output the results
print "the sum of the 3 numbers is"
print sumOfThree (Teenfix(num1),Teenfix(num2),Teenfix(num3))
    
