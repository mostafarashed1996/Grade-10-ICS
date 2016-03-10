#Dictionary 
#User can check if a word is in the dictionary. If the word is not the dictionary then the user may add it 

#Open's dictionary as read 
#Creates a variable for the list, keepGoing and the line 
#Creates a while loop to read each line
#Creates a while loop to continue asking the user for words
#If the word is in the dictionary, print yes it is.
#Else, print that the word is not in the dictionary but it will be added
import time
import os
wordFile=open("dictionary.txt","r")
listName=[]
keepGoing="y"
line="."
while line!="":
    line=wordFile.readline()
    line=line.rstrip("\n")
    listName.append(line)
print "The rules are:\n   1.The word has to be less than 6 characters\n   2.The word has to be greater than 3 characters\n"
while keepGoing[0].lower()=="y":
    word=raw_input("Enter a word which you would like to check in the dictionary :  ")
    os.system("CLS")
    if word in listName:
        print "Yes, this word IS in the dictionary."
    elif word.isdigit==True:
        print "this is not a valid word"
    else:
        print "The word is not in the dictionary"
        option=raw_input("Would you like to add the word?(y/n) ")
        if option=="y":
            print "The word has been added"
            listName.append(word)
            listName.sort()
            wordFile.close()
            wordFile=open("dictionary.txt","a")
        else:
            keepGoing=raw_input("Would you like to check another word(y/n): ")
            os.system("CLS")
            if keepGoing.lower()=="n":
                break
                print "Have a nice day"
if word.len()>=6 and word.len()<=3:
    print "SADJHASKJDHJKASDHKASJDHKHD:"
wordFile.close()
outFile=open("dictionary.txt",'w')
listName.sort()
outFile.writelines()
raw_input()
