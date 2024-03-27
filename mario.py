import pygame

# initiera pygame
pygame.init()
# __ENEMY IMAGE__
enemy_image = pygame.transform.scale(
    pygame.image.load("enemy.png"), (80, 64))
# laddar in bilderna som används till spelet
Standing_ground = pygame.transform.scale(
    pygame.image.load("mario.png"), (48, 64))
Jumping_ground = pygame.transform.scale(
    pygame.image.load("Jumping_mario.png"), (64, 64))
Background = pygame.transform.scale(
    pygame.image.load("Mario_background.jpg"), (800, 361))
# klocka så att skärmen refreshas
CLOCK = pygame.time.Clock()
# hur stor skärmen ska vara
screen_width = 800
screen_height = 362
screen = pygame.display.set_mode((screen_width, screen_height))
# x oxh y koordinater
X_POSITION_mario, Y_POSITION_mario = 400, 660

# Så att mario står där han ska när han blir inlagd
mario_rect = Standing_ground.get_rect(center=(X_POSITION_mario, Y_POSITION_mario))

# vad som gör så att marios hopp åker upp och ner på rätt sätt
Y_gravity = 0.7
Jump_height = 15
Y_velocity = 0

# run är sant så spelet körs och bilderna kommer upp på skärmen
run = True

# rörelse
while run:
    screen.blit(Background, (0, 0))
    screen.blit(enemy_image, (100, 100))

    # kollar vilka tangenter som blivit och blir tryckta
    key = pygame.key.get_pressed()
    # Justerar spelarens position efter vilka tangenter som trycks
    if key[pygame.K_a]:
        mario_rect.x -= 5
    if key[pygame.K_d]:
        mario_rect.x += 5
    # rörelse för hopp
    if key[pygame.K_SPACE]:
        if mario_rect.y == 250:
            Y_velocity = -Jump_height

    # Hur mario åker upp i luften
    Y_velocity += Y_gravity
    mario_rect.y += Y_velocity

    if mario_rect.y > 250:
        mario_rect.y = 250
        Y_velocity = 0
    # gör så att rätt bild på mario blir inlagd när
    if mario_rect.y == 250:
        screen.blit(Standing_ground, mario_rect)
    # Annars ska mariobilden vara hopp bilden
    else:
        screen.blit(Jumping_ground, mario_rect)

    pygame.display.update()
    # så att pygame avslutas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    # vilken framerate spelet ska ha
    CLOCK.tick(60)
    print(mario_rect.x)
    """Border Collision"""
    if mario_rect.x < 0:
        mario_rect.x = 0
    if mario_rect.x >= 750:
        mario_rect.x = 750

pygame.quit()
