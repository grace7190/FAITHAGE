import pygame
import os
import ctypes
from random import randint
from Skill import *
from Speaker import *
from MeleeEnemy import *
from RangedEnemy import *
from Cid import *
from Shana import *
from Luxon import *

# Just changing the window position so I can see the whole screen.
# Might not be the same for your monitor?
ctypes.windll.user32.SetProcessDPIAware()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (0,30)

pygame.init()
screen = pygame.display.set_mode([1920,1080], pygame.FULLSCREEN)
pygame.display.set_caption("#FAITHAGE")

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Other Useful Things Here --------
# Hide the mouse cursor
# pygame.mouse.set_visible(False)

# TESTING ONLY - global vars
test_bg = pygame.image.load("art/bg_forest.jpg").convert()
bg_dia_castle = pygame.image.load("art/bg_dia_castle.jpg").convert()
ui_icons = pygame.image.load("art/ui_overlay.png").convert()
ui_icons.set_colorkey((255,255,255))
click_sound = pygame.mixer.Sound("sound/fx_test.ogg")
click_sound.set_volume(0.1)
dialogue_file = open("dialogue.txt")

# Characters
Luxon = Luxon(350)
Cid = Cid(200)
Shana = Shana(500)

# Miscellaneous Groups
S_skill_Group = pygame.sprite.Group()
L_skill_Group = pygame.sprite.Group()
C_skill_Group = pygame.sprite.Group()
skill_Group = pygame.sprite.Group()
health_Group = pygame.sprite.Group()
speaker_Group = pygame.sprite.Group()

# Character Group
char_Group = pygame.sprite.Group()
char_Group.add(Shana)
char_Group.add(Cid)
char_Group.add(Luxon)
melee_limit = pygame.Rect((Shana.hitbox.x + Shana.hitbox.width, 0), (50, 1000))
ranged_limit = pygame.Rect((1250, 0), (50, 1000))

# Enemy Group
enemy_Group = pygame.sprite.Group()
m_enemy_List = []
r_enemy_List = []

# bob = MeleeEnemy(1650)
# m_enemy_List.append(bob)
# m_enemy_List.append(MeleeEnemy(850))
# m_enemy_List.append(MeleeEnemy(3000))
# m_enemy_List.append(MeleeEnemy(2000))

r_enemy_List.append(RangedEnemy(2300))
r_enemy_List.append(RangedEnemy(3000))
# r_enemy_List.append(RangedEnemy(1600))
# for en in m_enemy_List:
#     enemy_Group.add(en)
# for en in r_enemy_List:
#     enemy_Group.add(en)

# Set up Healthbars
for char in char_Group:
    health_Group.add(char.healthbar)
# for en in enemy_Group:
#     health_Group.add(en.healthbar)

# Variables
level = 1
score = 0
gold = 0
moving = True
background_x = 0
quit = False
a_released = True
s_released = True
d_released = True
# Speakers
show_dialogue = False
dialogue_next = True
s = pygame.font.SysFont("comicsansms", 32).render('', 1, (255,255,255))
d = pygame.font.SysFont("comicsansms", 32).render('', 1, (255,255,255))
left_speaker = Speaker("Shana", -1)
right_speaker = Speaker("Luxon", 1)
speaker_Group.add(left_speaker)
speaker_Group.add(right_speaker)
# Skills
S_skill_y, L_skill_y, C_skill_y = 1000, 915, 835
S_skill_timer, L_skill_timer, C_skill_timer = 100, 60, 250
S_skill_time, L_skill_time, C_skill_time = 0, 0, 0


def swap_speakers(left_char, right_char):
    if left_char != left_speaker.name:
        left_speaker.leave = True
        left = Speaker(left_char, -1)
        speaker_Group.add(left)
    else:
        left = left_speaker
    if right_char != right_speaker.name:
        right_speaker.leave = True
        right = Speaker(right_char, 1)
        speaker_Group.add(right)
    else:
        right = right_speaker
    return left, right


def swap_emotion(char, emotion):
    if left_speaker.name == char.upper():
        left_speaker.emotion_id = int(emotion)
    else:
        right_speaker.emotion_id = int(emotion)
    return


def find_triggered_skills(score, gold):
    for skill in S_skill_Group:
        if not skill.triggered and skill.check_clicked():
            score += 500
            gold += 3
            skill_Group.add(skill.activate_skill())
    for skill in L_skill_Group:
        if not skill.triggered and skill.check_clicked():
            score += 500
            gold += 3
            skill_Group.add(skill.activate_skill())
    for skill in C_skill_Group:
        if not skill.triggered and skill.check_clicked():
            score += 500
            gold += 3
            skill_Group.add(skill.activate_skill())


def activate_skill(skills, score, gold):
    max_x = 0
    current = None
    for s in skills:
        if (not s.triggered) and (s.rect.x > max_x):
            current = s
            max_x = s.rect.x
    if current:
        score += 500
        gold += 3
        skill_Group.add(current.activate_skill())
        current.triggered = True

def setup_enemies(melee=0, ranged=0, skell=0, zombi=0, melee2=0, ranged2=0, nox=0, stella=0):
    for i in range(melee):
        m_enemy_List.append(MeleeEnemy(1920+200*i))
    for i in range(zombi):
        m_enemy_List.append(Zombi(1920+200*(i+melee)))
    # for i in range(melee):
    #     m_enemy_List.append(MeleeEnemy(1920+200*i))
    for en in m_enemy_List:
        enemy_Group.add(en)
        health_Group.add(en.healthbar)
    for en in r_enemy_List:
        enemy_Group.add(en)
        health_Group.add(en.healthbar)


setup_enemies(4)

# -------- Main Program Loop ---------
while not quit:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                click_sound.play()
                find_triggered_skills(score, gold)
        elif event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:
                dialogue_next = True
            if pygame.key.get_pressed()[pygame.K_ESCAPE]:
                quit = True
            if pygame.key.get_pressed()[pygame.K_a]:
                if a_released:
                    activate_skill(C_skill_Group, score, gold)
                    a_released = False
            if pygame.key.get_pressed()[pygame.K_s]:
                if s_released:
                    activate_skill(L_skill_Group, score, gold)
                    s_released = False
            if pygame.key.get_pressed()[pygame.K_d]:
                if d_released:
                    activate_skill(S_skill_Group, score, gold)
                    d_released = False
        elif event.type == pygame.KEYUP:
            if not pygame.key.get_pressed()[pygame.K_a]:
                a_released = True
            if not pygame.key.get_pressed()[pygame.K_s]:
                s_released = True
            if not pygame.key.get_pressed()[pygame.K_d]:
                d_released = True

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

    # Skills
    if S_skill_time >= S_skill_timer:
        S_skill_Group.add(SkillIcon("AIRSTRIKE", S_skill_y))
        S_skill_time = 0
    if L_skill_time >= L_skill_timer:
        L_skill_Group.add(SkillIcon("DAZZLE", L_skill_y))
        L_skill_time = 0
    if C_skill_time >= C_skill_timer:
        C_skill_Group.add(SkillIcon("AIRSTRIKE", C_skill_y))
        C_skill_time = 0
    S_skill_time += 1
    L_skill_time += 1
    C_skill_time += 1

    # Check dead Enemies
    for en in m_enemy_List:
        if en.health <= 0:
            # dialogue_idx = 0
            # show_dialogue = True
            en.die()
            m_enemy_List.remove(en)
    for en in r_enemy_List:
        if en.health <= 0:
            en.die()
            r_enemy_List.remove(en)

    # Check Enemy Collision
    for en in m_enemy_List:
        en.check_can_move(melee_limit, m_enemy_List)
    for en in r_enemy_List:
        if en.has_frontline:
            en.check_can_move(ranged_limit, r_enemy_List)
        else:
            en.check_can_move(melee_limit, r_enemy_List)

    # Check Hero damage taken
    for en in m_enemy_List:
        if en.attacking and en.attack_time >= en.time_till_attack:
            en.attack_time = 0
            Shana.health -= en.damage
    for en in r_enemy_List:
        if en.attacking and en.attack_time >= en.time_till_attack:
            en.attack_time = 0
            [Shana, Cid, Luxon][randint(0,2)].health -= en.damage

    # Check Hero damage given
    for en in m_enemy_List:
        if melee_limit.colliderect(en.hitbox):
            moving = False
            Shana.change_anim(Shana.attack_anim)
            Shana.attacking = True
            if Shana.attack_time >= Shana.time_till_attack:
                Shana.attack_time = 0
                en.health -= Shana.damage
            break
        else:
            Shana.attacking = False
    if not m_enemy_List: # no more melee (man got damn dis some spaghetto ass code)
        if r_enemy_List:
            for en in r_enemy_List:
                if melee_limit.colliderect(en.hitbox):
                    moving = False
                    if Shana.attack_time >= Shana.time_till_attack:
                        Shana.attack_time = 0
                        en.health -= Shana.damage
                    break
                else:
                    moving = True
                en.has_frontline = False
        else:
            moving = True

    # Set walking
    if moving:
        Shana.change_anim(Shana.walk_anim)
        Cid.change_anim(Cid.walk_anim)
        Luxon.change_anim(Luxon.walk_anim)
        Shana.attacking = False
        for en in r_enemy_List:
            if not en.has_frontline:
                en.hitbox.move_ip(-2,0)
        for en in m_enemy_List:
            en.hitbox.move_ip(-2,0)
        for skill in skill_Group:
            skill.rect.move_ip(-2,0)
    else:
        Cid.change_anim(Cid.idle_anim)
        Luxon.change_anim(Luxon.idle_anim)
        Shana.change_anim(Shana.attack_anim)
        Shana.attacking = True

    # Scroll background
    if moving:
        background_x -= 2

    # Setting up UI text
    xp_text = pygame.font.SysFont("comicsansms", 32).\
        render("XP: "+str(score), 1, (0,0,0))
    gold_text = pygame.font.SysFont("comicsansms", 32).\
        render("Gold: "+str(gold), 1, (255, 204, 0), (0, 0, 102))

    # --- Drawing code
    screen.blit(test_bg, (background_x % -(test_bg.get_width()-screen.get_width()),0))
    screen.blit(xp_text, (5, 10))
    screen.blit(gold_text, (5, 50))
    screen.blit(ui_icons, (0,0))

# #### draw hitbox
    for en in enemy_Group:
        hitbox = pygame.Surface((en.hitbox.width, en.hitbox.height))
        screen.blit(hitbox, (en.hitbox.x, en.hitbox.y))
# ####

    # --- update Sprites
    S_skill_Group.update()
    L_skill_Group.update()
    C_skill_Group.update()
    skill_Group.update()
    char_Group.update()
    enemy_Group.update()
    # --- update the screen
    S_skill_Group.draw(screen)
    L_skill_Group.draw(screen)
    C_skill_Group.draw(screen)
    char_Group.draw(screen)
    enemy_Group.draw(screen)
    skill_Group.draw(screen)
    health_Group.draw(screen)

    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()
