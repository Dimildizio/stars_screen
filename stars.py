"""This code makes me remember old Windows screensaver of flying into space.
	Controls:
			Button 'w': speed up animation
			Button 's': slow down
			ESC: exit"""

import pygame as pg 
from random import randint, random
import sys
import math


W,H = 1600, 800						#sets screen size
FPS = 30							#sets FPS			
CENTER = W//2, H//2 				#center of the screen
WHITE = 255,255,255					
SPREAD = 200
STARS_NUMBER = 200					#number of stars
VELOCITY = 0.025					#sets stars velocity
SIZE_INCREASE = 0.0075				#sets the change of size at each step


pg.init()
SCREEN = pg.display.set_mode((W,H),pg.HWSURFACE|pg.DOUBLEBUF|pg.RESIZABLE|pg.FULLSCREEN)
pg.display.set_caption('Stars')
CLOCK = pg.time.Clock()


#class for a star
class Star:
	def __init__(self):									#sets random start position, direction and speed
		self.x = randint(0,W)
		self.y = randint(0,H)
		self.ox = self.x+randint(-SPREAD,SPREAD)
		self.oy = self.y+randint(-SPREAD,SPREAD)
		self.speed = random()

	def circle(self):									#draws a start at its pos
		pos = int(self.x),int(self.y)
		distance = ((self.x-self.ox)**2 + (self.y-self.oy)**2)**0.5
		pg.draw.circle(SCREEN, (WHITE), pos, int(distance*SIZE_INCREASE))		

	def update(self):									#changes star speed and direction
		cx,cy = CENTER
		radian = math.atan2(self.y-cy, self.x-cx)
		self.speed += VELOCITY
		dx = math.cos(radian) *(self.speed*10)
		dy = math.sin(radian) *(self.speed*10)
		self.x, self.y =self.x+dx, self.y+dy
		if not (0< self.x < W) or not (0 < self.y < H):
			self.ox = self.x = W//2+randint(-SPREAD,SPREAD)
			self.oy = self.y = H//2+randint(-SPREAD,SPREAD)
			self.speed = random()


def quit():												#exit program
	pg.quit()
	sys.exit()

def mainloop():											#mainloop 
	while True:
		CLOCK.tick(FPS)									#fps
		for event in pg.event.get():					#controls
			if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
				quit()
		global VELOCITY
		key = pg.key.get_pressed()						#changes speed
		if key[pg.K_w]:
			VELOCITY += 0.005
		if key[pg.K_s]:
			VELOCITY -= 0.01
		VELOCITY = min(0.75, max(0.0001,VELOCITY))
		SCREEN.fill((0,0,0))
		for star in stars:
			star.update()
			star.circle()
		pg.display.update()
		#alternative controls on a key pressed not held							
		'''if event.type == pg.KEYDOWN: 
			
			if event.key == pg.K_w:
				VELOCITY += 0.01
			elif event.key == pg.K_s:
				print('hi')
				VELOCITY -= 0.1
				if VELOCITY <= 0: VELOCITY = 0.001'''


stars = [Star() for x in range(STARS_NUMBER)]
mainloop()