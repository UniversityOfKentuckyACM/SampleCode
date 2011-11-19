import random

import Actor
import util

from Vector2 import Vector2
from config import *

class Enemy(Actor.Actor):
	''' 
		Enemy subs that cross the screen from left to right.
	'''
	# cache image in this static member
	loadedImage = 0

	def __init__(self):
		super(Enemy,self).__init__()

		# Load image if not already loaded
		if Enemy.loadedImage == 0:
			Enemy.loadedImage, tmp = util.loadImage(SUB_IMAGE, -1)

		# Assign image
		self.setImage(Enemy.loadedImage)

		# Random y coordinate. Ensure that it remains on screen and is reachable
		# by torpedos.
		y = random.randint(50, HEIGHT-10)

		self.setPos(-10,y)
		self.setVel(Vector2(SUB_VEL))
	
	def update(self):
		super(Enemy,self).update()

		# kill if out of bounds
		if self.rect.left > WIDTH:
			self.kill()


