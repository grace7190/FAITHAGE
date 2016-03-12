import pygame
from SpriteSheet import *
from HealthBar import *
from Enemy import Enemy


# Melee enemy class Class
class Melee_Enemy(Enemy):
    def __init__(self, x):
        idle = SpriteSheet("art/en_melee_minion_atk.png").images_at(
            [(0,0,400,300)],colourkey=(0,255,0))
        attack = SpriteSheet("art/en_melee_minion_atk.png").images_at(
            [(0,0,400,300),
             (400,0,400,300),
             (800,0,400,300),
             (1200,0,400,300)],colourkey=(0,255,0))
        Enemy.__init__(self, x, idle, idle, attack)
        self.can_move = True

    def check_can_move(self, limit, unit_list):
        if self.hitbox.colliderect(limit):
            self.can_move = False
            if self.current_anim != self.attack_anim:
                self.current_anim = self.attack_anim
                self.sprite_id = 0
            return
        hitbox_list = []
        for i in unit_list:
            hitbox_list.append(i.hitbox)
        hitbox_list.remove(self.hitbox)
        if self.hitbox.collidelist(hitbox_list) == -1:
            if self.current_anim != self.walk_anim:
                self.current_anim = self.walk_anim
                self.sprite_id = 0
            self.can_move = True
        else:
            self.can_move = False
            if self.current_anim != self.attack_anim:
                self.current_anim = self.attack_anim
                self.sprite_id = 0

    def die(self):
        self.kill()
        self.healthbar.kill()

    def update(self):
        Enemy.update(self)

        if self.can_move:
            if self.current_anim != self.walk_anim:
                self.current_anim = self.walk_anim
                self.sprite_id = 0
            self.hitbox.move_ip(-3,0)
