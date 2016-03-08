import pygame
from SpriteSheet import *
from HealthBar import *
from Character import Character


# Character Class gawt damn
class Cid(Character):
    def __init__(self, x):
        idle = SpriteSheet("art/pl_cid.png").images_at(
                [(0,0,400,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/pl_cid_attack1.png").images_at(
                [(0,0,250,400),
                (250,0,250,400),
                (500,0,250,400),
                (750,0,250,400)],colourkey=(0,255,0))
        Character.__init__(self, x, idle, attack, attack)

    def update(self):
        Character.update(self)
