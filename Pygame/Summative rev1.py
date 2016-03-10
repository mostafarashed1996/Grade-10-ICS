import pygame, sys, os, time
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
pygame.display.set_caption('Pygam Main') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)

#The screen is the Drawing window
screen.fill(THECOLORS['white'])
mainmenu = pygame.image.load("Sketchit.gif").convert()
screen.blit(mainmenu, (0,0))
event = pygame.event.get()
def play():
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
    brush = pygame.image.load("brush.png")
    while keepGoing:
        clock.tick(60)
        mouseloc = pygame.mouse.get_pos()
        events=pygame.event.get()
        for ev in events:
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
                brush = pygame.image.load("brush.png")
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
            if mouseloc[0] >= 80 and mouseloc[0] <= 140 and mouseloc[1] >= 457 and mouseloc[1] <= 479 and mousebut[0] == 1:
                screen.fill((255, 255, 255))
                bg = pygame.image.load("bg.gif").convert()
                screen.blit(bg, (0,0))
                pygame.display.update()
            elif ev.type == MOUSEBUTTONUP:
                painting = False
            if ev.type == KEYDOWN and ev.key == K_BACKSPACE:
                erasing = True
            if ev.type == KEYUP and ev.key == K_BACKSPACE:
                erasing = False
            elif ev.type == QUIT:
                keepGoing=False   # Stop the program, it's detected quit...
        if painting == True:
            screen.blit(brush,(mouseloc[0]-64,mouseloc[1]-64))
            pygame.display.update()
        elif erasing == True:
            screen.blit(copy,(0,0))
            pygame.display.update()

pygame.display.flip()

# Event Handling #
def mainmenu():
    keepGoing=True
    while keepGoing:
        events=pygame.event.get()
        for ev in events:
            mouseloc = pygame.mouse.get_pos()
            mousebut = pygame.mouse.get_pressed()
            print mouseloc, mousebut
            if mouseloc[0] > 382 and mouseloc[0] < 568 and mouseloc[1] > 289 and mouseloc[1] < 346 and mousebut[0] == 1:
                screen.fill((255, 255, 255))
                bg = pygame.image.load("bg.gif").convert()
                screen.blit(bg, (0,0))
                pygame.display.update()
                play()
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
            bg = pygame.image.load("bg.gif").convert()
            screen.blit(bg, (0,0))
            pygame.display.update()
            play()
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...

pygame.quit()  # Keep this IDLE friendly 



        
        
