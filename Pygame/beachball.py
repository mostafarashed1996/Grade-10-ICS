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
pygame.display.set_caption('Beachball!') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)

#The screen is the Drawing window
screen.fill(THECOLORS['white'])
beachball = pygame.image.load('beachBall.png').convert()
keepgoing = True
dirx = 1
diry = 1
x = 100
y = 100
while keepgoing == True:
    x += 4*dirx
    y += 4*diry
    screen.blit(beachball, (x,y))
    pygame.display.flip()
    pygame.time.delay(50)
    pygame.draw.rect(screen, (255,255,255),(x,100,100,100))
    if x>=378 or x<0:
        dirx = dirx * (-1)
    if y>= or x<0:
        diry = diry * (-1)


# Event Handling #
keepGoing=True

while keepGoing:

    events=pygame.event.get()

    for ev in events:

        
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...


pygame.quit()  # Keep this IDLE friendly 



        
        
