import pygame
from SpriteSheet import *
from HealthBar import *

FLOOR = 780
HITBOX = (80,230)
HITBOX_OFFSET = 150


# Enemy Class gawt damn
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, idle_anim, walk_anim, attack_anim):
        pygame.sprite.Sprite.__init__(self)
        self.idle_anim = idle_anim
        self.walk_anim = walk_anim
        self.attack_anim = attack_anim
        self.current_anim = walk_anim
        self.sprite_id = 0
        self.image = self.current_anim[self.sprite_id]
        self.rect = self.image.get_rect()
        self.health = 100
        self.total_health = 100
        self.healthbar = HealthBar(self, (153, 51, 102))
        self.hitbox = pygame.Rect(
            (x, FLOOR - self.image.get_height() + 20 + HITBOX_OFFSET),
            HITBOX)

    def update(self):
        self.rect.centerx = self.hitbox.centerx
        self.rect.y = self.hitbox.y - HITBOX_OFFSET
        self.healthbar.update()
        self.sprite_id += 1
        if self.sprite_id >= len(self.current_anim)*10:
            self.sprite_id = 0
        self.image = self.current_anim[(self.sprite_id)//10]