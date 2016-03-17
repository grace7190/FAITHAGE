import pygame
from SpriteSheet import *
from HealthBar import *

FLOOR = 780
HITBOX = (150, 300)
HITBOX_OFFSET = 80


# Character Class gawt damn
class Character(pygame.sprite.Sprite):
    def __init__(self, x, idle_anim, walk_anim, attack_anim):
        pygame.sprite.Sprite.__init__(self)
        self.idle_anim = idle_anim
        self.walk_anim = walk_anim
        self.attack_anim = attack_anim
        self.image = self.idle_anim[0]
        self.current_anim = self.idle_anim
        self.rect = self.image.get_rect()
        self.sprite_id = 0
        self.health = 20
        self.total_health = 100
        self.healthbar = HealthBar(self, (20, 131, 7))
        self.hitbox = pygame.Rect(
            (x, FLOOR - self.image.get_height() + 20 + HITBOX_OFFSET),
            HITBOX)
        self.dead = False

    def change_anim(self, anim):
        if anim != self.current_anim:
            self.current_anim = anim
            self.sprite_id = 0
            self.image = self.current_anim[(self.sprite_id)//12]
            self.rect = self.image.get_rect()

    def update(self):
        if self.dead:
            self.image.set_alpha(self.image.get_alpha() - 10)
            if self.image.get_alpha() <= 10:
                self.kill()
                self.healthbar.kill()
        else:
            self.sprite_id += 1
            if self.sprite_id >= len(self.current_anim)*12:
                self.sprite_id = 0
            self.image = self.current_anim[(self.sprite_id)//12]
            self.image.set_alpha(255)

            self.rect.centerx = self.hitbox.centerx
            self.rect.y = self.hitbox.y - HITBOX_OFFSET

            if self.health < 0:
                self.dead = True
                self.health = 0
            if self.health > 100:
                self.health = 100
            self.healthbar.update()