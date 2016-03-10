#All ASCII Characters
#Mostafa Rashed
#Last Rev. 25 March 2012
#Displays all the ASCII characters from 0 to 225

#Makes the 'count' variable
count = -1
#Starts the loop
while True:
    #Adds 1 to count for every loop
    count += 1
    #Gives the numbers beside the characters to the user
    print "%d: " %count + chr(count) + "\t",
    #If statment to break the loop after the 225th character
    if count == 225:
        break
raw_input()
