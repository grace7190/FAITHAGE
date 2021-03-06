import pygame
from SpriteSheet import *


class Speaker(pygame.sprite.Sprite):
    def __init__(self, speaker_sprites, side):
        pygame.sprite.Sprite.__init__(self)
        # self.speaker = SpriteSheet("art/"+speaker_sprites+"_dialogue.png").images_at(
        #         [(0,0,200,200),
        #         (200,0,200,200),
        #         (400,0,200,200)],colourkey=(0,255,0))
        self.speaker = SpriteSheet("art/pl_dia_"+speaker_sprites.lower()+".png").images_at(
            [(0,0,800,800)], colourkey=(0,255,0))
        self.name = speaker_sprites
        self.emotion_id = 0
        self.image = self.speaker[self.emotion_id].convert()
        self.rect = self.image.get_rect()
        self.rect.x = 625 + 625*side
        self.rect.y = -5
        self.image.set_alpha(15)
        self.leave = False
        #LEFT = -1
        #RIGHT = 1
        self.side = side

    def update(self):
        if self.leave:
            if self.image.get_alpha() <= 10:
                self.kill()
                return
            self.image.set_alpha(self.image.get_alpha() - 15)
            self.rect.x += 3*self.side
        else:
            if self.image.get_alpha() < 245:
                self.image.set_alpha(self.image.get_alpha() + 10)
                self.rect.x += -1*self.side
                if self.side == 1:
                    tmp_alpha = self.image.get_alpha()
                    self.image = pygame.transform.flip(
                        self.speaker[self.emotion_id], True, False).convert()
                    self.image.set_alpha(tmp_alpha)
            else:
                if self.side == 1:
                    self.image = pygame.transform.flip(
                        self.speaker[self.emotion_id], True, False).convert()
                else:
                    self.image = self.speaker[self.emotion_id].convert()

                self.image.set_alpha(255)
