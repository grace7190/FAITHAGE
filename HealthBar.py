import pygame
from SpriteSheet import *

BAR_SIZE = 120

# A Healthbar sprite
class HealthBar(pygame.sprite.Sprite):
    def __init__(self, unit, colour):
        pygame.sprite.Sprite.__init__(self)
        self.unit = unit
        self.colour = colour
        self.image = pygame.Surface((BAR_SIZE, 20))
        pygame.draw.rect(self.image, colour, (0,0,BAR_SIZE,20), 1)
        self.rect = self.image.get_rect()
        self.old_percent = 0

    def update(self):
        self.percent = self.unit.health / (self.unit.total_health * 1.0)
        if self.percent != self.old_percent:
            pygame.draw.rect(self.image,
                             (245*self.percent+1, 45*self.percent+1, 10*self.percent+1),
                             (1,1,BAR_SIZE-2,18)) # fill black
            pygame.draw.rect(self.image, self.colour,
                             (1,1,int(BAR_SIZE * self.percent),18),0) # fill green
        self.old_percent = self.percent
        self.rect.centerx = self.unit.rect.centerx
        self.rect.centery = self.unit.rect.centery - self.unit.rect.height /2 - 10