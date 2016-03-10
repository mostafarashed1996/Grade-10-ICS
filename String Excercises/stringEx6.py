#Center Sentince
#Mostafa Rashed
#Last Rev. 2 March 2012
#It takes the sentince from the user and it shows it centered in the X number of field surronded by dots

#Asks user for the sentince that he wants at a max length of 60 characters
sen = raw_input("Please enter you sentince at a max of 60 characters ")
#Gets the length of the user's sentince
lsen = len(sen)
#Gets the user's prefered length of field for the dots to surround his/her sentince
field = input("Please enter a field length over " + str(lsen) + " characters and under 98 ")
#Sets the variable for the amount of dots for each side
dotlen = (field-lsen)/2
#Set a variable just in case of an odd number to add an extra dot
dotlen2= (field-lsen)%2
#Prints it out to the user tabbed
print " "*(lsen-dotlen) + "."*dotlen + sen + "."*(dotlen + dotlen2)
raw_input()
