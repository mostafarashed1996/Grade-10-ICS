#Extention identifyer
#Mostafa Rashed
#Last Rev. 23 Feb, 2012
#Takes full name of a file and tells the user the extention of the file

#Takes the full name of the file from the user
file = raw_input("Please input the file name ")
#Identifys the "."
dot = file.find(".")
#Outputs the extention of the file
print file[dot:]
raw_input()
