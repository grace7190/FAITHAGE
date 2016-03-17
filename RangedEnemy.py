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
        self.attack_time = 0
        self.time_till_attack = 100
        self.health = 85
        self.total_health = 85
        self.has_frontline = True

    def check_can_move(self, limit, unit_list):
        self.check_can_move_ranged(limit, unit_list)

    def die(self):
        self.kill()
        self.healthbar.kill()

    def launch_skill(self, target):
        return Missile(self.rect.x, target)

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


class Skelli(Enemy):
    def __init__(self, x):
        idle = SpriteSheet("art/en_skeleton.png").images_at(
            [(0,0,300,400)],colourkey=(0,255,0))
        attack = SpriteSheet("art/en_skeleton_atk.png").images_at(
            [(0,0,300,400),
             (300,0,300,400),
             (600,0,300,400),
             (900,0,300,400)],colourkey=(0,255,0))
        Enemy.__init__(self, x, idle, idle, attack)
        self.attack_time = 0
        self.time_till_attack = 48
        self.health = 75
        self.total_health = 75
        self.has_frontline = True

    def check_can_move(self, limit, unit_list):
        self.check_can_move_ranged(limit, unit_list)

    def die(self):
        self.kill()
        self.healthbar.kill()

    def launch_skill(self, target):
        return Missile(self.rect.x, target)

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


class Missile(pygame.sprite.Sprite):
    def __init__(self, start_x, target):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_array = SpriteSheet("art/fx_bone.png").images_at(
                [(0,0,200,200),
                (200,0,200,200),
                (400,0,200,200),
                (600,0,200,200),
                (800,0,200,200),
                (1000,0,200,200)],colourkey=(0,255,0))
        self.sprite_id = 0
        self.image = self.sprites_array[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = start_x
        self.rect.y = 400
        self.target = target

    def update(self):
        if self.rect.centerx <= self.target.hitbox.centerx:
            self.target.health -= 5
            self.kill()

        self.image = self.sprites_array[((self.sprite_id)//6)%len(self.sprites_array)]
        self.rect.move_ip(-15, 0)
        self.sprite_id += 1