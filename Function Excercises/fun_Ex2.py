#Index finder
#Mostafa Rashed
#Last Rev. 15 May 2012
#Converts the list finding to a string finding

#Set up a variable just incase you want to redo the program
redo = "Y"
#Setting up a loop
while redo.upper()=="Y":
    #Makes the number list
    numberlist = range(1,20)
    #Makes a find function to find the index later
    def find(num, numberlist):
        #Make the list a string
        numberlist = str(numberlist)
        #Get the index using this line
        numfind = numberlist.find(num)
        #Prints the index
        return numfind
    #Asks the user for the number they were wanting to check
    num = raw_input("What number do you want to check? ")
    #if the number is not located (-1 index) then it tells the user to try again
    if find(num,numberlist) == -1:
        #Notifies the user of the error
        print "Error, please try again"
    #Else if it isn't -1
    else:
        #Prints the digit that the user used and the index number of that digit
        print "The index of your digit (%d) is %d" %(num, find(num,numberlist))
        #Asks if the user wants to redo it
        redo = raw_input("Do you want to try again? (Y/N) ")
raw_input("Thanks for using the program!")
