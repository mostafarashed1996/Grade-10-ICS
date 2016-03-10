import pygame, sys, os, time, random, inputbox
from pygame.locals import * 
from pygame.color import THECOLORS

## If you get the no available video device error, copy and paste the below code ##
import platform
if platform.system() == "Windows":
    os.environ['SDL_VIDEODRIVER'] = 'windib'
### If you get the no available video device error, copy and paste the above code ###

pygame.init() 
clock=pygame.time.Clock()
window = pygame.display.set_mode((1024, 480)) 
pygame.display.set_caption('Sketch It! v1.0') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)

#The screen is the Drawing window
screen.fill(THECOLORS['white'])
mainmenu = pygame.image.load("Sketchit.gif").convert()
screen.blit(mainmenu, (0,0))
event = pygame.event.get()
pygame.display.update()
#Loads, using the pygame mixer, the song that I will be playing
pygame.mixer.music.load('Sketchsong.ogg')
#It is playing in an infinite loop
pygame.mixer.music.play(-1,0.0)
#Define the "play" function that holds the game itself
def play():
    #While loop
    while True:
        #Sets up the events variable
        events=pygame.event.get()
        #For loop to take the movements of the keys/mouse movements
        for ev in events:
            #Sets up the mouse location variable
            mouseloc = pygame.mouse.get_pos()
            #Sets up the mouse button variable
            mousebut = pygame.mouse.get_pressed()
            #if statement for one player mode
            if mouseloc[0] >= 375 and mouseloc[0] <= 560 and mouseloc[1] >= 101 and mouseloc[1] <= 157 and mousebut[0] == 1:
                #Sets up the True/False statements for things that allow painting, erasing, loop, drawing word, different colours for the brush
                painting = False
                erasing = False
                keepGoing = True
                newword = True
                red = False
                blue = False
                green = False
                yellow = False
                orange = False
                brown = False
                black = True
                purple = False
                white = False
                wordlist = []
                #It loads the default brush
                brush = pygame.image.load("black2.gif")
                #Fill the background of the screen with white
                screen.fill((255, 255, 255))
                #Loads the tutorial image
                tut = pygame.image.load("tut.gif").convert()
                #Blits it on the screen
                screen.blit(tut, (0,0))
                #Updates the display to show the change
                pygame.display.update()
                #Waits 5 seconds to give time to the user to read
                pygame.time.wait(5000)
                #Fill the background of the screen with white
                screen.fill((255, 255, 255))
                #Loads the background image
                bg = pygame.image.load("bg.gif").convert()
                #Blits it on the screen
                screen.blit(bg, (0,0))
                #Updates the display to show the change
                pygame.display.update()
                clock.tick(60)
                #While loop
                while keepGoing:
                    #Sets up a while loop
                    while newword == True:
                        #Words in the lists that are going to be told to the user to draw
                        drawlist = ["Tree", "Duck", "House", "Sunglasses", "Firetruck", "Sun", "Phone"]
                        #This will choose a random word from the list
                        drawword = drawlist[random.randint(0,6)]
                        #The font that will be used
                        drawfont = pygame.font.SysFont("Franklin Gothic Demi",38)
                        #Renders the word on the screen
                        drawtext = drawfont.render("Draw: %s!"%drawword,True,(0,0,0))
                        #Blits it on the screen
                        screen.blit(drawtext,(400,52))
                        #Updates the display
                        pygame.display.update()
                        #Makes the variable False so it can break the loop
                        newword = False
                    #Sets up the mouse location variable
                    mouseloc = pygame.mouse.get_pos()
                    #Events variable
                    events=pygame.event.get()
                    #For loop to take the movements of the keys/mouse movements
                    for ev in events:
                        #If statement for the menu button
                        if mouseloc[0] >= 0 and mouseloc[0] <= 134 and mouseloc[1] >= 0 and mouseloc[1] <= 26:
                            #if the a mouse button is down on the menu button, it will take you to the main menu
                            if ev.type == MOUSEBUTTONDOWN:
                                mainmenu()
                        #if the mouse is in the middle part of the screen (or the drawing area)
                        if mouseloc[0] >= 150 and mouseloc[0] <= 830 and mouseloc[1] >= 0 and mouseloc[1] <= 480:
                            #If any mouse button is down then you can draw
                            if ev.type == MOUSEBUTTONDOWN:
                                painting = True
                                #Copy variable which allows the user to use the backspace button to undo your action
                                copy=screen.copy()
                            #You can never paint if no mouse buttons are pressed
                            elif ev.type == MOUSEBUTTONUP:
                                painting = False
                        #Multiple if statements for different colours
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 250 and mouseloc[1] <= 276 and mousebut[0] == 1:
                            red = True
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("red2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 250 and mouseloc[1] <= 276 and mousebut[0] == 1:
                            red = False
                            blue = True
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("blue2.gif")
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 292 and mouseloc[1] <= 318 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = True
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("green2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 292 and mouseloc[1] <= 318 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = True
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("yellow2.gif")
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 331 and mouseloc[1] <= 357 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = True
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("orange2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 331 and mouseloc[1] <= 357 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = True
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("brown2.gif")
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 369 and mouseloc[1] <= 396 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = True
                            purple = False
                            white = False
                            brush = pygame.image.load("black2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 369 and mouseloc[1] <= 396 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = True
                            white = False
                            brush = pygame.image.load("purple2.gif")
                        if mouseloc[0] >= 68 and mouseloc[0] <= 118 and mouseloc[1] >= 423 and mouseloc[1] <= 444 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = True
                            brush = pygame.image.load("white2.gif")
                        #Clear screen button
                        if mouseloc[0] >= 80 and mouseloc[0] <= 140 and mouseloc[1] >= 457 and mouseloc[1] <= 479:
                            if ev.type == MOUSEBUTTONDOWN:
                                screen.fill((255, 255, 255))
                                bg = pygame.image.load("bg.gif").convert()
                                screen.blit(bg, (0,0))
                                pygame.display.update()
                        #Different sizes for the colour brushes.
                        if mouseloc[0] >= 838 and mouseloc[0] <= 939 and mouseloc[1] >= 252 and mouseloc[1] <= 350 and mousebut[0] == 1:
                            if red == True:
                                brush = pygame.image.load("red1.gif")
                            if blue == True:
                                brush = pygame.image.load("blue1.gif")
                            if green == True:
                                brush = pygame.image.load("green1.gif")
                            if yellow == True:
                                brush = pygame.image.load("yellow1.gif")
                            if orange == True:
                                brush = pygame.image.load("orange1.gif")
                            if brown == True:
                                brush = pygame.image.load("brown1.gif")
                            if black == True:
                                brush = pygame.image.load("black1.gif")
                            if purple == True:
                                brush = pygame.image.load("purple1.gif")
                            if white == True:
                                brush = pygame.image.load("white1.gif")
                        if mouseloc[0] >= 856 and mouseloc[0] <= 906 and mouseloc[1] >= 191 and mouseloc[1] <= 239 and mousebut[0] == 1:
                            if red == True:
                                brush = pygame.image.load("red2.gif")
                            if blue == True:
                                brush = pygame.image.load("blue2.gif")
                            if green == True:
                                brush = pygame.image.load("green2.gif")
                            if yellow == True:
                                brush = pygame.image.load("yellow2.gif")
                            if orange == True:
                                brush = pygame.image.load("orange2.gif")
                            if brown == True:
                                brush = pygame.image.load("brown2.gif")
                            if black == True:
                                brush = pygame.image.load("black2.gif")
                            if purple == True:
                                brush = pygame.image.load("purple2.gif")
                            if white == True:
                                brush = pygame.image.load("white2.gif")
                        if mouseloc[0] >= 869 and mouseloc[0] <= 880 and mouseloc[1] >= 163 and mouseloc[1] <= 175 and mousebut[0] == 1:
                            if red == True:
                                brush = pygame.image.load("red3.gif")
                            if blue == True:
                                brush = pygame.image.load("blue3.gif")
                            if green == True:
                                brush = pygame.image.load("green3.gif")
                            if yellow == True:
                                brush = pygame.image.load("yellow3.gif")
                            if orange == True:
                                brush = pygame.image.load("orange3.gif")
                            if brown == True:
                                brush = pygame.image.load("brown3.gif")
                            if black == True:
                                brush = pygame.image.load("black3.gif")
                            if purple == True:
                                brush = pygame.image.load("purple3.gif")
                            if white == True:
                                brush = pygame.image.load("white3.gif")
                        #If you click the finish button, it will load a new word, after it erases the screen
                        if mouseloc[0] >= 858 and mouseloc[0] <= 974 and mouseloc[1] >= 450 and mouseloc[1] <= 480:
                            if ev.type == MOUSEBUTTONDOWN:
                                #Does the usual pattern
                                screen.fill((255, 255, 255))
                                bg = pygame.image.load("bg.gif").convert()
                                screen.blit(bg, (0,0))
                                pygame.display.update()
                                #Newword = True means that it can re launch the random word loop
                                newword = True
                        #if the backspace is pressed, then it will "undo"
                        if ev.type == KEYDOWN and ev.key == K_BACKSPACE:
                            erasing = True
                        #if it isn't pressed, it won't undo
                        if ev.type == KEYUP and ev.key == K_BACKSPACE:
                            erasing = False
                        elif ev.type == QUIT:
                            keepGoing=False   # Stop the program, it's detected quit...
                    #if statmenet to identify what "painting" does when its true
                    if painting == True:
                        #Blits
                        screen.blit(brush,(mouseloc[0]-20,mouseloc[1]-20))
                        #Update display
                        pygame.display.update()
                    #if statement to identify what "erasing" does when its true
                    elif erasing == True:
                        #Blis screen with the state of screen before the last "painting" event
                        screen.blit(copy,(0,0))
                        #updates the screen
                        pygame.display.update()
            #if statment for the two player mode
            if mouseloc[0] >= 375 and mouseloc[0] <= 560 and mouseloc[1] >= 171 and mouseloc[1] <= 227 and mousebut[0] == 1:
                #Sets up the True/False statements for things that allow painting, erasing, loop, word for guessing (multiplayer), different colours for the brush
                painting = False
                erasing = False
                keepGoing = True
                guessword = False
                red = False
                blue = False
                green = False
                yellow = False
                orange = False
                brown = False
                black = True
                purple = False
                white = False
                #It loads the default brush
                brush = pygame.image.load("black2.gif")
                #Fill the background of the screen with white
                screen.fill((255, 255, 255))
                #Loads the tutorial image
                tut2 = pygame.image.load("tut2.gif").convert()
                #Blits it on the screen
                screen.blit(tut2, (0,0))
                #Updates the display to show the change
                pygame.display.update()
                #Waits 5 seconds to give time to the user to read
                pygame.time.wait(5000)
                #Fill the background of the screen with white
                screen.fill((255, 255, 255))
                #Loads the background image
                bg2 = pygame.image.load("bg2.gif").convert()
                #Blits it on the screen
                screen.blit(bg2, (0,0))
                #Updates the display to show the change
                pygame.display.update()
                #Font setups for use later
                headingFont=pygame.font.SysFont("Arial Black",20)
                myfont = pygame.font.SysFont("Times New Roman", 25)
                #Testvalue variable that is needed for inputbox
                textValue=""
                pygame.display.update()
                clock.tick(60)
                #While loop
                while keepGoing:
                    #Sets up a while loop
                    if guessword == True:
                        #Imports the following from a text box (The text box is NOT mine) it is an extention
                        answer = inputbox.ask(screen, "Your guess")
                        print inputbox.test
                        #Fill white
                        screen.fill((255, 255, 255))
                        #Loads the background image
                        bg2 = pygame.image.load("bg2.gif").convert()
                        #Blits it
                        screen.blit(bg2, (0,0))
                        #Updates the display
                        pygame.display.update()
                        #Guessword is False so it is 
                        guessword = False
                    #Sets up the mouse location variable
                    mouseloc = pygame.mouse.get_pos()
                    #Events variable
                    events=pygame.event.get()
                    #For loop to take the movements of the keys/mouse movements
                    for ev in events:
                        #If statement for the menu button
                        if mouseloc[0] >= 0 and mouseloc[0] <= 134 and mouseloc[1] >= 0 and mouseloc[1] <= 26:
                            if ev.type == MOUSEBUTTONDOWN:
                                mainmenu()
                        #If any mouse button is down then you can draw
                        if mouseloc[0] >= 150 and mouseloc[0] <= 830 and mouseloc[1] >= 0 and mouseloc[1] <= 480:
                            if ev.type == MOUSEBUTTONDOWN:
                                painting = True
                                #Copy variable which allows the user to use the backspace button to undo your action
                                copy=screen.copy()
                            #You can never paint if no mouse buttons are pressed
                            elif ev.type == MOUSEBUTTONUP:
                                painting = False
                        #Multiple if statements for different colours
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 250 and mouseloc[1] <= 276 and mousebut[0] == 1:
                            red = True
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("red2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 250 and mouseloc[1] <= 276 and mousebut[0] == 1:
                            red = False
                            blue = True
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("blue2.gif")
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 292 and mouseloc[1] <= 318 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = True
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("green2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 292 and mouseloc[1] <= 318 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = True
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("yellow2.gif")
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 331 and mouseloc[1] <= 357 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = True
                            brown = False
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("orange2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 331 and mouseloc[1] <= 357 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = True
                            black = False
                            purple = False
                            white = False
                            brush = pygame.image.load("brown2.gif")
                        if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 369 and mouseloc[1] <= 396 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = True
                            purple = False
                            white = False
                            brush = pygame.image.load("black2.gif")
                        if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 369 and mouseloc[1] <= 396 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = True
                            white = False
                            brush = pygame.image.load("purple2.gif")
                        if mouseloc[0] >= 68 and mouseloc[0] <= 118 and mouseloc[1] >= 423 and mouseloc[1] <= 444 and mousebut[0] == 1:
                            red = False
                            blue = False
                            green = False
                            yellow = False
                            orange = False
                            brown = False
                            black = False
                            purple = False
                            white = True
                            brush = pygame.image.load("white2.gif")
                        #Clear screen button
                        if mouseloc[0] >= 80 and mouseloc[0] <= 140 and mouseloc[1] >= 457 and mouseloc[1] <= 479:
                            if ev.type == MOUSEBUTTONDOWN:
                                screen.fill((255, 255, 255))
                                bg2 = pygame.image.load("bg2.gif").convert()
                                screen.blit(bg2, (0,0))
                                pygame.display.update()
                        #Different sizes for the colour brushes.
                        if mouseloc[0] >= 838 and mouseloc[0] <= 939 and mouseloc[1] >= 252 and mouseloc[1] <= 350 and mousebut[0] == 1:
                            if red == True:
                                brush = pygame.image.load("red1.gif")
                            if blue == True:
                                brush = pygame.image.load("blue1.gif")
                            if green == True:
                                brush = pygame.image.load("green1.gif")
                            if yellow == True:
                                brush = pygame.image.load("yellow1.gif")
                            if orange == True:
                                brush = pygame.image.load("orange1.gif")
                            if brown == True:
                                brush = pygame.image.load("brown1.gif")
                            if black == True:
                                brush = pygame.image.load("black1.gif")
                            if purple == True:
                                brush = pygame.image.load("purple1.gif")
                            if white == True:
                                brush = pygame.image.load("white1.gif")
                        if mouseloc[0] >= 856 and mouseloc[0] <= 906 and mouseloc[1] >= 191 and mouseloc[1] <= 239 and mousebut[0] == 1:
                            if red == True:
                                brush = pygame.image.load("red2.gif")
                            if blue == True:
                                brush = pygame.image.load("blue2.gif")
                            if green == True:
                                brush = pygame.image.load("green2.gif")
                            if yellow == True:
                                brush = pygame.image.load("yellow2.gif")
                            if orange == True:
                                brush = pygame.image.load("orange2.gif")
                            if brown == True:
                                brush = pygame.image.load("brown2.gif")
                            if black == True:
                                brush = pygame.image.load("black2.gif")
                            if purple == True:
                                brush = pygame.image.load("purple2.gif")
                            if white == True:
                                brush = pygame.image.load("white2.gif")
                        if mouseloc[0] >= 869 and mouseloc[0] <= 880 and mouseloc[1] >= 163 and mouseloc[1] <= 175 and mousebut[0] == 1:
                            if red == True:
                                brush = pygame.image.load("red3.gif")
                            if blue == True:
                                brush = pygame.image.load("blue3.gif")
                            if green == True:
                                brush = pygame.image.load("green3.gif")
                            if yellow == True:
                                brush = pygame.image.load("yellow3.gif")
                            if orange == True:
                                brush = pygame.image.load("orange3.gif")
                            if brown == True:
                                brush = pygame.image.load("brown3.gif")
                            if black == True:
                                brush = pygame.image.load("black3.gif")
                            if purple == True:
                                brush = pygame.image.load("purple3.gif")
                            if white == True:
                                brush = pygame.image.load("white3.gif")
                        #If you click the guess buttion if will make guess word true and it will let the user input a guess
                        if mouseloc[0] >= 858 and mouseloc[0] <= 974 and mouseloc[1] >= 450 and mouseloc[1] <= 480:
                            if ev.type == MOUSEBUTTONDOWN:
                                guessword = True
                        #if the backspace is pressed, then it will "undo"
                        if ev.type == KEYDOWN and ev.key == K_BACKSPACE:
                            erasing = True
                        #if it isn't pressed, it won't undo
                        if ev.type == KEYUP and ev.key == K_BACKSPACE:
                            erasing = False
                        elif ev.type == QUIT:
                            keepGoing=False   # Stop the program, it's detected quit...
                    #if statmenet to identify what "painting" does when its true
                    if painting == True:
                        #Blits
                        screen.blit(brush,(mouseloc[0]-20,mouseloc[1]-20))
                        #Update display
                        pygame.display.update()
                    #if statement to identify what "erasing" does when its true
                    elif erasing == True:
                        #Blis screen with the state of screen before the last "painting" event
                        screen.blit(copy,(0,0))
                        #updates the screen
                        pygame.display.update()

#Define the "freemode" mode.
def freemode():
    #Very similar functions as abouve. This is just a paint program, without any game approach to it.
    painting = False
    erasing = False
    keepGoing = True
    red = False
    blue = False
    green = False
    yellow = False
    orange = False
    brown = False
    black = True
    purple = False
    white = False
    brush = pygame.image.load("black2.gif")
    while keepGoing:
        clock.tick(60)
        mouseloc = pygame.mouse.get_pos()
        events=pygame.event.get()
        for ev in events:
            if mouseloc[0] >= 0 and mouseloc[0] <= 134 and mouseloc[1] >= 0 and mouseloc[1] <= 26:
                if ev.type == MOUSEBUTTONDOWN:
                    mainmenu()
            if mouseloc[0] >= 150 and mouseloc[0] <= 830 and mouseloc[1] >= 0 and mouseloc[1] <= 480:
                if ev.type == MOUSEBUTTONDOWN:
                    painting = True
                    copy=screen.copy()
                elif ev.type == MOUSEBUTTONUP:
                    painting = False
            if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 250 and mouseloc[1] <= 276 and mousebut[0] == 1:
                red = True
                blue = False
                green = False
                yellow = False
                orange = False
                brown = False
                black = False
                purple = False
                white = False
                brush = pygame.image.load("red2.gif")
            if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 250 and mouseloc[1] <= 276 and mousebut[0] == 1:
                red = False
                blue = True
                green = False
                yellow = False
                orange = False
                brown = False
                black = False
                purple = False
                white = False
                brush = pygame.image.load("blue2.gif")
            if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 292 and mouseloc[1] <= 318 and mousebut[0] == 1:
                red = False
                blue = False
                green = True
                yellow = False
                orange = False
                brown = False
                black = False
                purple = False
                white = False
                brush = pygame.image.load("green2.gif")
            if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 292 and mouseloc[1] <= 318 and mousebut[0] == 1:
                red = False
                blue = False
                green = False
                yellow = True
                orange = False
                brown = False
                black = False
                purple = False
                white = False
                brush = pygame.image.load("yellow2.gif")
            if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 331 and mouseloc[1] <= 357 and mousebut[0] == 1:
                red = False
                blue = False
                green = False
                yellow = False
                orange = True
                brown = False
                black = False
                purple = False
                white = False
                brush = pygame.image.load("orange2.gif")
            if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 331 and mouseloc[1] <= 357 and mousebut[0] == 1:
                red = False
                blue = False
                green = False
                yellow = False
                orange = False
                brown = True
                black = False
                purple = False
                white = False
                brush = pygame.image.load("brown2.gif")
            if mouseloc[0] >= 53 and mouseloc[0] <= 78 and mouseloc[1] >= 369 and mouseloc[1] <= 396 and mousebut[0] == 1:
                red = False
                blue = False
                green = False
                yellow = False
                orange = False
                brown = False
                black = True
                purple = False
                white = False
                brush = pygame.image.load("black2.gif")
            if mouseloc[0] >= 93 and mouseloc[0] <= 119 and mouseloc[1] >= 369 and mouseloc[1] <= 396 and mousebut[0] == 1:
                red = False
                blue = False
                green = False
                yellow = False
                orange = False
                brown = False
                black = False
                purple = True
                white = False
                brush = pygame.image.load("purple2.gif")
            if mouseloc[0] >= 68 and mouseloc[0] <= 118 and mouseloc[1] >= 423 and mouseloc[1] <= 444 and mousebut[0] == 1:
                red = False
                blue = False
                green = False
                yellow = False
                orange = False
                brown = False
                black = False
                purple = False
                white = True
                brush = pygame.image.load("white2.gif")
            if mouseloc[0] >= 80 and mouseloc[0] <= 140 and mouseloc[1] >= 457 and mouseloc[1] <= 479:
                if ev.type == MOUSEBUTTONDOWN:
                    screen.fill((255, 255, 255))
                    bg3 = pygame.image.load("bg3.gif").convert()
                    screen.blit(bg, (0,0))
                    pygame.display.update()
            if mouseloc[0] >= 838 and mouseloc[0] <= 939 and mouseloc[1] >= 252 and mouseloc[1] <= 350 and mousebut[0] == 1:
                if red == True:
                    brush = pygame.image.load("red1.gif")
                if blue == True:
                    brush = pygame.image.load("blue1.gif")
                if green == True:
                    brush = pygame.image.load("green1.gif")
                if yellow == True:
                    brush = pygame.image.load("yellow1.gif")
                if orange == True:
                    brush = pygame.image.load("orange1.gif")
                if brown == True:
                    brush = pygame.image.load("brown1.gif")
                if black == True:
                    brush = pygame.image.load("black1.gif")
                if purple == True:
                    brush = pygame.image.load("purple1.gif")
                if white == True:
                    brush = pygame.image.load("white1.gif")
            if mouseloc[0] >= 856 and mouseloc[0] <= 906 and mouseloc[1] >= 191 and mouseloc[1] <= 239 and mousebut[0] == 1:
                if red == True:
                    brush = pygame.image.load("red2.gif")
                if blue == True:
                    brush = pygame.image.load("blue2.gif")
                if green == True:
                    brush = pygame.image.load("green2.gif")
                if yellow == True:
                    brush = pygame.image.load("yellow2.gif")
                if orange == True:
                    brush = pygame.image.load("orange2.gif")
                if brown == True:
                    brush = pygame.image.load("brown2.gif")
                if black == True:
                    brush = pygame.image.load("black2.gif")
                if purple == True:
                    brush = pygame.image.load("purple2.gif")
                if white == True:
                    brush = pygame.image.load("white2.gif")
            if mouseloc[0] >= 869 and mouseloc[0] <= 880 and mouseloc[1] >= 163 and mouseloc[1] <= 175 and mousebut[0] == 1:
                if red == True:
                    brush = pygame.image.load("red3.gif")
                if blue == True:
                    brush = pygame.image.load("blue3.gif")
                if green == True:
                    brush = pygame.image.load("green3.gif")
                if yellow == True:
                    brush = pygame.image.load("yellow3.gif")
                if orange == True:
                    brush = pygame.image.load("orange3.gif")
                if brown == True:
                    brush = pygame.image.load("brown3.gif")
                if black == True:
                    brush = pygame.image.load("black3.gif")
                if purple == True:
                    brush = pygame.image.load("purple3.gif")
                if white == True:
                    brush = pygame.image.load("white3.gif")
            if ev.type == KEYDOWN and ev.key == K_BACKSPACE:
                erasing = True
            if ev.type == KEYUP and ev.key == K_BACKSPACE:
                erasing = False
            elif ev.type == QUIT:
                keepGoing=False   # Stop the program, it's detected quit...
        if painting == True:
            screen.blit(brush,(mouseloc[0]-20,mouseloc[1]-20))
            pygame.display.update()
        elif erasing == True:
            screen.blit(copy,(0,0))
            pygame.display.update()

#Defines "mainmenu"
def mainmenu():
    #Keepgoing variable for the loop
    keepGoing=True
    #While loop
    while keepGoing:
        #Fill the background of the screen with white
        screen.fill((255, 255, 255))
        #Loads the menu image
        mainmenu = pygame.image.load("Sketchit.gif").convert()
        #Blits it on the screen
        screen.blit(mainmenu, (0,0))
        #Updates the display to show the change
        pygame.display.update()
        #Events variable
        events=pygame.event.get()
        #For loop to take the movements of the keys/mouse movements
        for ev in events:
            #Sets up the mouse location variable
            mouseloc = pygame.mouse.get_pos()
            #Sets up the mouse button press variable
            mousebut = pygame.mouse.get_pressed()
            #If statement for the "Play mode"
            if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 289 and mouseloc[1] < 346 and mousebut[0] == 1:
                #Normal pattern
                screen.fill((255, 255, 255))
                modemenu = pygame.image.load("Sketchitmode.gif").convert()
                screen.blit(modemenu, (0,0))
                pygame.display.update()
                events=pygame.event.get()
                #Launches the play function
                play()
            #If statement for the "Free mode"
            if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 355 and mouseloc[1] < 412 and mousebut[0] == 1:
                screen.fill((255, 255, 255))
                bg3 = pygame.image.load("bg3.gif").convert()
                screen.blit(bg, (0,0))
                pygame.display.update()
                freemode()
            #If statement for quitting button
            if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 424 and mouseloc[1] < 480 and mousebut[0] == 1:
                quit()
            if ev.type == QUIT:
                keepGoing=False   # Stop the program, it's detected quit...
#Launches the mainmenu
mainmenu()

pygame.quit()  # Keep this IDLE friendly 



        
        
