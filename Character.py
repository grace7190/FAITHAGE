import pygame
from SpriteSheet import *


# Character Class gawt damn
class Character(pygame.sprite.Sprite):
    def __init__(self, name, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.name = name
        self.sprites = SpriteSheet("art/pl_"+name+".png").images_at(
            [(0,0,400,400)],colourkey=(0,255,0))
        self.image = self.sprites[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
