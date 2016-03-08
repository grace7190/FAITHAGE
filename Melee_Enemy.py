import pygame
from SpriteSheet import *
from HealthBar import *
from Enemy import Enemy


# Melee enemy class Class
class Melee_Enemy(Enemy):
    def __init__(self, x):
        idle = SpriteSheet("art/en_melee_minion_atk.png").images_at(
            [(0,0,400,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/en_melee_minion_atk.png").images_at(
            [(0,0,400,400),
             (400,0,400,400),
             (800,0,400,400),
             (1200,0,400,400)],colourkey=(0,255,0))
        Enemy.__init__(self, x, idle, attack, attack)
        self.can_move = True

    def check_can_move(self, limit, unit_list):
        if self.hitbox.colliderect(limit):
            self.can_move = False
            return
        hitbox_list = []
        for i in unit_list:
            hitbox_list.append(i.hitbox)
        hitbox_list.remove(self.hitbox)
        if self.hitbox.collidelist(hitbox_list) == -1:
            self.can_move = True
        else:
            self.can_move = False

    def update(self):
        Enemy.update(self)
        self.sprite_id += 1
        if self.can_move:
            self.hitbox.move_ip(-3,0)
        if self.sprite_id >= len(self.attack_anim)*10:
            self.sprite_id = 0
        self.image = self.attack_anim[(self.sprite_id)//10]
