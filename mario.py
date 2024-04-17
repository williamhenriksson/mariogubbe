import pygame

# initiera pygame
pygame.init()
# __ENEMY IMAGE__
enemy_image = pygame.transform.scale(pygame.image.load("enemy.png"), (80, 64))
# laddar in bilderna som används till spelet
# vanlig mario
Standing_ground = pygame.transform.scale(pygame.image.load("mario.png"), (48, 64))
# hoppande mario
Jumping_ground = pygame.transform.scale(pygame.image.load("Jumping_mario.png"), (64, 64))
# bakgrund
Background = pygame.transform.scale(pygame.image.load("Mario_background.jpg"), (800, 361))
# mario död
Death_image = pygame.transform.scale(pygame.image.load("Mario_death.png"), (48, 64))
# svart skärm
Game_over = pygame.transform.scale(pygame.image.load("game-over.webp"), (800, 362))
# game over text
Game_over_text = pygame.transform.scale(pygame.image.load("game over text.png"), (800, 362))
# klocka så att skärmen refreshas
CLOCK = pygame.time.Clock()

# hur mario bilden ska försvinna när man dör

Transparent = (0, 0, 0, 0)
# hur stor skärmen ska vara

screen = pygame.display.set_mode((800, 362))

# x oxh y koordinater
X_POSITION_MARIO, Y_POSITION_MARIO = 400, 362
X_POSITION_ENEMY, Y_POSITION_ENEMY = 700, 300

# Så att mario och enemy står där han ska när han blir inlagd
mario_rect = Standing_ground.get_rect(center=(X_POSITION_MARIO, Y_POSITION_MARIO))
Enemy_rect = enemy_image.get_rect(center=(X_POSITION_ENEMY, Y_POSITION_ENEMY))
Death_image_rect = Standing_ground.get_rect(center=(X_POSITION_MARIO, Y_POSITION_MARIO))
# vad som gör så att marios hopp åker upp och ner på rätt sätt
Y_gravity = 0.7
Jump_height = 15
Y_velocity = 0

# run är sant så spelet körs och bilderna kommer upp på skärmen
run = True

# konstant till att någon rör säg i en speciell hastighet
direction = -1
# hela run loopen så spelet går
while run:
    # Så att bilder på bakgrunden och enemy uppdateras
    screen.blit(Background, (0, 0))
    screen.blit(enemy_image, (Enemy_rect.x, Enemy_rect.y))

    # så att enemy rör sig i directions hastighet vilket är -1
    Enemy_rect.x += direction
    # så att gubben rör sig tills hans x kordinat är -60 i -1 i direction
    if Enemy_rect.x >= -60:
        direction = -1
    else:
        Enemy_rect.x = 800

    # Så allt försvinner förutom mario och enemy när man dör
    # så att game over skärmen kommer upp när man dör
    if mario_rect.x == Enemy_rect.x - 18 and mario_rect.y != Enemy_rect.y + 5:
        Standing_ground.fill(Transparent)
        Background.fill(Transparent)
        direction = 0
        screen.blit(Death_image, mario_rect)
        screen.blit(Game_over, (800, 362))
        screen.blit(Game_over_text, (0, 0))
    elif mario_rect.x == Enemy_rect.x + 25 and mario_rect.y != Enemy_rect.y + 5:
        Standing_ground.fill(Transparent)
        Background.fill(Transparent)
        direction = 0
        screen.blit(Death_image, mario_rect)
        screen.blit(Game_over, (800, 362))
        screen.blit(Game_over_text, (0, 0))

# kollar vilka tangenter som blivit och blir tryckta
    key = pygame.key.get_pressed()
# Justerar spelarens position efter vilka tangenter som trycks
    if key[pygame.K_a]:
        mario_rect.x -= 4
    if key[pygame.K_d]:
        mario_rect.x += 4

# rörelse för hopp ( mario )
    if key[pygame.K_SPACE]:
        if mario_rect.y == 250:
            Y_velocity = -Jump_height

# Så att mario inte bara flyger iväg när nam hoppar och att han flyger upp som han ska
    Y_velocity += Y_gravity
    mario_rect.y += Y_velocity

# Sätter en maxhöjd på marios hopp och när den uppnås slutar han gå uppåt
    if mario_rect.y > 250:
        mario_rect.y = 250
        Y_velocity = 0

# gör så att rätt bild på mario blir inlagd när
    if mario_rect.y == 250:
        screen.blit(Standing_ground, mario_rect)

# Annars ska mariobilden vara hopp bilden
    else:
        screen.blit(Jumping_ground, mario_rect)

# Så att displayen uppdateras och bilderna inte bara är där
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
