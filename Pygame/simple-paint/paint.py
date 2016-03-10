#!/usr/bin/env python
# -*- coding: UTF-8 -*-
# Created by Kris Occhipinti (A.K.A. Metalx1000)
# http://filmsbykris.com/
# Oct. 3, 2010
# Copyright 2010 Kris Occhipinti
# This program is distributed under the terms of the GNU GPL

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

#    Modified by Andreas Collsén Oct, 17 2010

import sys, pygame, glob
from pygame.locals import *
from eegg import *

selected_brush = 0
brushes = []
data = []
history = []
egg = False

pygame.init()

screen = pygame.display.set_mode((1000,600))
pygame.display.set_caption("SimplePaint v1.01")

class Brush(object):
    def __init__(self, file):
        self.image = pygame.image.load("./brushes/" + file)

#Put the paint on the painting function
def paint():
    data.append((selected_brush, mx - brushes[selected_brush].image.get_width() / 2, my - brushes[selected_brush].image.get_height() / 2))
    history.append((selected_brush, mx - brushes[selected_brush].image.get_width() / 2, my - brushes[selected_brush].image.get_height() / 2))

#Load the brushes
for x in glob.glob1("./brushes","*.png"):
    brushes.append(Brush(x))
print "Loaded " + str(len(brushes)) + " brushes"

painting = False
erasing = False
#Main loop
while True:
    #Get mouse pos
    mx, my = pygame.mouse.get_pos()

    #Get events
    for e in pygame.event.get():
        if e.type == QUIT:
            sys.exit()
        if e.type == MOUSEBUTTONDOWN:
            history = []
            painting = True
            if e.button == 3:
                print data
            if e.button == 4:
                if selected_brush < len(brushes) - 1:
                    selected_brush += 1
            if e.button == 5:
                if selected_brush > 0:
                    selected_brush -= 1
        if e.type == KEYDOWN and e.key == K_DOWN:
            if selected_brush > 0:
                selected_brush -= 1
        if e.type == KEYDOWN and e.key == K_UP:
            if selected_brush < len(brushes) - 1:
                selected_brush += 1
        if e.type == MOUSEBUTTONUP:
            painting = False
        if e.type == KEYDOWN and e.key == K_BACKSPACE:
            erasing = True
        if e.type == KEYUP and e.key == K_BACKSPACE:
            erasing = False
        keys = pygame.key.get_pressed()
        if keys[K_LCTRL]:
            if keys[K_z]:
                for x in history:
                    data.pop()
                history = []
            if keys[K_n]:
                data = []
                history = []
            if keys[K_e]:
                data = []
                count = 0
                egg = True

    if egg:
        if len(data) < len(eegg):
            data.append(eegg[count])
            count += 1
        else:
            egg = False

    #Is the user painting or undoing?
    if painting: 
        paint()
    elif erasing:
        if len(data) > 0:
            data.pop()

    #Fille with white
    screen.fill((255, 255, 255))
    
    #Loop through the data array wich holds what the user have painted
    for x in data:
        screen.blit(brushes[x[0]].image, (x[1], x[2]))
    
    #Show what brush you selected
    screen.blit(brushes[selected_brush].image, (mx - brushes[selected_brush].image.get_width() / 2, my - brushes[selected_brush].image.get_height() / 2))
    
    pygame.display.flip()

