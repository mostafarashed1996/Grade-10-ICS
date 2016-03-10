#Spellchecker
#Manny Er-Chua
#30 April 2012
#This program asks the user to input a word. Then it will check it against the dictionary and ask to add if you want. It will then ask for another word if wanted.

#Import
import os
import time
#Welcome
print "Welcome to the CG Spellchecker."
#Set variable and blank list
dictlist = []
#Open txt file and read
dictionary = open("dictionary.txt","r")
for x in range(9314):
    wordcheck = dictionary.readline()
    #Get rid of "\n"
    wordcheck = wordcheck.rstrip("\n")
    #Add word to list
    dictlist.append(wordcheck)
    
#Loop
while True:
    word = raw_input("What is the 3 - 6 letter word you would like to check the spelling of? (Type \"S\" to stop the program.) ")
    #If user inputs "S" print and break out of loop
    if word == "S":
        os.system("CLS")
        time.sleep(0.5)
        print "Thank you for using the CG Spellchecker. Lelouch vi Britannia commands you: Come again!"
        break
    #If word is in dictionary, print
    if word in dictlist:
        print word + " was in the dictionary."
    #Else print. Then ask if the user wants to add word
    else:
        print "The word wasn't in the dictionary."
        addword = raw_input("Would you like to add the word to the dictionary? Y/N: ")
        #If yes, append, sort.
        if addword.upper() == "Y" or addword.upper() == "YES":
            dictlist.append(word)
            dictlist.sort()
            #Open file and write
            dictionary = open("dictionary.txt","w")
            for x in dictlist:
                dictionary.write(x + "\n")
            #Close file
            dictionary.close()
            #Reset addword
            addword = ""
        #If no, print.
        if addword.upper() == "N" or addword.upper() == "NO":
            os.system("CLS")
            time.sleep(0.5)
            print "Thank you for using the CG Spellchecker. Lelouch vi Britannia commands you: Come again!"
            break
raw_input("\nPress enter to close.")
        
    
