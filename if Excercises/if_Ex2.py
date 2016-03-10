#Even or Odd?
#Mostafa Rashed
#Last Rev. 21 March 2012
#Takes the user's sentince and tells you if it is an even number or an odd number

#Import OS for clearing the screen later
import os
#Gets the word from the user
word = raw_input("Please enter the word you want to use ")
#Make a length variable to get the number of letters in the word
length = len(word)
#Clears the screen
os.system("clear")
#Make an if function to get it to say if it is even
if length%2 == 0:
    word = word.lower()
    print "The word '%s' has an even number in length" %word
#Make an else function to get it to say if it is odd
else:
    word = word.lower()
    print "The word '%s' has an odd number in length" %word
raw_input("Thank you for using the program. Have a nice day ")
