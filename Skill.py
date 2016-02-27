import pygame

class Skill(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("art/ic_temp.png").convert()
        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 910
        self.triggered = False

    def update(self):
        if not self.triggered:
            self.rect.x += 5
        else:
            self.image.set_alpha(self.image.get_alpha() - 10)
