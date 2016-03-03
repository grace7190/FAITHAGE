import pygame
from SpriteSheet import *
from HealthBar import *


# Character Class gawt damn
class Character(pygame.sprite.Sprite):
    def __init__(self, name, centerx, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.sprites = SpriteSheet("art/pl_"+name+".png").images_at(
            [(0,0,400,400)],colourkey=(0,255,0))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = centerx
        self.rect.y = y - (400-350)
        self.health = 100
        self.total_health = 100
        self.healthbar = HealthBar(self, (20, 131, 7))

    def update(self):
        if self.health < 0:
            self.health = 0
        self.healthbar.update()