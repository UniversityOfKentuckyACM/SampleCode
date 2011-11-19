# Configuration variables to be used by rest of game
import os
from pygame.locals import *

WIDTH = 640
HEIGHT = 480
IS_FULLSCREEN = False
FRAME_RATE = 60

GAME_TITLE = "Submarine"

DIRECTION_KEYS = [K_UP, K_DOWN, K_LEFT, K_RIGHT]

GAME_IMAGES = "images"
GAME_SOUNDS = "sounds"

BACKGROUND_IMAGE = "sea.png"

START_X = WIDTH / 2
START_Y = 20
PLAYER_SPEED = 4
PLAYER_IMAGE = "ship.png"

SUB_IMAGE = "sub.png"
TORPEDO_IMAGE = "ship_fire.png"

TORPEDO_VEL = (0,3)
SUB_VEL = (2,0)

ENEMY_SPAWN_INTERVAL = 60
