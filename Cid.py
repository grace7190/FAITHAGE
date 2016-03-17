import pygame
from SpriteSheet import *
from HealthBar import *
from Character import Character


# Character Class gawt damn
class Cid(Character):
    def __init__(self, x):
        idle = SpriteSheet("art/pl_cid.png").images_at(
                [(0,0,300,400)],colourkey=(0,255,0))
        walk = SpriteSheet("art/pl_cid_walk.png").images_at(
                [(0,0,300,400),
                (300,0,300,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/pl_cid_attack1.png").images_at(
                [(0,0,250,400),
                (250,0,250,400),
                (500,0,250,400),
                (750,0,250,400)],colourkey=(0,255,0))
        Character.__init__(self, x, idle, walk, attack)
        self.attack_time = -1

    def do_skill(self):
        if self.current_anim != self.walk_anim:
            self.attack_time = len(self.attack_anim)*12 - 1

    def update(self):
        Character.update(self)

        if self.attack_time > 0:
            self.image = self.attack_anim[self.attack_time//12]
            self.rect.x += 23
            self.attack_time -= 1