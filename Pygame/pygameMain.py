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
window = pygame.display.set_mode((468, 480)) 
pygame.display.set_caption('Pygam Main') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)

#The screen is the Drawing window
screen.fill(THECOLORS['white'])



pygame.display.flip()

# Event Handling #
keepGoing=True

while keepGoing:

    events=pygame.event.get()

    for ev in events:

        
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...


pygame.quit()  # Keep this IDLE friendly 



        
        
