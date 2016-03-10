#Serendipity Booksellers book club
#Mostafa Rashed
#Last Rev. 21 March 2012
#Takes the number of books this person got this month, and tells how much he/she earned in points for books she purchased this month

#Import os to clear the screen later
import os
#Asks how many books were purchased
books = int(raw_input("How many books were purchased from Serendipity Booksellers this month? "))
#Clear the screen
os.system("clear")
#Makes an if statment to see how many points he/she earned
if books == 0:
    print "You have earned 0 points because you have purchased 0 books this month."
elif books == 1:
    print "You have earned 5 points because you have purchased 1 book this month."
elif books == 2:
    point = 2 * 7.5
    print "You have earned %2d points because you have purchased 2 books this month." %point
elif books == 3:
    point = 3 * 10
    print "You have earned %2d points because you have purchased 3 books this month." %point
elif books >= 4:
    point = books * 15
    print "You have earned %2d points because you have purchased %2d books this month." %(point, books)
raw_input()
