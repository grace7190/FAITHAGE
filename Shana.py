import pygame
from SpriteSheet import *
from HealthBar import *
from Character import Character


# Character Class gawt damn
class Shana(Character):
    def __init__(self, x):
        idle = SpriteSheet("art/pl_shana.png").images_at(
                [(0,0,300,400)],colourkey=(0,255,0))
        walk = SpriteSheet("art/pl_shana_walk.png").images_at(
                [(0,0,300,400),
                (300,0,300,400),
                (600,0,300,400),
                (900,0,300,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/pl_shana_attack1.png").images_at(
                [(0,0,400,400),
                (400,0,400,400),
                (800,0,400,400),
                (1200,0,400,400),
                (1600,0,400,400),
                (2000,0,400,400)],colourkey=(0,255,0))
        Character.__init__(self, x, idle, walk, attack)
        self.attacking = False
        self.attack_time = 0
        self.time_till_attack = 60
        self.damage = 80

    def do_skill(self):
        return None

    def update(self):
        Character.update(self)
        if self.attacking:
            self.attack_time += 1