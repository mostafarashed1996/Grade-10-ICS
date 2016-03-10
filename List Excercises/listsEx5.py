import time
import os
parafile = open("Text.txt", "r")
orgpara = parafile.readline()
parafile.close()
count = 0
for char in orgpara:
    if orgpara[count] == "-":
        orgpara[count] == " "
    count += 1
orgpara = orgpara.split()
dictfile = open("dictionary.txt", "r")
dictionary = []
checklist = []
dictwords = " "
while dictwords != "":
    dictwords = dictfile.readline()
    if dictwords != "":
        dictwords = dictwords.rstrip("\n")
        dictionary.append(dictwords)
dictfile.close()
newpara = ""
for x in orgpara:
    output = x
    locatedword = False
    addontf = False
    addon = ""
    for word in dictionary:
        for letter in x:
            if output.count("!") or output.count("?") or output.count(".") or output.count(",") or output.count("/")>0:
                addontf = True
                addon = x[-1]
                output = x[ :-1]
        if x.lower() == word.lower():
            locatedword = True
    if locatedword == False and output.isdigit() == False:
        choice = raw_input("The word '%s' was not found in the dictionary.\nPlease select an option:\n1)Change the word\n2)Add to dictionary\n3)Ignore\n" %output)
        if choice == "1":
            output = raw_input("Please enter the word you want to replace it with ")
            os.system("CLS")
        if choice == "2":
            dictfile2 = open("dictionary.txt","a")
            dictfile2.write("\n" + output)
            dictfile2.close()
            checklist.append(output)
            checklist.sort()
            os.system("CLS")
        if choice == "3":
            print "The word has been skipped"
            os.system("CLS")
    newpara += output + addon + " "
extract = open("Text2.txt", "w")
extract.write(newpara)
extract.close()
review = raw_input("Do you want to see your new paragraph? (Y/N) ")
if review.upper()=="Y":
    print "Your revised paragraph:\n\n%s\n" %newpara
    raw_input("Thank you for using the program! To exit please press 'Enter'! Have a nice day!")
else:
    raw_input("Thank you for using the program! To exit please press 'Enter'! Have a nice day!")
    
