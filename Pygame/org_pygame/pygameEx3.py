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
image = pygame.image.load('beachBall.gif').convert()

# Event Handling #
keepGoing=True
#Create variables for the direction of the ball, and set values
dirx=1
x=100
y=100
diry=1
#Create loop such that the ball chances direction and bounces off walls
while keepGoing:
    x += 4*dirx
    y += 4*diry
    screen.blit(image,(x,y))
#Flip the image onto screen
    pygame.display.flip()
#Create speed for the ball
    pygame.time.delay(50)
#Draw rectangle to cover up the ball
    pygame.draw.rect(screen,(255,255,255),(x,y,100,100))
#Create if statements that will change the direction of the ball, by reversing the value of dirx and diry
    if x>=378 or x<0:
        dirx=dirx*(-1)
    if y>=378 or y<0:
        diry=diry*(-1)
    
    events=pygame.event.get()
#Create events that allow for keyboard control
    for ev in events:
        if ev.type == KEYDOWN:
#Create value that detects the pressing of keys
            keypressed = pygame.key.name(ev.key)
#Create seperate if statements that affect the value of diry and dirx, such that the ball moves in the direction accordingly to the keyboard key pressed
            if keypressed == "up":
                diry = -1
            if keypressed == "down":
                diry = 1
            if keypressed == "right":
                dirx = 1
            if keypressed == "left":
                dirx = -1
                
                
        
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...


pygame.quit()  # Keep this IDLE friendly 



        
        
