#Users name
#Mostafa Rashed
#Last Rev. 23 Feb, 2012
#Takes the user's full name in one line and it outputs it back in lastname, firstname form

#Takes users first name and last name
user = raw_input("Please input the full name with first name first followed by last name ")
#Finds the space in between the first and last names
space = user.find(" ")
#Outputs it back as lastname, firstname
print user[space:] + ",", user[0:space+1]
raw_input()
