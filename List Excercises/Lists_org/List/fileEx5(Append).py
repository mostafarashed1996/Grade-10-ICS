#Rainfaller
#User enters rainfall for each month and the program outputs the average,total and the greatest rainfall month and value

#Create a variable for an empty list 
#Create another variable equal to zero to use to find the average
#Create a litst with all 12 months
#Create a for loop for each month 
#Within the loop ask for the amount of rain
#Append the amount of rain to the empty list 
#Adds the rainfall for each month to the total 
#Add the amount inserted to the variable used for the average
#Once outside the loop find the max amount of rain in the list of rain amounts
#Find the index position of the max rainfall in your list of rain amounts
#Using the index position found, find the month which matches the given index position
#Than find the average amount and round it to one decimal place
#Print the average, the total amount and the month with the highest amount and what that amount was

import os
total=0
rainList=[]
month=["January","February","March","April","May","June","July","August","September","October","November","December"]                                         
print "Please remember to: \n 1)Enter according to cm \n 2)Enter according to one decimal place "
for num in range(len(month)):
    rainfallAmount=raw_input("What is the rainfall in %s: " % month[num])
    if rainfallAmount!=str:
        rainfallAmount=float(rainfallAmount)
        rainList.append(rainfallAmount)
        total+=rainfallAmount
    else:
        print "Please enter a valid number"
average=total/12
os.system("CLS")
print"\n\t    INFO\n"
for num in range(len(month)):
    print "%12s" % month[num] , "\t" , "%8s" % str(round(rainList[num],1)),"(cm)"
    
print "The total amount of rainfall in the year was:",round(total,1),"(cm)"
print "The average amount of rainfall a month was: ",round(average,1),"(cm)"
print "The greatest total rainfall was: ", round(max(rainList),1),"(cm)"
print "This was in:"
for num in range(len(month)):
    if max(rainList)==rainList[num]:
        print month[num]
print "\nHave a nice day"
raw_input()    

