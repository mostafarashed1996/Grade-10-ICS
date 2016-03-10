#Classnames for classmates
#Mostafa Rashed
#Last Rev. 11 April 2012
#Opens a text file for writing names, then when it is done you get to veiw the file. After that you can add as many additional names as you want in append mode then view the file a final time

#Imports os to clear the screen later
import os
#Opens the file to write names in
txt1=open("trolling.txt", "w")
#Sets a count variable to see how many names are inputted
count = 1
#Starts a while loop
while True:
    #Asks the user what name they want to input in the file and if they want to stop they need to write stop
    name=raw_input("Please enter a name #" + str(count) + " to write in the file. If you want to quit at any time, type 'Stop' ")
    #Sets an 'if' statement so it stops when they say 'stop'
    if name.upper()=="STOP":
        #Clears the screen
        os.system("clear")
        #Asks if they want to see the text file
        review=raw_input("Do you want to see your text file ? (Y/n) ")
        #If they said yes or 'y' then it will show them
        if review.upper()=="Y":
            #Closes the the text file
            txt1.close()
            #Opens it again in read mode
            txt2=open("trolling.txt", "r")
            #Sets the read variable to read the text
            read=" "
            #Sets a while loop
            while read !="":
                #Re-makes the read variable to read the text file
                read = txt2.read()
                #Removes the final "\n" so it looks 'cleaner'
                read = read[:-1]
                #At the end of the file, it will execute different commands.
                if read!="":
                    #It would clear the screen
                    os.system("clear")
                    #Prints the text file on the screen
                    print read
                    #Tells you how many different names there are
                    print "There are " + str(count - 1) + " names in the file"
                    #Closes the text file
                    txt2.close()
                    #Breaks the loop
                    break
            #Breaks the loop
            break
        #Makes an else statment incase they don't want to see the file's contents
        else:
            #Closes the text file
            txt1.close()
            #Breaks the loop
            break
    #Makes the count variable for each word counting
    count += 1
    #Writes in the text file and adds a new line at the end of each sentince
    txt1.write(name + "\n")
    #Clears the screen
    os.system("clear")
#Asks if they want to add any addtional names
more=raw_input("Do you want to add any more names? (Y/n) ")
#Clears the screen
os.system("clear")
#If statment to add more names if they said yes or 'y'
if more.upper()=="Y":
    #reopens the file in append mode
    txt3=open("trolling.txt", "a")
    #A while loop
    while True:
        #Asks the user what name they want to input in the file and if they want to stop they need to write stop
        name2 = raw_input("Please enter any additional names. Enter 'Stop' to quit. ")
        #Sets an 'if' statement so it stops when they say 'stop'
        if name2.upper()=="STOP":
            #Clears the screen
            os.system("clear")
            #Asks if they want to see the text file
            review=raw_input("Do you want to see your text file ? (Y/n) ")
            #If they said yes or 'y' then it will show them
            if review.upper()=="Y":
                #Closes the the text file
                txt3.close()
                #Opens it again in read mode
                txt4=open("trolling.txt", "r")
                #Sets the read variable to read the text
                read=" "
                #Sets a while loop
                while read !="":
                    #Re-makes the read variable to read the text file
                    read = txt4.read()
                    #Removes the final "\n" so it looks 'cleaner'
                    read = read[:-1]
                    #At the end of the file, it will execute different commands.
                    if read!="":
                        #It would clear the screen
                        os.system("clear")
                        #Prints the text file on the screen
                        print read
                        #Closes the text file
                        txt3.close()
                        #Breaks the loop
                        break
                #Breaks the loop
                break
            #Makes an else statment incase they don't want to see the file's contents
            else:
                #Closes the text file
                txt1.close()
                #Breaks the loop
                break
        #Writes in the text file and adds a new line at the end of each sentince
        txt3.write(name2 + "\n")
        #Clears the screen
        os.system("clear")
raw_input()
