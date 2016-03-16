import pygame
from SpriteSheet import *
from HealthBar import *
from Enemy import Enemy


# Ranged enemy class Class
class RangedEnemy(Enemy):
    def __init__(self, x):
        idle = SpriteSheet("art/en_ranged_minion_atk.png").images_at(
            [(0,0,400,300)],colourkey=(0,255,0))
        attack = SpriteSheet("art/en_ranged_minion_atk.png").images_at(
            [(0,0,400,300),
             (400,0,400,300),
             (800,0,400,300),
             (1200,0,400,300)],colourkey=(0,255,0))
        Enemy.__init__(self, x, idle, idle, attack)
        self.damage = 5
        self.attack_time = 0
        self.time_till_attack = 100
        self.health = 85
        self.total_health = 85
        self.has_frontline = True

    def check_can_move(self, limit, unit_list):
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

    def die(self):
        self.kill()
        self.healthbar.kill()

    def update(self):
        if self.health < 0:
            self.health = 0

        Enemy.update(self)

        if self.has_frontline:
            if self.can_move:
                if self.current_anim != self.walk_anim:
                    self.current_anim = self.walk_anim
                    self.sprite_id = 0
                self.hitbox.move_ip(-3,0)

        if self.attacking:
            self.attack_time += 1