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
window = pygame.display.set_mode((600, 480)) 
pygame.display.set_caption('Beach Ball') 
screen = pygame.display.get_surface() 
myfont = pygame.font.SysFont("Times New Roman", 25)

#The screen is the Drawing window
screen.fill(THECOLORS['white'])
ball=pygame.image.load("beachBall.gif").convert()

daballlist = [(1,1,1,1)]
while True:
    clock.tick(30)
    screen.fill((255,255,255))
    for beachball in range(0,len(daballlist)):
        ballpos = daballlist[beachball][0],daballlist[beachball][1]
        screen.blit(ball,ballpos)
        ballloc = daballlist[beachball]
        x = ballloc[0]+ballloc[2]*8
        y = ballloc[1]+ballloc[3]*8
        x2 = ballloc[2]
        y2 = ballloc[3]
        if x<=0 or x>=510:
            x2 =-ballloc[2]
        if y<=0 or x>=390:
            y2 =-ballloc[3]
        ballloc=x,y,x2,y2
        daballlist[beachball]=ballloc

    pygame.display.flip()
    pygame.time.delay(20)
    events=pygame.event.get()

    for ev in events:
        pos=pygame.mouse.get_pos()
        but=pygame.mouse.get_pressed()
        if but[0]==1:
            x=pos[0]
            y=pos[1]
            if x > 510:
                x = 500
            if y > 390:
                y = 380
            if x <=300 and y <=240:
                x2=1
                y2=1
            elif x<=300 and y>240:
                x2=1
                y2=-1
            elif x>300 and y<=240:
                x2=-1
                y2=1
            else:
                x2=-1
                y2=-1
            beachball2 = (x,y,x2,y2)
            daballlist.append(beachball2)
        
        if ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...


pygame.quit()  # Keep this IDLE friendly 



        
        
