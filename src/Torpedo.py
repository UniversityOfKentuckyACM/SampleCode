
import Actor
import util

from Vector2 import Vector2
from config import *


class Torpedo(Actor.Actor):
	'''
		Torpedo class. Inherits from Actor and handles special behavior that
		torpedos have.
	'''

	# We don't want to reload the image every time we create another torpedo.
	# This image will be static among all torpedos.
	loadedImage = 0

	def __init__(self, x, y):
		# Call super constructor and assign its image to TORPEDO_IMAGE
		super(Torpedo,self).__init__()

		# Load image on first torpedo
		if Torpedo.loadedImage == 0:
			Torpedo.loadedImage,tmp = util.loadImage(TORPEDO_IMAGE)
		
		# Assign pre-loaded image
		self.setImage(Torpedo.loadedImage)

		# Set position
		self.setPos(x,y)

		# Set velocity -- always moving downwards
		self.setVel(Vector2(TORPEDO_VEL))
	
	def update(self):
		# Update just as an actor would
		super(Torpedo,self).update()

		# Also check to see if still in bounds
		if self.rect.top > HEIGHT:
			self.kill()
