import pygame
import os
import ctypes
from Skill import *
from Speaker import *
from Melee_Enemy import *
from Cid import *
from Shana import *
from Luxon import *

# Just changing the window position so I can see the whole screen.
# Might not be the same for your monitor?
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

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
bg_dia_castle = pygame.image.load("art/bg_dia_castle.jpg").convert()
click_sound = pygame.mixer.Sound("sound/fx_test.ogg")
click_sound.set_volume(0.1)
dialogue_file = open("dialogue.txt")

# Characters
Luxon = Luxon(50)
Cid = Cid(200)
Shana = Shana(350)

# Miscellaneous Groups
skillIcon_Group = pygame.sprite.Group()
skill_Group = pygame.sprite.Group()
health_Group = pygame.sprite.Group()
speaker_Group = pygame.sprite.Group()

# Character Group
char_Group = pygame.sprite.Group()
char_Group.add(Shana)
char_Group.add(Cid)
char_Group.add(Luxon)
limit = pygame.Rect((Shana.hitbox.x + Shana.hitbox.width, 0), (50, 1000))

# Enemy Group
enemy_Group = pygame.sprite.Group()
enemy_List = []
bob = Melee_Enemy(650)
enemy_List.append(bob)
enemy_List.append(Melee_Enemy(850))
enemy_List.append(Melee_Enemy(3000))
enemy_List.append(Melee_Enemy(2000))
for en in enemy_List:
    enemy_Group.add(en)

# Set up Healthbars
for char in char_Group:
    health_Group.add(char.healthbar)
for en in enemy_Group:
    health_Group.add(en.healthbar)

# Variables
score = 0
gold = 0
add_sprite = 0
moving = False
background_x = 0
left_speaker = Speaker("SHANA", -1)
right_speaker = Speaker("LUXON", 1)
speaker_Group.add(left_speaker)
speaker_Group.add(right_speaker)


def swap_speakers(left_char, right_char):
    if left_char != left_speaker:
        left_speaker.leave = True
        left = Speaker(left_char, -1)
        speaker_Group.add(left)
    else:
        left = left_char
    if right_char != right_speaker:
        right_speaker.leave = True
        right = Speaker(right_char, 1)
        speaker_Group.add(right)
    else:
        left = left_char
    return left, right


def swap_emotion(char, emotion):
    if left_speaker.name == char.upper():
        left_speaker.emotion_id = int(emotion)
    else:
        right_speaker.emotion_id = int(emotion)
    return

# Loop until the user clicks the close button.
quit = False
show_dialogue = True
dialogue_next = True
s = pygame.font.SysFont("comicsansms", 32).\
                    render('', 1, (255,255,255))
d = pygame.font.SysFont("comicsansms", 32).\
                    render('', 1, (255,255,255))
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
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                dialogue_next = True

    # DIALOGUE
    if show_dialogue:
        if dialogue_next:
            dialogue = dialogue_file.next().strip()
            if dialogue == "===":
                show_dialogue = False
            elif dialogue[0] == '[':
                speakers = dialogue[1:-1].split(', ')
                (left_speaker, right_speaker) = swap_speakers(speakers[0], speakers[1])
            elif dialogue[0] == '{':
                char_emotion = dialogue[1:-1].split(', ')
                swap_emotion(char_emotion[0], char_emotion[1])
            else:
                print(dialogue)
                dialogue = dialogue.split(': ')
                s = pygame.font.SysFont("comicsansms", 20).\
                    render(dialogue[0], 1, (180,180,180))
                d = pygame.font.SysFont("comicsansms", 28).\
                    render(dialogue[1], 1, (255,255,255))
                dialogue_next = False

        screen.blit(bg_dia_castle, (0,0))
        screen.blit(s, (590,830))
        screen.blit(d, (590,885))
        speaker_Group.update()
        speaker_Group.draw(screen)
        pygame.display.flip()
        clock.tick(60)
        continue



    # Testing multiple skills
    if add_sprite > 60:
        skillIcon_Group.add(SkillIcon("SKILL_NAME"))
        add_sprite = 0
    add_sprite += 1
    Cid.health -= 1
    bob.health -= 1

    # Check dead Enemies
    for en in enemy_List:
        if en.health < 0:
            dialogue_idx = 0
            # show_dialogue = True
            en.die()
            enemy_List.remove(en)
    # Check Enemy Collision
    for enemy in enemy_List:
        enemy.check_can_move(limit, enemy_List)

    # Setting up UI text
    xp_text = pygame.font.SysFont("comicsansms", 32).\
        render("XP: "+str(score), 1, (0,0,0))
    gold_text = pygame.font.SysFont("comicsansms", 32).\
        render("Gold: "+str(gold), 1, (255, 204, 0), (0, 0, 102))

    # --- Drawing code
    screen.blit(test_bg, (0,0))
    screen.blit(xp_text, (5, 10))
    screen.blit(gold_text, (5, 50))

    # draw hitbox
    # hitbox = pygame.Surface((bob.hitbox.width, bob.hitbox.height))
    # screen.blit(hitbox, (bob.hitbox.x, bob.hitbox.y))

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
