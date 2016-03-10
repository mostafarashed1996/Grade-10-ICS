#Number-To-ASCII
#Numbers into binary
#Marko Alhamadani
#14/5/2012
#This is a program that converts numbers to ascii

print"""
    **************
    * Welcome to *
    *     My     *
    *  Program   *
    **************
    
This program converts numbers into binary
Continue to play.....
"""

#converts an inputed decimal into its binary equivalent
ask=raw_input("Do you want to play a game[Y/N]? ")
while ask[0].lower()=="y":
    #the 'places = 8' means that there are 8 character places in the binary.
    def deciToAscii(number):
        places = 8
        #set the variable ascii to nothing for future use 
        ascii = ""
        #put in while loop to keep doing the division below by 2 so each time the number is devisible by two it will go through this loop
        while number > 0:
            #using modulus to get remainder by 2
            ascii = str(number%2) + ascii
            #half it 
            number = number/2
        #if the final ascii has less than 8 characters, it'll find out how many more 0's it needs to fill the space.    
        if places > len(ascii):
            #algorithm
            addingMore = places - len(ascii)
            #putting the 0's in the empty places.
            ascii = "0"*addingMore + ascii
        #return the function ascii    
        return ascii
    #ask the user for the number
    number = input("\nEnter your number: ")
    #print the result after the inputed number goes through the loop
    print "Your Ascii number is ",deciToAscii(number)

    #ask if the user wants do go through the loop again
    ask=raw_input("\nDo you want to go again[Y/N]? ")
else:
    raw_input("Press enter to leave")
