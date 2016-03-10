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
window = pygame.display.set_mode((640, 480)) 
pygame.display.set_caption('Exercise 1') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)

#The screen is the Drawing window
screen.fill(THECOLORS['white'])
pygame.draw.circle(screen,(217,27,53),(110,160),70)
pygame.draw.circle(screen,(255,255,255),(110,160),45)
pygame.draw.circle(screen,(217,27,53),(110,160),24)
#Load the target image
targetImage=pygame.image.load('targetLogo.jpg').convert()
#Assign x and y cordinates to the image
screen.blit(targetImage,(350,25))
#Assign the font for target logo
targetFont=pygame.font.SysFont("Franklin Gothic Demi",38)
#Assign the xy and y cordinates for the logo, as well as colour
textTarget=targetFont.render("TARGET",True,(217,27,53))
screen.blit(textTarget,(50,240))

pygame.display.flip()

# Event Handling #
keepGoing=True

while keepGoing:

    events=pygame.event.get()

    for ev in events:

        
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...


pygame.quit()  # Keep this IDLE friendly 



        
        
