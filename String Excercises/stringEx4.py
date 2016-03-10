#Makes a TDSB email
#Mostafa Rashed
#Last Rev. March 1, 2012
#Takes the first name and last name form the user and puts it into a TDSB email

#Takes user's first name
fname = raw_input("Please input the First Name ")
#Takes user's last name
lname = raw_input("Please input the Last Name ")
#Make email variable
email = "@tdsb.on.ca"
#Puts them all together to make the email
print fname + "." + lname + email
raw_input()
