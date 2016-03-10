#X's on the screen
#Mostafa Rashed
#Last Rev. March 1, 2012
#Takes a number from the user and squares it, then outputs it back to the user with X's in the same amount as the squared number

#Takes the number from the user
num = input("Please input the number you want ")
#Outputs the number multiply by the letter X for each line, multiply again by the number for the number of lines
print "\n"*49 + ("\t"*4 + "X"*num + "\n")*num + "\n"*49
raw_input()
