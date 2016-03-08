import pygame
from SpriteSheet import *
from HealthBar import *
from Character import Character


# Character Class gawt damn
class Shana(Character):
    def __init__(self, x):
        idle = SpriteSheet("art/pl_shana.png").images_at(
                [(0,0,400,400)],colourkey=(0,255,0))
        Character.__init__(self, x, idle, idle, idle)

    def update(self):
        Character.update(self)