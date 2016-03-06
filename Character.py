import pygame
from SpriteSheet import *
from HealthBar import *

FLOOR = 700
HITBOX = (150, 350)


# Character Class gawt damn
class Character(pygame.sprite.Sprite):
    def __init__(self, x, idle_anim, walk_anim, attack_anim):
        pygame.sprite.Sprite.__init__(self)
        self.idle_anim = idle_anim
        self.walk_anim = walk_anim
        self.attack_anim = attack_anim
        self.image = self.idle_anim[0]
        self.rect = pygame.Rect((x, FLOOR - self.rect.height + 20 + 20), HITBOX)
        self.health = 100
        self.total_health = 100
        self.healthbar = HealthBar(self, (20, 131, 7))

    def update(self):
        if self.health < 0:
            self.health = 0
        self.healthbar.update()