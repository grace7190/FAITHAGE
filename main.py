import pygame
from Skill import *

pygame.init()
screen = pygame.display.set_mode([1920,1080])
pygame.display.set_caption("#FAITHAGE")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# TESTING ONLY - global vars
test_bg = pygame.image.load("art/bg_temp.jpg").convert()
test_sprite = pygame.image.load("art/pl_temp.png").convert()
test_sprite.set_colorkey((0,255,0))
test_enemy = pygame.image.load("art/en_temp.png").convert()
test_enemy.set_colorkey((0,255,0))
click_sound = pygame.mixer.Sound("sound/fx_test.ogg")
# need to make a class for skill to store the x position, destroy self?

# Loop until the user clicks the close button.
quit = False

# Adding a skill
skill = Skill()
skill_Group = pygame.sprite.Group()
skill_Group.add(skill)

# -------- Main Program Loop -----------
while not quit:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # --- case for LMB pressed
            if pygame.mouse.get_pressed()[0]:
                click_sound.play()
                if skill.rect.collidepoint(pygame.mouse.get_pos()):
                    skill.triggered = True


    # --- Drawing code
    screen.blit(test_bg, (0,0))
    screen.blit(test_sprite, (600-test_sprite.get_width(),
                              780-test_sprite.get_height()+20))
    screen.blit(test_enemy, (1320,
                             780-test_enemy.get_height()+20))
    
    # --- update the screen
    skill_Group.update()
    skill_Group.draw(screen)
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
