#Word Checker
#Mostafa Rashed
#Checks the word of choice, and if its in the dictionary it would notify the user, if not then it would ask the user if he wants to add it into the program.

#Import 'os' to clear the screen later
import os
#Makes the 'keepgoing' variable to use for the loop later
keepgoing = "Y"
#Make a 'dictionary' variable to use as a list later
dictionary = []
#Make a variable so if the dictionary reaches an end it would stop appending.... later
dictword = " "
#Starts the loop
while keepgoing.upper() == "Y":
    #Opens the dictionary file in read mode
    dictfile = open("dictionary.txt","r")
    #Starts asking the person what word they want to input
    word = raw_input("Welcome to Mostafa's amazing dictionary!\nPlease enter a word that is 3-6 letters in length, to check in the dictionary ")
    #Lower-cases the word
    word = word.lower()
    #Makes an if statement for if the wored is greater than 2 and smaller than 7
    if len(word)>= 3 and len(word) <=6:
        #While statement for the dictword variable
        while dictword != "":
            #It reads the lines of the dictionary file
            dictword = dictfile.readline()
            #It strips line return from the lines
            dictword = dictword.rstrip("\n")
            #It appends the dictionary words in the brackets
            dictionary.append(dictword)
        #If the word is in the dictionary, then it will notify the user
        if word in dictionary:
            print "This word is in the dictionary"
        #Else statement for if the word is not in the dictionary
        else:
            #Asks the user if he wants to add or not
            add = raw_input("This word is not in the dictionary. Do you want to add this word to the dictionary? (Y/N) ")
            #If he wants then start the 'if' statement
            if add.upper() == "Y":
                #Closes the dictionary file
                dictfile.close()
                #Opens it again in append mode
                dictfile2 = open("dictionary.txt", "a")
                #Writes the word in the dictionary file
                write = dictfile2.write(word + "\n")
                #It appends the word in the dictionary list
                dictionary.append(word)
                #Closes the file
                dictfile2.close()
                #Notifies the user
                print "The word %s has been added to the list" %word
        #Keepgoing loop if they want to check a new word
        keepgoing = raw_input("Do you want to check another word? (Y/N) ")
    #Elif for words that are less than 3 then it won't accept it
    elif len(word) < 3:
        print "The word is less than 3 letters. Please try again"
        break
    #Elif for words that are greater than 6 then it won't accept it
    elif len(word) > 6:
        print "The word is more than 6 letters. Please try again"
raw_input("Thank you for using this dictionary! Have a good day!")
