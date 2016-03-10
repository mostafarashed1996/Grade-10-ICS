import pygame, sys, os, time, random
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
def play():
    while True:
        events=pygame.event.get()
        for ev in events:
            mouseloc = pygame.mouse.get_pos()
            mousebut = pygame.mouse.get_pressed()
            if mouseloc[0] >= 375 and mouseloc[0] <= 560 and mouseloc[1] >= 101 and mouseloc[1] <= 157 and mousebut[0] == 1:
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
                screen.fill((255, 255, 255))
                tut = pygame.image.load("tut.gif").convert()
                screen.blit(tut, (0,0))
                pygame.display.update()
                pygame.time.wait(5000)
                brush = pygame.image.load("black2.gif")
                screen.fill((255, 255, 255))
                bg = pygame.image.load("bg.gif").convert()
                screen.blit(bg, (0,0))
                pygame.display.update()
                clock.tick(60)
                while keepGoing:
                    while newword == True:
                        drawlist = ["Tree", "Duck", "House", "Sunglasses", "Firetruck", "Sun", "Phone"]
                        drawword = drawlist[random.randint(0,6)]
                        drawfont = pygame.font.SysFont("Franklin Gothic Demi",38)
                        drawtext = drawfont.render("Draw: %s!"%drawword,True,(0,0,0))
                        screen.blit(drawtext,(400,52))
                        newword = False
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
                                bg = pygame.image.load("bg.gif").convert()
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
                        if mouseloc[0] >= 858 and mouseloc[0] <= 974 and mouseloc[1] >= 450 and mouseloc[1] <= 480:
                            if ev.type == MOUSEBUTTONDOWN:
                                screen.fill((255, 255, 255))
                                bg = pygame.image.load("bg.gif").convert()
                                screen.blit(bg, (0,0))
                                pygame.display.update()
                                newword = True
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
                        
                if mouseloc[0] >= 375 and mouseloc[0] <= 560 and mouseloc[1] >= 171 and mouseloc[1] <= 227 and mousebut[0] == 1:
                    painting = False
                    erasing = False
                    keepGoing = True
                    guessword = True
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
                    screen.fill((255, 255, 255))
                    tut = pygame.image.load("tut2.gif").convert()
                    screen.blit(tut, (0,0))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    headingFont=pygame.font.SysFont("Arial Black",20)
                    myfont = pygame.font.SysFont("Times New Roman", 25)
                    textValue=""
                    screen.fill((255, 255, 255))
                    tut = pygame.image.load("tut.gif").convert()
                    screen.blit(tut, (0,0))
                    pygame.display.update()
                    pygame.time.wait(5000)
                    brush = pygame.image.load("black2.gif")
                    screen.fill((255, 255, 255))
                    bg = pygame.image.load("bg.gif").convert()
                    screen.blit(bg, (0,0))
                    pygame.display.update()
                    clock.tick(60)
                    while keepGoing:
                        while guessword == True:
                            keepGoing=True
                            while keepGoing:
                                clock.tick(30)
                                events=pygame.event.get()
                                for ev in events:
                                    mouseloc = pygame.mouse.get_pos()
                                    events=pygame.event.get()
                                    print mouseloc
                                    if ev.type == QUIT:
                                        keepGoing=False
                                    elif ev.type == KEYDOWN:
                                        if ev.key == K_BACKSPACE and len(textValue) > 0:
                                            textValue = textValue[:-1] #cut off last character
                                        elif ev.unicode and len(textValue) < 40:
                                            #That condition limits the length to 50 and only alphanumeric
                                            textValue = textValue + ev.unicode #adds character value of key
                                        text = myfont.render(textValue, True, (0,0,0))
                                        screen.fill((255,255,255))
                                        screen.blit(head,(400,60))
                                        pygame.draw.rect(screen, (255,0,0), (350,100,200,40),3)
                                        screen.blit(text, (400, 105))
                            guessword = False
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
                                    bg = pygame.image.load("bg.gif").convert()
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
                            if mouseloc[0] >= 858 and mouseloc[0] <= 974 and mouseloc[1] >= 450 and mouseloc[1] <= 480:
                                if ev.type == MOUSEBUTTONDOWN:
                                    head=headingFont.render("Type in the box below:",True,(0,0,0))
                                    text=myfont.render(textValue, True, (0,0,0))
                                    screen.fill((255,255,255))
                                    screen.blit(head,(400,60))
                                    pygame.draw.rect(screen,(255,0,0),(350,100,200,40),3)
                                    screen.blit(text, (400,105))
                                    pygame.display.update()
                                    guessword = True
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
def freemode():
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
                    bg = pygame.image.load("bg.gif").convert()
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

# Event Handling #
def mainmenu():
    keepGoing=True
    while keepGoing:
        events=pygame.event.get()
        screen.fill((255, 255, 255))
        mainmenu = pygame.image.load("Sketchit.gif").convert()
        screen.blit(mainmenu, (0,0))
        pygame.display.update()
        for ev in events:
            mouseloc = pygame.mouse.get_pos()
            mousebut = pygame.mouse.get_pressed()
            print mouseloc, mousebut
            if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 289 and mouseloc[1] < 346 and mousebut[0] == 1:
                screen.fill((255, 255, 255))
                modemenu = pygame.image.load("Sketchitmode.gif").convert()
                screen.blit(modemenu, (0,0))
                pygame.display.update()
                events=pygame.event.get()
                play()
            if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 355 and mouseloc[1] < 412 and mousebut[0] == 1:
                screen.fill((255, 255, 255))
                bg = pygame.image.load("bg.gif").convert()
                screen.blit(bg, (0,0))
                pygame.display.update()
                freemode()
            if ev.type == QUIT:
                keepGoing=False   # Stop the program, it's detected quit...

keepGoing=True
while keepGoing:
    events=pygame.event.get()
    for ev in events:
        mouseloc = pygame.mouse.get_pos()
        mousebut = pygame.mouse.get_pressed()
        print mouseloc, mousebut
        if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 289 and mouseloc[1] < 346 and mousebut[0] == 1:
            screen.fill((255, 255, 255))
            modemenu = pygame.image.load("Sketchitmode.gif").convert()
            screen.blit(modemenu, (0,0))
            pygame.display.update()
            events=pygame.event.get()
            play()
        if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 355 and mouseloc[1] < 412 and mousebut[0] == 1:
            screen.fill((255, 255, 255))
            bg = pygame.image.load("bg.gif").convert()
            screen.blit(bg, (0,0))
            pygame.display.update()
            freemode()
        if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 453 and mouseloc[1] < 480 and mousebut[0] == 1:
            quit()
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...

pygame.quit()  # Keep this IDLE friendly 



        
        
