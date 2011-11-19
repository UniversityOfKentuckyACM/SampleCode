
# Graphics class
# Contains screen, sprite groups, etc
import pygame
import pygame.gfxdraw
import util

from Actor import Actor
from Vector2 import Vector2
from config import *
from pygame.locals import *
import random
		
	
class Graphics():
	def __init__(self, game_obj):
		self.main = game_obj
		
		if IS_FULLSCREEN:
			self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN|DOUBLEBUF)
		else:
			self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
		
		pygame.display.set_caption(GAME_TITLE)
	
		self.bgGroup = pygame.sprite.OrderedUpdates()
		self.playerGroup = pygame.sprite.RenderPlain()
		self.torpedoGroup = pygame.sprite.RenderPlain()

		# Load image of torpedo, also returns rect but we ignore this
		self.torpImage, tmp = util.loadImage(TORPEDO_IMAGE)

	def loadBackground(self, imagefile):
		# Create background object
		self.bg = Actor(imagefile)
		self.bgGroup.add(self.bg)
	
	def loadPlayer(self, imagefile):
		self.player = Actor(imagefile, -1)
		self.playerGroup.add(self.player)
		return self.player
	
	def addTorpedo(self, pos):
		torp = Actor()
		# assign torpedo image
		torp.setImage(self.torpImage)
		# assign it a coordinate and velocity
		torp.setPos(pos[0], pos[1])
		torp.setVel(Vector2(0,3))
		# add it to render group
		self.torpedoGroup.add(torp)

	def update(self):
		self.bgGroup.update()
		self.playerGroup.update()
		self.torpedoGroup.update()

	def drawScreen(self):
		# draw background
		self.bgGroup.draw(self.screen)
		# draw player	
		self.playerGroup.draw(self.screen)
		# draw torpedos
		self.torpedoGroup.draw(self.screen)

		pygame.display.flip()

