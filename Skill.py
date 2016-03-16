import pygame
from SpriteSheet import *


# A Skill Icon which travels the bottom of the screen and
# must be pressed to activate. Subclass of Sprite.
class SkillIcon(pygame.sprite.Sprite):
    def __init__(self, skill_name, y):
        pygame.sprite.Sprite.__init__(self)
        self.skill_name = skill_name
        self.triggered = False

        # Determine which skill was summoned
        if self.skill_name == "AIRSTRIKE":
            self.image = pygame.image.load("art/ic_airstrike.png").convert()
            self.skill_sprites = SpriteSheet("art/fx_airstrike.png").images_at(
                [(0,0,200,200),
                (200,0,200,200),
                (400,0,200,200),
                (600,0,200,200),
                (800,0,200,200)],colourkey=(0,255,0))
            self.skill_class = Airstrike
        elif self.skill_name == "DAZZLE":
            self.image = pygame.image.load("art/ic_dazzle.png").convert()
            self.skill_sprites = SpriteSheet("art/fx_dazzle.png").images_at(
                [(0,0,200,200),
                (200,0,200,200),
                (400,0,200,200),
                (600,0,200,200)],colourkey=(0,255,0))
            self.skill_class = Dazzle
            #self.skill = skill_function
        # elif self.skill_name == "SOME_OTHER_SKILL":
        #     self.image = pygame.image.load("SOME_SKILL.png").convert()
        #     #self.skill = skill_function

        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = y

    def update(self):
        if not self.triggered:
            self.rect.move_ip(5,0)
        else:
            self.image.set_alpha(self.image.get_alpha() - 10)
        # Destroy when past screen
        if self.rect.x > 1650:
            self.kill()

    # Check if skill has been clicked. Trigger if true.
    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            self.triggered = True
            return True
        else:
            return False

    # Return a skill object for activated skill icon.
    def activate_skill(self):
        return self.skill_class(self.skill_sprites, self.rect.centerx)


# The activated skill to appear above pressed skill icon. Subclass of Sprite.
class Airstrike(pygame.sprite.Sprite):
    def __init__(self, skill_sprites, x):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_array = skill_sprites
        self.sprite_id = 0
        self.image = skill_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = -200

    def update(self):
        if self.rect.y < 575:
            self.rect.move_ip(0, 15)
        else:
            self.sprite_id += 1
            if self.sprite_id >= len(self.sprites_array)*6:
                self.kill()
            else:
                self.image = self.sprites_array[(self.sprite_id)//6]

class Dazzle(pygame.sprite.Sprite):
    def __init__(self, skill_sprites, x):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_array = skill_sprites
        self.sprite_id = 0
        self.image = skill_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = 550

    def update(self):
        self.sprite_id += 1
        if self.sprite_id >= len(self.sprites_array)*6:
            self.kill()
        else:
            self.image = self.sprites_array[(self.sprite_id)//6]
