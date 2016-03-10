#ICS2 Test 1-B - Program One -
#Mostafa Rashed
#Last Rev. March 9, 2012
#Takes a word from the user and either: get the length of the word, convert it to uppercase, or replace a substring with another

#"Import OS" to clear the screen later
import os
#Askes user to input the word
word = raw_input("Please enter the word you would like to use ")
#Askes the user what he wants to do with his word
selection = input("What would you like to do with your word? Would you like to 1-Get the length of the word, or 2- Convert the word to uppercase, or 3- replace one substring of your word with another substring? ")
#Clears the screen
os.system("clear")
#Using "if" to take his choice and process it, first for getting the length of the choice then out putting it back to the user.
if selection==1:
    length=len(word)
    print "The lenght of your word is " + str(length) + " characters long."
#Using "elif" to take his choice and process it if he didn't want choice #1. This is for the "Convert the word to uppercase" (#2)
elif selection==2:
    wordu=word.upper()
    print "Your word in uppercase is:", wordu
#Using "elif" to take his choice and process it if he didn't want choices #1 and #2. This is for "Replace one substring with another" (#3)
elif selection==3:
    rep=raw_input("What do you want to replace in your word? ")
    repment=raw_input("What do you want to replace it with? ")
    wordrep=word.replace(rep,repment)
    print "Here is your new word:", wordrep
raw_input("Thank you for using the program, hope you have a nice day! (Press any key to exit.) ")
