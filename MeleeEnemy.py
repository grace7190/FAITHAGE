import pygame
from SpriteSheet import *
from HealthBar import *
from Enemy import Enemy


# Melee enemy class Class
class MeleeEnemy(Enemy):
    def __init__(self, x):
        idle = SpriteSheet("art/en_melee_minion_atk.png").images_at(
            [(0,0,400,300)],colourkey=(0,255,0))
        attack = SpriteSheet("art/en_melee_minion_atk.png").images_at(
            [(0,0,400,300),
             (400,0,400,300),
             (800,0,400,300),
             (1200,0,400,300)],colourkey=(0,255,0))
        Enemy.__init__(self, x, idle, idle, attack)
        self.damage = 3
        self.attack_time = 0
        self.time_till_attack = 60
        self.health = 100
        self.total_health = 100

    def check_can_move(self, limit, unit_list):
        if self.hitbox.colliderect(limit):
            self.can_move = False
            self.change_anim(self.attack_anim)
            return
        hitbox_list = []
        for i in unit_list:
            if type(i)==type(self):
                hitbox_list.append(i.hitbox)
        hitbox_list.remove(self.hitbox)
        if self.hitbox.collidelist(hitbox_list) == -1:
            self.change_anim(self.walk_anim)
            self.can_move = True
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

        if self.can_move:
            if self.current_anim != self.walk_anim:
                self.current_anim = self.walk_anim
                self.sprite_id = 0
            self.hitbox.move_ip(-3,0)

        if self.attacking:
            self.attack_time += 1


class Zombi(Enemy):
    def __init__(self, x):
        idle = SpriteSheet("art/en_zombie.png").images_at(
            [(0,0,300,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/en_zombie_atk.png").images_at(
            [(0,0,300,400),
             (300,0,300,400)],colourkey=(0,255,0))
        walk = SpriteSheet("art/en_zombie_walk.png").images_at(
            [(0,0,300,400),
             (300,0,300,400),
             (600,0,300,400)],colourkey=(0,255,0))
        Enemy.__init__(self, x, idle, walk, attack)
        self.damage = 3
        self.attack_time = 0
        self.time_till_attack = 60
        self.health = 100
        self.total_health = 100

    def check_can_move(self, limit, unit_list):
        if self.hitbox.colliderect(limit):
            self.can_move = False
            self.change_anim(self.attack_anim)
            print(1)
            return
        hitbox_list = []
        for i in unit_list:
            if type(i)==type(self):
                hitbox_list.append(i.hitbox)
        hitbox_list.remove(self.hitbox)
        if self.hitbox.collidelist(hitbox_list) == -1:
            self.change_anim(self.walk_anim)
            self.can_move = True
            print(2)
        else:
            print(3)
            self.can_move = False
            self.change_anim(self.attack_anim)

    def die(self):
        self.kill()
        self.healthbar.kill()

    def update(self):
        if self.health < 0:
            self.health = 0

        Enemy.update(self)

        if self.can_move:
            if self.current_anim != self.walk_anim:
                self.current_anim = self.walk_anim
                self.sprite_id = 0
            self.hitbox.move_ip(-4,0)

        if self.attacking:
            self.attack_time += 1