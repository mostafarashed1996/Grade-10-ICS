#Convert Miles to Kilometers
#Mostafa Rashed
#Last Rev. 23 March 2012
#Converts the miles (from  to the unit of kilometers

#Sets up "miles" variable
miles=0
#Prints the structure of the graph before the loop
print "Miles \t Kilometers \n ------ \t ---------- \n" 
#Starts a "while" loop
while True:
    #Sets mile to add one every time it loops
    miles += 1
    #Sets up kilometers conversion formula
    kilometers=miles*1.61
    #Prints them under the table
    print "%2d \t %.2f" %(miles, kilometers)
    #Breaks the program after 10 miles have been displayed
    if miles == 10:
        break
raw_input()
