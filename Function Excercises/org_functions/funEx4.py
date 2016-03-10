# palindrome program
#Marko Alhamadani
#14/05/2012
# this program will ask the user to enter a word and it will determine whether it is a palindrome or not 

# make the function is_palindrome
import os
ask="yes"
def is_palindrome(word):
# make string filled in to get it backwards 
    backward = ""
    word = word.lower()
    for char in word:
        backward = char + backward
# if the word is equal to the word backwards it's a palindrome
    if word == backward or word==True:
        answer = word+" is a palindrome therefore word "+word+" is TRUE"
# if it's not the same it's not a palindrome
    else:
        answer = word+" is not a palindrome therefore word <"+word+"> is FALSE"
    return answer
# ask them for the word
while ask=="yes":
    word = raw_input("enter the word you are checking: ")
# give them the answer
    print is_palindrome(word)
    raw_input("Press enter to go again")
    os.system("CLS")
    

