#Spell Checker
#Alisikander Ahmed 
#Last revised December 20th 2011
#This program will allow the user to check for words in a dictionary and in a paragraph

#Open the files as read
#Put text file into a string
#Split Text file
#Loop through whole list
#punctuation = ""
#if word[-1].isalnum() == False
#Save first part of the word to word
#Save last character to punctuation
#if not in dictionary
#dicChack = True
###while dicCheck == True
#   1
#   2
#   3
#Save new paragraph and dictinary

listName=[]
from os import system
textFile = open("Text.txt", "r")
paragraph = textFile.readline()
textFile.close()

print "Your current paragraph:\n"
print paragraph
raw_input("Press enter to edit.")
system("cls")

index = 0
for char in paragraph:
    if paragraph[index] == "-":
        paragraph[index] = " "
    index += 1

paragraph = paragraph.split()

dictionaryFile = open("dictionary.txt", "r")
dictionary = []
line = "random"
while line != "":
    line = dictionaryFile.readline()
    if line != "":
        line = line.rstrip("\n")
        dictionary.append(line)
dictionaryFile.close()

newParagraph = ""

for element in paragraph:
    output = element
    wordFound = False
    addOnNeeded = False
    addOn = ""

    for word in dictionary:
        for letter in element:
            if output.count(".") or output.count(",") or output.count("!") or output.count("?") or output.count("/") > 0:
                addOnNeeded = True
                addOn = element[-1]                 
                output = element[ :-1]
        
        if element.lower() == word.lower():
            wordFound = True
            
        
    if wordFound == False and output.isdigit() == False:
        print "The word '" + output + "' was not found in the dictionary."
        print "Please pick an option \n1)Change \n2)Skip and Add \n3)Skip "
        option=raw_input()
        if option=="1":
            output = raw_input("Please respell the word.")
            system("CLS")
        if option=="2":
            dictionaryFile = open("dictionary.txt","a")
            dictionaryFile.write("\n"+output)
            dictionaryFile.close()
            listName.append(output)
            listName.sort()
            system("CLS")
        if option=="3":
            print "Skipped"
            system("CLS")
    newParagraph += output + addOn + " "
listName=str(listName)
outFile = open("Text_revised.txt", "w")
outFile.write(newParagraph)
print "Your new paragraph:\n"
print newParagraph + "\n\n"
raw_input("Bye Bye\nHave a nice day.")



