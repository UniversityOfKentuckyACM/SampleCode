
# Graphics class
# Contains screen, sprite groups, etc
import pygame
import pygame.gfxdraw
import util

from Actor import Actor
from Torpedo import Torpedo
from Enemy import Enemy
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
		self.subGroup = pygame.sprite.RenderPlain()

	def loadBackground(self, imagefile):
		# Create background object
		self.bg = Actor(imagefile)
		self.bgGroup.add(self.bg)
	
	def loadPlayer(self, imagefile):
		self.player = Actor(imagefile, -1)
		self.playerGroup.add(self.player)
		return self.player
	
	def addTorpedo(self, pos):
		# create a new torpedo and give it a position
		torp = Torpedo(pos[0], pos[1])

		# add it to render group
		self.torpedoGroup.add(torp)
	
	def addSub(self):
		# Create new sub
		sub = Enemy()
		self.subGroup.add(sub)

	def update(self):
		self.bgGroup.update()
		self.playerGroup.update()
		self.torpedoGroup.update()
		self.subGroup.update()

	def drawScreen(self):
		# draw background
		self.bgGroup.draw(self.screen)
		# draw player	
		self.playerGroup.draw(self.screen)
		# draw torpedos
		self.torpedoGroup.draw(self.screen)
		# draw enemies
		self.subGroup.draw(self.screen)

		pygame.display.flip()

