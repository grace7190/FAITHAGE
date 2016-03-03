import pygame
import os
import ctypes
from Skill import *
from Character import *
from Enemy import *

# Just changing the window position so I can see the whole screen.
# Might not be the same for your monitor?
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,20)

pygame.init()
screen = pygame.display.set_mode([1920,1080])
pygame.display.set_caption("#FAITHAGE")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Other Useful Things Here --------
# Hide the mouse cursor
# pygame.mouse.set_visible(False)

# TESTING ONLY - global vars
test_bg = pygame.image.load("art/bg_temp.jpg").convert()
click_sound = pygame.mixer.Sound("sound/fx_test.ogg")
click_sound.set_volume(0.1)

CHAR_IMG_SIZE = (400,400)
CID_X = 400 - CHAR_IMG_SIZE[0]
SHANA_X = 700 - CHAR_IMG_SIZE[0]
CHAR_Y = 780 - 350 + 20
HITBOX = (150,350)

Cid_rect = pygame.Rect((CID_X,CHAR_Y), HITBOX)
Cid = Character("cid", Cid_rect.centerx, Cid_rect.y)
Shana = Character("shana", SHANA_X, CHAR_Y)

skillIcon_Group = pygame.sprite.Group()
skill_Group = pygame.sprite.Group()
health_Group = pygame.sprite.Group()
char_Group = pygame.sprite.Group()
enemy_Group = pygame.sprite.Group()

# Characters
char_Group.add(Cid)
char_Group.add(Shana)

# Enemies
enemy_Group.add(Enemy("melee_minion_atk", 1320, CHAR_Y))

# Set up Healthbars
for char in char_Group:
    health_Group.add(char.healthbar)
for en in enemy_Group:
    health_Group.add(en.healthbar)

score = 0
gold = 0
add_sprite = 0


# Loop until the user clicks the close button.
quit = False
# -------- Main Program Loop ---------
while not quit:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                click_sound.play()
                for skill in skillIcon_Group:
                    if not skill.triggered and skill.check_clicked():
                        score += 500
                        gold += 3
                        skill_Group.add(skill.activate_skill())

    # Testing multiple skills
    if add_sprite > 60:
        skillIcon_Group.add(SkillIcon("SKILL_NAME"))
        add_sprite = 0
        Shana.health -= 9
    add_sprite += 1
    Cid.health -= 1

    # Setting up UI text
    xp_text = pygame.font.SysFont("comicsansms", 32).\
        render("XP: "+str(score), 1, (0,0,0))
    gold_text = pygame.font.SysFont("comicsansms", 32).\
        render("Gold: "+str(gold), 1, (255, 204, 0), (0, 0, 102))

    # --- Drawing code
    screen.blit(test_bg, (0,0))
    screen.blit(xp_text, (5, 10))
    screen.blit(gold_text, (5, 50))

    # --- update Sprites
    skillIcon_Group.update()
    skill_Group.update()
    char_Group.update()
    enemy_Group.update()
    # --- update the screen
    skillIcon_Group.draw(screen)
    skill_Group.draw(screen)
    char_Group.draw(screen)
    enemy_Group.draw(screen)
    health_Group.draw(screen)
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
