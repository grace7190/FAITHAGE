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
        elif self.skill_name == "HEAL":
            self.image = pygame.image.load("art/ic_layhands.png").convert()
            self.skill_sprites = SpriteSheet("art/fx_layhands.png").images_at(
                [(0,0,200,200),
                (200,0,200,200),
                (400,0,200,200),
                (600,0,200,200)],colourkey=(0,255,0))
            self.skill_class = Heal

        self.image.set_alpha(255)
        self.rect = self.image.get_rect()
        self.rect.x = 250
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
    def activate_skill(self, enemy_Group, char):
        char.do_skill()
        return self.skill_class(self.skill_sprites, self.rect.centerx, enemy_Group)


# The activated skill to appear above pressed skill icon. Subclass of Sprite.
class Airstrike(pygame.sprite.Sprite):
    def __init__(self, skill_sprites, x, enemy_Group):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_array = skill_sprites
        self.sprite_id = 0
        self.image = skill_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = -200
        self.enemy_list = []
        self.hitbox_list = []
        for en in enemy_Group:
            self.hitbox_list.append(en.hitbox)
            self.enemy_list.append(en)

    def update(self):
        if self.rect.y < 575:
            self.rect.move_ip(0, 15)
        else:
            self.sprite_id += 1
            if self.sprite_id == 2:
                hits_idx = self.rect.collidelistall(self.hitbox_list)
                for i in hits_idx:
                    self.enemy_list[i].health -= 20
            if self.sprite_id >= len(self.sprites_array)*6:
                self.kill()
            else:
                self.image = self.sprites_array[(self.sprite_id)//6]


class Dazzle(pygame.sprite.Sprite):
    def __init__(self, skill_sprites, x, enemy_Group):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_array = skill_sprites
        self.sprite_id = 0
        self.image = skill_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.y = 550
        self.enemy_list = []
        self.hitbox_list = []
        for en in enemy_Group:
            self.hitbox_list.append(en.hitbox)
            self.enemy_list.append(en)

    def update(self):
        self.sprite_id += 1
        if self.sprite_id == 1:
                hits_idx = self.rect.collidelistall(self.hitbox_list)
                for i in hits_idx:
                    self.enemy_list[i].stun = 90
        if self.sprite_id >= len(self.sprites_array)*6:
            self.kill()
        else:
            self.image = self.sprites_array[(self.sprite_id)//6]


class Heal(pygame.sprite.Sprite):
    def __init__(self, skill_sprites, x, char_Group):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_array = skill_sprites
        self.sprite_id = 0
        self.image = skill_sprites[0]
        self.rect = self.image.get_rect()
        self.rect.y = 550
        min_health = 100
        for char in char_Group:
            if char.health <= min_health:
                self.healed = char
                min_health = char.health
        self.rect.centerx = self.healed.hitbox.centerx

    def update(self):
        self.sprite_id += 1
        if self.sprite_id >= len(self.sprites_array)*6:
            self.healed.health += 10
            self.kill()
        else:
            self.image = self.sprites_array[(self.sprite_id)//6]