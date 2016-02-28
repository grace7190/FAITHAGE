import pygame
import os
from Skill import *

# Just changing the window position so I can see the whole screen.
# Might not be the same for your monitor?
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
test_sprite = pygame.image.load("art/pl_shana.png").convert()
test_sprite.set_colorkey((0,255,0))
test_enemy = pygame.image.load("art/en_temp.png").convert()
test_enemy.set_colorkey((0,255,0))
click_sound = pygame.mixer.Sound("sound/fx_test.ogg")
click_sound.set_volume(0.1)

skillIcon_Group = pygame.sprite.Group()
skill_Group = pygame.sprite.Group()
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
                        skill_Group.add(skill.activate_skill())

    # Testing multiple skills
    if add_sprite > 60:
        skillIcon_Group.add(SkillIcon("SKILL_NAME"))
        add_sprite = 0
    add_sprite += 1

    # --- Drawing code
    screen.blit(test_bg, (0,0))
    screen.blit(test_sprite, (600-test_sprite.get_width(),
                              780-test_sprite.get_height()+20))
    screen.blit(test_enemy, (1320,
                             780-test_enemy.get_height()+20))

    # --- update Sprites
    skillIcon_Group.update()
    skill_Group.update()
    # --- update the screen
    skillIcon_Group.draw(screen)
    skill_Group.draw(screen)
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
