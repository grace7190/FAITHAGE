import pygame

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([1920, 1080])
 
# This sets the name of the window
pygame.display.set_caption('#FAITHAGE')
 
clock = pygame.time.Clock()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
background_image = pygame.image.load("art/bg_temp.jpg").convert()
player_image = pygame.image.load("art/pl_temp.png").convert()
player_image.set_colorkey((0,255,0))

done = False
 
while not done:
    ## ----- Main Event Loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("click/tap")
    ## ----- Game Logic Here
    mouse_position = pygame.mouse.get_pos()
            
    ## ----- Rendering Here
    screen.blit(background_image, background_position)
    screen.blit(player_image, [600-player_image.get_width(),780-player_image.get_height()+20])
    pygame.display.flip()
 
    clock.tick(60)
 
pygame.quit()
