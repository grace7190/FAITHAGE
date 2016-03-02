import pygame
from SpriteSheet import *
from HealthBar import *


# Enemy Class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.sprites = SpriteSheet("art/en_"+name+".png").images_at(
            [(0,0,400,400),
             (400,0,400,400),
             (800,0,400,400),
             (1200,0,400,400)],colourkey=(0,255,0))
        self.image = self.sprites[0]
        self.sprite_id = 0
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.health = 100
        self.total_health = 100
        self.healthbar = HealthBar(self, (153, 51, 102))

    def update(self):
        self.health -= 1
        if self.health < 0:
            self.health = 0
        self.healthbar.update()

        self.sprite_id += 1
        if self.sprite_id >= len(self.sprites)*15:
            self.sprite_id = 0
        self.image = self.sprites[(self.sprite_id)//15]