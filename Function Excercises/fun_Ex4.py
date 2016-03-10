#Pallindrome checker
#Mostafa Rashed
#Last Rev. 16 May 2012
#Checks if a word is a pallindrome or not

#imoport 'os' to clear the screen later
import os
#Prints a nice welcome message
print "Welcome to Mostafa's awesome palindrome word checker!"
#Define the function to check if the word is a pallindrome
def palichkr(word):
    #'Backwords' variable set
    backwards = ""
    #lower-cases the word
    word = word.lower()
    #for loop to add it backwards
    for char in word:
        #Adds the characters backwards
        backwards = char + backwards
    #if the word is exactly the same as it is backwards
    if word == backwards:
        #Returns back if it is a palindrome or not
        return "'%s' is a palindrome." %word
    #if it isn't
    else:
        #Then it tells the user that it is not a palindrome
        return "'%s' is not a palindrome." %word
#Set a redo variable to use if the person wants to redo the once
redo = "Y"
#While loop
while redo.upper()=="Y":
    #Asks the user for the word
    word = raw_input("To get started, please write the word you want to check ")
    #Prints the answer
    print palichkr(word)
    #Asks the user if they want to try again
    redo = raw_input("Do you want to redo? (Y/N) ")
    #Clears the screen
    os.system("CLS")
raw_input("Have a nice day!")
