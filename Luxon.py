import pygame
from SpriteSheet import *
from HealthBar import *
from Character import Character


# Character Class gawt damn
class Luxon(Character):
    def __init__(self, x):
        idle = SpriteSheet("art/pl_temp.png").images_at(
                [(0,0,400,400)],colourkey=(0,255,0))
        walk = SpriteSheet("art/pl_luxon_walk.png").images_at(
                [(0,0,300,400),
                (300,0,300,400),
                (600,0,300,400),
                (900,0,300,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/pl_luxon_attack1.png").images_at(
                [(0,0,250,400),
                (250,0,250,400),
                (500,0,250,400),
                (750,0,250,400),
                (1000,0,250,400),
                (1250,0,250,400)],colourkey=(0,255,0))
        Character.__init__(self, x, idle, walk, attack)

    def update(self):
        Character.update(self)