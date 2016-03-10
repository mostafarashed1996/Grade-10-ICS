#Announcing Repetition
#Mostafa Rashed
#Last Rev. 23 March 2012
#Tells the user how many loops were executed

#Asks the user if he wants to start the loop
more = raw_input("Type 'More' to continue ")
#Sets the count variable
count = 0
#Sets a "while" variable for a loop
while more.upper()[0] == "M":
    #Makes the count (0) start adding one every time a loop is excecuted
    count += 1
    #Prints "Loop excecution number" plus the number of times a loop has occured
    print "Loop execution number " + str(count)
    #Excecutes the loop again by writing 'More'
    more = raw_input("Type 'More' to continue ")
raw_input()
