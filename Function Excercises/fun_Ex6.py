#Dec to Bin
#Mostafa Rashed
#17 May 2012
#Program that converts normal numbers to binary

#Redo variable for the loop
redo = "Y"
#While loop for the user to convert the number
while redo.upper()=="Y":
    #Defines the conversion function
    def dectobin(number):
        #Sets the binary variable
        bina = ""
        #While loop for conversion process
        while True:
            #Using the modulus way to get the remainer of the number by 2
            bina = str(number%2) + bina
            #Then it halves the number
            number = number/2
        #Returns the binary variable
        return bina
    #Asks the user to input thier number to convert
    number = input("Please enter your number: ")
    #Prints the number back to the user
    print "Your binary number is " + dectobin(number)
    #Asks if they want to do it again or not
    redo = raw_input("Do you want to go again? Y/N? ")
raw_input("Have a nice day!")
