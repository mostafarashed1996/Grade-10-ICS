#Lottery Numbers
#Program generates seven different lottery numbers and adds them to a list

#Algorithm
#Import modules
#Generate random single digit numbers
#Prints if number has not been printed before
#Exit program

import random
filename=[]
count=0
for num in range(7):
    randomNum=random.randint(0,9)
    count+=1
    print "Lottery number",count,":",randomNum
    filename.append(randomNum)
print "\nHere are your lottery numbers:\n",filename
print "Have a nice day"
raw_input()
