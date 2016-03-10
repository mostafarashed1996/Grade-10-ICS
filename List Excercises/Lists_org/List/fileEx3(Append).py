#Dictionary 
#User can check if a word is in the dictionary. If the word is not the dictionary then the user may add it 

#Open's dictionary as read 
#Creates a variable for the list, keepGoing and the line 
#Creates a while loop to read each line
#Creates a while loop to continue asking the user for words
#If the word is in the dictionary, print yes it is.
#Else, print that the word is not in the dictionary but it will be added

import os
wordFile=open("dictionary.txt","r")
listName=[]
keepGoing="y"
line="."
while line!="":
    line=wordFile.readline()
    line=line.rstrip("\n")
    listName.append(line)
while keepGoing[0].lower()=="y":
    word=raw_input("Enter a word which you would like to check in the dictionary :  ")
    if word in listName:
        print "Yes, this word is in the dictionary."
    else:
        print "The word was not in the dictionary"
        option=raw_input("Would you like to add the word?(y/n) ")
        if option=="y":
            listName.append(word)
        else:
            keepGoing=raw_input("Would you like to check another word(y/n): ")
            os.system("CLS")
            if keepGoing.lower()=="n":
                break
                print "Have a nice day"

wordFile.close()
outFile=open("dictionary.txt",'w')
listName.sort()
outFile.writelines()
raw_input()
