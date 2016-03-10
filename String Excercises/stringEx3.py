#One Word per Line
#Mostafa Rashed
#Last Rev March 1 2012
#It takes a sentince and displayes it word per line

#Askes user to input his sentince
sen = raw_input("Please input your sentince ")
#Replaces the space with a new line, which will make one word per line
sen2 = sen.replace(" ","\n")
#Prints it out to the user
print sen2
raw_input()
