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
pygame.draw.line(screen,(0,0,0),(0,150),(486,150),2)
pygame.draw.line(screen,(0,0,0),(0,300),(486,300),2)
pygame.draw.line(screen,(0,0,0),(150,0),(150,486),2)
pygame.draw.line(screen,(0,0,0),(300,0),(300,480),2)

pygame.display.flip()
control = True
# Event Handling #
keepGoing=True

while keepGoing:
#Create track mouse position, as well as the clicking of mouse keys
    pos=pygame.mouse.get_pos()
    button=pygame.mouse.get_pressed()
#Create if statements such that when the right mouse key is clicked, and the variable control is true, create a circle
    if button[0]==1 and control == True:
        pygame.draw.circle(screen,(217,27,53),(pos[0],pos[1]),60)
        pygame.draw.circle(screen,(255,255,255),(pos[0],pos[1]),50)
        pygame.display.flip()
        control = False
#Create if statements such that when the left mouse key is clicked, and the variable is false, it draws a x
    if button[2]==1 and control == False:
        pygame.draw.line(screen,(217,27,53),(pos[0]+60,pos[1]-60),(pos[0]-60,pos[1]+60),2)
        pygame.draw.line(screen,(217,27,53),(pos[0]-60,pos[1]-60),(pos[0]+60,pos[1]+60),2)
        control = True
        pygame.display.flip()
    events=pygame.event.get()

    for ev in events:

        
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...


pygame.quit()  # Keep this IDLE friendly 



        
        
