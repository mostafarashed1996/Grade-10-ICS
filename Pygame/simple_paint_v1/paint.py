#!/usr/bin/env python
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

import sys, pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((1000,600))

screen.fill((255,255,255))

brush = pygame.image.load("brush.gif")

pygame.display.update()
clock = pygame.time.Clock()

z = 0

while 1:
	clock.tick(60)
	x,y = pygame.mouse.get_pos()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN:
			z = 1
		elif event.type == MOUSEBUTTONUP:
			z = 0

		if z == 1:
			screen.blit(brush,(x-64,y-64))
			pygame.display.update()
