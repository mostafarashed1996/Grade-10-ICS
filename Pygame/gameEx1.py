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
screen.fill((255, 255, 255))

selected_brush = 0
brushes = []
data = []
history = []
painting = False
erasing = False
keepGoing=True
brush = pygame.image.load("brush.png")
copies = []

while keepGoing:
    clock.tick(60)
    x, y = pygame.mouse.get_pos()
    events=pygame.event.get()
    for ev in events:
        if ev.type == MOUSEBUTTONDOWN:
            painting = True
            copy=screen.copy()
        elif ev.type == MOUSEBUTTONUP:
            painting = False
        if ev.type == KEYDOWN and ev.key == K_BACKSPACE:
            erasing = True
        if ev.type == KEYUP and ev.key == K_BACKSPACE:
            erasing = False
        elif ev.type == QUIT:
            keepGoing=False   # Stop the program, it's detected quit...
    if painting == True:
        screen.blit(brush,(x-64,y-64))
        pygame.display.update()
    elif erasing == True:
        screen.blit(copy,(0,0))
        pygame.display.update()

pygame.quit()  # Keep this IDLE friendly 



        
        
