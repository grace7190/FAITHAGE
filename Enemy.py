import pygame
from SpriteSheet import *
from HealthBar import *

FLOOR = 780
HITBOX = (80,230)
HITBOX_OFFSET = 50


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
        self.healthbar = HealthBar(self, (153, 51, 102))
        self.hitbox = pygame.Rect(
            (x, FLOOR - self.image.get_height() + 20 + HITBOX_OFFSET),
            HITBOX)
        self.can_move = True
        self.attacking = False
        self.stun = 0

    def change_anim(self, anim):
        if anim != self.current_anim:
            self.current_anim = anim
            self.sprite_id = 0
            self.image = self.current_anim[(self.sprite_id)//12]
            self.rect = self.image.get_rect()

    def check_can_move(self, limit, unit_list):
        if self.hitbox.colliderect(limit):
            self.can_move = False
        else:
            hitbox_list = []
            for i in unit_list:
                if type(i)==type(self):
                    hitbox_list.append(i.hitbox)
            hitbox_list.remove(self.hitbox)
            collisions = self.hitbox.collidelistall(hitbox_list)
            if not collisions:
                self.can_move = True
            else:
                for hitbox_idx in collisions:
                    if hitbox_list[hitbox_idx].x < self.hitbox.x:
                        self.can_move = False
                        break
                    self.can_move = True

        if self.can_move:
            self.change_anim(self.walk_anim)
        else:
            self.change_anim(self.attack_anim)

    def check_can_move_ranged(self, limit, unit_list):
        if self.has_frontline:
            if self.hitbox.colliderect(limit):
                self.can_move = False
                self.change_anim(self.attack_anim)
                return
            hitbox_list = []
            for i in unit_list:
                hitbox_list.append(i.hitbox)
            hitbox_list.remove(self.hitbox)
            if self.hitbox.collidelist(hitbox_list) == -1:
                self.change_anim(self.walk_anim)
                self.can_move = True
            else:
                self.can_move = False
                self.change_anim(self.attack_anim)
        else:
            self.can_move = False
            self.change_anim(self.attack_anim)

    def update(self):
        if self.stun > 0:
            self.stun -= 1
            self.can_move = False
            self.change_anim(self.idle_anim)
        self.rect.centerx = self.hitbox.centerx
        self.rect.y = self.hitbox.y - HITBOX_OFFSET
        self.healthbar.update()
        self.sprite_id += 1
        if self.sprite_id >= len(self.current_anim)*12:
            self.sprite_id = 0
        self.image = self.current_anim[(self.sprite_id)//12]
        self.attacking = not (self.can_move or self.stun > 0 or self.hitbox.x > 900)


