import pygame
from SpriteSheet import *
from HealthBar import *
import Character


# Character Class gawt damn
class Cid(Character.Character):
    def __init__(self):
        x = 50
        anim_idle = self.skill_sprites = SpriteSheet("art/pl_cid.png").images_at(
                [(0,0,400,400)],colourkey=(0,255,0))
        anim_walk = self.skill_sprites = SpriteSheet("art/pl_cid_attack1.png").images_at(
                [(0,0,250,400),
                (250,0,250,400),
                (500,0,250,400),
                (750,0,250,400)],colourkey=(0,255,0))
        Character.__init__(self, x, anim_idle, anim_walk, anim_walk)
