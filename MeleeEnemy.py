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
        self.health = 200
        self.total_health = 200

    def die(self):
        self.kill()
        self.healthbar.kill()

    def update(self):
        if self.health < 0:
            self.health = 0

        Enemy.update(self)

        self.attacking &= self.hitbox.x < 900

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
        self.time_till_attack = 50
        self.health = 60
        self.total_health = 60

    def die(self):
        self.kill()
        self.healthbar.kill()

    def update(self):
        if self.health < 0:
            self.health = 0

        Enemy.update(self)
        self.attacking &= self.hitbox.x < 900

        if self.can_move:
            if self.current_anim != self.walk_anim:
                self.current_anim = self.walk_anim
                self.sprite_id = 0
            self.hitbox.move_ip(-4,0)

        if self.attacking:
            self.attack_time += 1


class MeleeEnemyR(MeleeEnemy):
    def __init__(self, x):
        MeleeEnemy.__init__(self, x)
        self.idle_anim = SpriteSheet("art/en_melee_redminion_atk.png").images_at(
            [(0,0,400,300)],colourkey=(0,255,0))
        self.walk_anim = self.idle_anim
        self.attack_anim = SpriteSheet("art/en_melee_redminion_atk.png").images_at(
            [(0,0,400,300),
             (400,0,400,300),
             (800,0,400,300),
             (1200,0,400,300)],colourkey=(0,255,0))
        self.damage = 9


class MeleeEnemyG(MeleeEnemy):
    def __init__(self, x):
        MeleeEnemy.__init__(self, x)
        self.idle_anim = SpriteSheet("art/en_melee_greenminion_atk.png").images_at(
            [(0,0,400,300)],colourkey=(0,255,0))
        self.walk_anim = self.idle_anim
        self.attack_anim = SpriteSheet("art/en_melee_greenminion_atk.png").images_at(
            [(0,0,400,300),
             (400,0,400,300),
             (800,0,400,300),
             (1200,0,400,300)],colourkey=(0,255,0))
        self.health = 150
        self.total_health = 150


class Nox(MeleeEnemy):
    def __init__(self, x):
        MeleeEnemy.__init__(self, x)
        self.idle_anim = SpriteSheet("art/en_nox_necro.png").images_at(
            [(0,0,400,400)],colourkey=(0,255,0))
        self.walk_anim = self.idle_anim
        self.attack_anim = self.idle_anim
        self.damage = 0
        self.health = 50
        self.total_health = 50
        self.hitbox.y -= 100 #just cause
        self.dead = False

    def die(self):
        self.dead = True
        self.image = pygame.image.load("art/en_nox.png").convert()
        self.image.set_colorkey((0,255,0))
        self.image.set_alpha(255)

    def update(self):
        if self.dead:
            self.image.set_alpha(self.image.get_alpha() - 5)
            if self.image.get_alpha() <= 10:
                self.kill()
                self.healthbar.kill()
        else:
            MeleeEnemy.update(self)