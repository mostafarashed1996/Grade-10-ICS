#Class Marker
#Last Revised: Dec 10, 2011
#Alisikander Ahmed 
#Program generates list of random marks

#Import random 
#Create a variable for an empty list 
#Generates mark for 24 students in a while loop
#Appends mark to list 
#Print mark
#Calculates highest mark
#Prints highest mark
#Prints average 


import random
classList=[]
length=0
average=0
topMark=0
counter=0

print "    Class marks \n   -------------"
while length<24:
    mark=random.randint(0,100)
    classList.append(mark)
    length=length+1
    average=average+mark
    counter+=1
    print mark
    if topMark<mark:
        topMark=mark
classAverage=average/24

print "\nClass average:" , round((average/24.0),2) , "%"
print "Highest Mark:", topMark , "%"

raw_input()
