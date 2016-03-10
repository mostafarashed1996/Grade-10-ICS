#Hangman
#Mostafa Rashed
#Last Rev. 26 April 2012
#Basic Python Hangman game for the funs :)

#Import OS so we can clear the screen later
import os
#Import time so we can delay some of the commands
import time
#Import random so we can choose random words from the list of words
import random
#Prints out a warm welcome to my game
print"""
 ________         __                              __         
|  |  |  |.-----.|  |.----.-----.--------.-----. |  |_.-----.
|  |  |  ||  -__||  ||  __|  _  |        |  -__| |   _|  _  |
|________||_____||__||____|_____|__|__|__|_____| |____|_____|
                                                             """   
print"""
888    888                                                      
888    888                                                      
888    888                                                      
8888888888 8888b. 88888b.  .d88b. 88888b.d88b.  8888b. 88888b.  
888    888    "88b888 "88bd88P"88b888 "888 "88b    "88b888 "88b 
888    888.d888888888  888888  888888  888  888.d888888888  888 
888    888888  888888  888Y88b 888888  888  888888  888888  888 
888    888"Y888888888  888 "Y88888888  888  888"Y888888888  888 
                               888                              
                          Y8b d88P                              """
#Asks the username of the player
name = raw_input("Username: ")
#Asks the user if they want to start the game or not
ignition = raw_input("Welcome to Hangman %s! Please choose one of the following:\n1)Start Game\n2)Quit\n" %name)
#If the user wants to start the game, they would go through my awesome loading animation.
if ignition == "1":
    os.system("CLS")
    print"""
.-.                   .-. _                        .---. 
: :                   : ::_;                       `--. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.              ,','
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   .'.'_ 
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  :____;
                                   .-. :                 
                                   `._.'                  """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                          ,-.  ,-.
: :                   : ::_;                       .'  :.'  :
: :    .--.  .--.   .-' :.-.,-.,-. .--.             `: : `: :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _     : :  : :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;    :_;  :_;
                                   .-. :                     
                                   `._.'                     """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                          ,-. .--. 
: :                   : ::_;                       .'  :: .; :
: :    .--.  .--.   .-' :.-.,-.,-. .--.             `: :`.  .'
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _     : :: .; :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;    :_;`.__.'
                                   .-. :                      
                                   `._.'                      """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                        .---. .---. 
: :                   : ::_;                       `--. :`--. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.              ,','  ,','
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   .'.'_ .'.'_ 
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  :____;:____;
                                   .-. :                       
                                   `._.'                       """
    time.sleep(0.5)
    os.system("CLS")
    print"""
.-.                   .-. _                        .---. .----.
: :                   : ::_;                       `--. :: .--'
: :    .--.  .--.   .-' :.-.,-.,-. .--.              ,','`. `. 
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   .'.'_ .-`, :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  :____;`.__.'
                                   .-. :                       
                                   `._.'                       """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                        .----..----.
: :                   : ::_;                       `--  ;`--  ;
: :    .--.  .--.   .-' :.-.,-.,-. .--.             .' '  ,',' 
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _    _`,`. : :  
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  `.__.' :_:  
                                   .-. :                       
                                   `._.'                       """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                        .----. .--. 
: :                   : ::_;                       : .--': ,. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.            `. `. : :: :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   .-`, :: :; :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  `.__.'`.__.'
                                   .-. :                       
                                   `._.'                       """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                          .-. .---. 
: :                   : ::_;                        .'.' `--. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.            .' '.   ,','
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   : .; :.'.'_ 
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  `.__.':____;
                                   .-. :                       
                                   `._.'                       """
    time.sleep(0.5)
    os.system("CLS")
    print"""
.-.                   .-. _                          .-. .--. 
: :                   : ::_;                        .'.': .; :
: :    .--.  .--.   .-' :.-.,-.,-. .--.            .' '.`._, :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   : .; :  : :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  `.__.'  :_:
                                   .-. :                      
                                   `._.'                      """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                         .--. .---. 
: :                   : ::_;                       : .; :`--. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.            `.  .'  ,','
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   : .; :.'.'_ 
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;  `.__.':____;
                                   .-. :                       
                                   `._.'                       """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                         .--. .---. 
: :                   : ::_;                       : .; :`--. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.            `._, :  ,','
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _      : :.'.'_ 
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;     :_::____;
                                   .-. :                       
                                   `._.'                       """
    time.sleep(0.5)
    os.system("CLS")
    print"""
.-.                   .-. _                         .--.  .--. 
: :                   : ::_;                       : .; :: .; :
: :    .--.  .--.   .-' :.-.,-.,-. .--.            `._, :`._, :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _      : :   : :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;     :_:   :_:
                                   .-. :                       
                                   `._.'                       """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                               ,-.
: :                   : ::_;                            .'  :
: :    .--.  .--.   .-' :.-.,-.,-. .--.             _____`: :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _   :_____:: :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;         :_;
                                   .-. :                     
                                   `._.'                     """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                         ,-.
: :                   : ::_;                      .'  :
: :    .--.  .--.   .-' :.-.,-.,-. .--.       _____`: :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _   :_____:: :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;         :_;
                                   .-. :               
                                   `._.'               """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                            ,-.
: :                   : ::_;                         .'  :
: :    .--.  .--.   .-' :.-.,-.,-. .--.          _____`: :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _   :_____:: :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;         :_;
                                   .-. :                  
                                   `._.'                  """
    time.sleep(1)
    os.system("CLS")
    print"""
.-.                   .-. _                          ,-. .--.  .--. 
: :                   : ::_;                       .'  :: ,. :: ,. :
: :    .--.  .--.   .-' :.-.,-.,-. .--.             `: :: :: :: :: :
: :__ ' .; :' .; ; ' .; :: :: ,. :' .; : _  _  _     : :: :; :: :; :
:___.'`.__.'`.__,_;`.__.':_;:_;:_;`._. ;:_;:_;:_;    :_;`.__.'`.__.'
                                   .-. :                            
                                   `._.'                            """
    time.sleep(0.5)
    os.system("CLS")
    #Sets a variable for 'keepgoing' so the user can replay the game
    keepgoing = "Y"
    #Sets a while variable so it can starts the loop for the guts of the game
    while keepgoing.upper() == "Y":
        #Asks the user if they want to play one or two player
        mode = raw_input("How many people are playing? (1/2) ")
        os.system("CLS")
        #If statement for the single player game
        if mode == "1":
            #Sets the variable to check the used letters later on
            wordcheck = ""
            #A list of words that the hangman application would use randomly using the random variable
            hangword = random.choice(["quote", "adept", "stone", "trunk", "event"])
            #Measures the length of the word and places underscores where the letters are
            blank = len(hangword) * "_ "
            #Prints out the blanks for the user to see
            print blank + "\n"
            #Prints a statement to tell the people how long the words are for their knowladge
            print "You have to guess a " + str(len(hangword)) + " letter word. Good luck. \n"
            #How many attempts you have
            attempts = 5
            #If you didn't run out of attempts, it would execute the following commands
            while attempts >= 1:
              #Sets a variable so the program understands if you win or if you lose
              strikes = 0
              #for the character that the user wrote is in the hangman word it would execute the floowing command
              for char in hangword:
                #if the character is in the letter checker
                if char in wordcheck:
                  #Print that caracter and replace the underscores
                  print char,
                else:
                  #If not, then it will still keep the underscore
                  print "_ ",
                  #And it adds a strike
                  strikes = strikes + 1
              #If you have zero strikes
              if strikes == 0:
                #Print that they are victorious
                print "Good job! You are victorius!"
                #Then it breaks the loop
                break
              #Asks the user what letter they want to guess
              letterguess = raw_input("Which letter do you think is in the blanks? Input and see! ")
              os.system("CLS")
              #If the length of the letter is more than one, it won't let you do so
              if len(letterguess)>1:
                  print "That is cheating! Only one letter please! "
                  #Reminds the user of what words they used
                  print "\nAs a reminder, here are the words you have guessed so far! " + wordcheck
              #If the letter that the user guessed, and he already guessed it before, it warns the user to try and write another one
              if letterguess in wordcheck:
                  print "Why waste an attempt? You have guessed this letter already!. "
                  #Reminds the user of what words they used
                  print "\nAs a reminder, here are the words you have guessed so far! " + wordcheck
              #If the length of the word is exactly one and it hasn't been guessed before,
              elif len(letterguess)==1 and letterguess not in wordcheck:
                  #It would change the word to lowercase
                  letterguess = letterguess.lower()
                  #it adds the word to the list of words already used
                  wordcheck = wordcheck + letterguess
                  #Reminds the user of what words they used
                  print "\nAs a reminder, here are the words you have guessed so far! " + wordcheck
                  #If the letter that was guessed was incorrect,
                  if letterguess not in hangword:
                      #It would subtract one from the attempts
                      attempts = attempts - 1
                      #Informs the user that they got it incorrect
                      print "Unfortunatly you have guessed the wrong letter. "
                      #Informs the amount of trys left
                      print "You have " + str(attempts) + " trys left.\n "
                      #It counts down the and create the hangman from 5 attempts to none
                      if attempts <5:      
                          print "  |------|------|"      
                          print "  |      O      |"
                      if attempts <4:
                          print "  |     \ /     |"
                      if attempts <3:
                          print "  |      |      |"
                      if attempts <2:
                          print "  |     / \     |"                                                
                      if attempts <1:
                          print "  |_____________|"
                          #Informs the user that it is the end and game over
                          print "\nOh no! Do you see what I see? The hangman is complete! THE HANGMAN IS COMPLETE! :(\nThe word you were guessing is: %s\nBetter luck next time!" %hangword
            #Asks the user if they want to play again
            keepgoing = raw_input("Do you want to play again? (Y/N) ")
        #If statement for the two player game
        if mode == "2":
            os.system("CLS")
            #Sets the variable to check the used letters later on
            wordcheck = ""
            #Asks a player to write the word the other player would guess
            hangword = raw_input("Type up a word that you want the other player to guess. Don't let him see what you are typing! ")
            os.system("CLS")
            #Makes it lowercase
            hangword = hangword.lower()
            #Measures the length of the word and places underscores where the letters are
            blank = len(hangword) * "_ "
            #Prints out the blanks for the user to see
            print blank + "\n"
            #Prints a statement to tell the people how long the words are for their knowladge
            print "You have to guess a " + str(len(hangword)) + " letter word. Good luck. \n\n\n\n\n"
            #How many attempts you have
            attempts = 5
            #If you didn't run out of attempts, it would execute the following commands
            while attempts >= 1:
              #Sets a variable so the program understands if you win or if you lose
              strikes = 0
              #for the character that the user wrote is in the hangman word it would execute the floowing command
              for char in hangword:
                #if the character is in the letter checker
                if char in wordcheck:
                  #Print that caracter and replace the underscores
                  print char,
                else:
                  #If not, then it will still keep the underscore
                  print "_ ",
                  #And it adds a strike
                  strikes = strikes + 1
              if strikes == 0:
                #Print that they are victorious
                print "Good job! You are victorius!"
                #Then it breaks the loop
                break
              #Asks the user what letter they want to guess
              letterguess = raw_input("Which letter do you think is in the blanks? Input and see! ")
              os.system("CLS")
              if len(letterguess)>1:
                  print "That is cheating! Only one letter please! "
                  #Reminds the user of what words they used
              if letterguess in wordcheck:
                  #If the letter that the user guessed, and he already guessed it before, it warns the user to try and write another one
                  print "Why waste an attempt? You have guessed this letter already!. "
              #If the length of the word is exactly one and it hasn't been guessed before,
              elif len(letterguess)==1 and letterguess not in wordcheck:
                  #It would change the word to lowercase
                  letterguess = letterguess.lower()
                  #it adds the word to the list of words already used
                  wordcheck = wordcheck + letterguess
                  #Reminds the user of what words they used
                  print "\nAs a reminder, here are the words you have guessed so far! " + wordcheck
                  #If the letter that was guessed was incorrect,
                  if letterguess not in hangword:
                      #It would subtract one from the attempts
                      attempts = attempts - 1
                      #Informs the user that they got it incorrect
                      print "Unfortunatly you have guessed the wrong letter. "
                      #Informs the amount of trys left
                      print "You have " + str(attempts) + " trys left.\n "
                      #It counts down the and create the hangman from 5 attempts to none
                      if attempts <5:
                          print "  |------|------|"      
                          print "  |      O      |"
                      if attempts <4:
                          print "  |     \ /     |"
                      if attempts <3:
                          print "  |      |      |"
                      if attempts <2:
                          print "  |     / \     |"                                                
                      if attempts <1:
                          print "  |_____________|"
                          #Informs the user that it is the end and game over
                          print "\nOh no! Do you see what I see? The hangman is complete! THE HANGMAN IS COMPLETE! :(\nThe word you were guessing is: %s\nBetter luck next time!" %hangword
#If you quit
else:
    #It bids you farwell
    print "Goodbye!"
    #Delays the execution by a second
    time.sleep(1)
    #It quits the program
    quit()
#It bids you farwell
print "Goodbye!"
#Delays the execution by a second
time.sleep(1)
#It quits the program
quit()
