import pygame
from SpriteSheet import *
from HealthBar import *
from Character import Character

FLOOR = 780
HITBOX = (150, 300)
HITBOX_OFFSET = 80


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

        self.hitbox = pygame.Rect((x,
                                   FLOOR - idle[0].get_height() + 20 + HITBOX_OFFSET),
                                  HITBOX)
        Character.__init__(self, self.hitbox.centerx, self.hitbox.y, idle, attack, attack)

    def update(self):
        Character.update(self)
        self.rect.centerx = self.hitbox.centerx
        self.rect.y = self.hitbox.y - HITBOX_OFFSET

