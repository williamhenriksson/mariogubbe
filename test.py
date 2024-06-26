import pygame
import random

# initiera pygame
pygame.init()
# Coin bild
Coin_image = pygame.transform.scale(pygame.image.load("coin-1.png"), (30, 30))
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

# movement
Walking_speed = 5
# hur mario bilden ska försvinna när man dör

Transparent = (0, 0, 0, 0)

# border edges
Border_edge_l = 0
Border_edge_r = 750
Goomba_edge_l = -60
Goomba_edge_r = 800
Coin_edge_l = 25
Coin_edge_r = 700
Coin_edge_upp = 90
Coin_edge_down = 270
# hur stor skärmen ska vara

screen = pygame.display.set_mode((800, 362))

# x oxh y koordinater
X_POSITION_MARIO, Y_POSITION_MARIO = 400, 362
X_POSITION_ENEMY, Y_POSITION_ENEMY = 700, 300
X_POSITION_ENEMY_2, Y_POSITION_ENEMY_2 = 700, 300
X_POSITION_ENEMY_3, Y_POSITION_ENEMY_3 = 800, 300
Coin_position_x, Coin_position_y = 500, 130
# Så att mario och enemy står där han ska när han blir inlagd
mario_rect = Standing_ground.get_rect(center=(X_POSITION_MARIO, Y_POSITION_MARIO))
Enemy_rect = enemy_image.get_rect(center=(X_POSITION_ENEMY, Y_POSITION_ENEMY))
Enemy_rect_2 = enemy_image.get_rect(center=(X_POSITION_ENEMY_2, Y_POSITION_ENEMY_2))
Enemy_rect_3 = enemy_image.get_rect(center=(X_POSITION_ENEMY_3, Y_POSITION_ENEMY_3))
Death_image_rect = Standing_ground.get_rect(center=(X_POSITION_MARIO, Y_POSITION_MARIO))
# vad som gör så att marios hopp åker upp och ner på rätt sätt
Y_gravity = 0.7
Jump_height = 15
Y_velocity = 0
Mario_max_height = 250
# mario död bool så det blir enklare för han att sluta fungera när han dör
Mario_dead = False
Score = 0

def handle_game_over(Mario_dead, key, mario_rect, Enemy_rect, direction):
    if Mario_dead:
        key = None
        mario_rect.x = mario_rect.x
        Enemy_rect.x = Enemy_rect.x
        direction = 0
    return key, mario_rect, Enemy_rect, direction

def handle_game_over_2(Mario_dead, key, mario_rect, Enemy_rect_2, direction):
    if Mario_dead:
        key = None
        mario_rect.x = mario_rect.x
        Enemy_rect.x = Enemy_rect.x
        direction = 0
    return key, mario_rect, Enemy_rect_2, direction

def handle_game_over_3(Mario_dead, key, mario_rect, Enemy_rect_3, direction):
    if Mario_dead:
        key = None
        mario_rect.x = mario_rect.x
        Enemy_rect.x = Enemy_rect.x
        direction = 0
    return key, mario_rect, Enemy_rect_3, direction

# run är sant så spelet körs och bilderna kommer upp på skärmen
run = True


# konstant till att någon rör säg i en speciell hastighet

direction = -1.8
direction_2 = -1
direction_3 = -2.4
# hela run loopen så spelet går
while run:
    # kollar vilka tangenter som blivit och blir tryckta
    key = pygame.key.get_pressed()

    key, mario_rect, Enemy_rect, direction = handle_game_over(Mario_dead, key, mario_rect, Enemy_rect, direction)
    key, mario_rect, Enemy_rect_2, direction = handle_game_over(Mario_dead, key, mario_rect, Enemy_rect_2, direction)
    key, mario_rect, Enemy_rect_3, direction = handle_game_over(Mario_dead, key, mario_rect, Enemy_rect_3, direction)
    # Så att bilder på bakgrunden och enemy uppdateras
    screen.blit(Background, (0, 0))
    screen.blit(enemy_image, (Enemy_rect.x, Enemy_rect.y))
    screen.blit(Coin_image, (Coin_position_x, Coin_position_y))
    # Justerar spelarens position efter vilka tangenter som trycks
    if key[pygame.K_a]:
        mario_rect.x -= Walking_speed
    if key[pygame.K_d]:
        mario_rect.x += Walking_speed
    # rörelse för hopp (mario)
    if key[pygame.K_SPACE]:
        if mario_rect.y == Mario_max_height:
            Y_velocity = -Jump_height

    # Så att mario inte bara flyger iväg när nam hoppar och att han flyger upp som han ska
    Y_velocity += Y_gravity
    mario_rect.y += Y_velocity
    if Coin_position_x + 10 > mario_rect.x > Coin_position_x - 40 and Coin_position_y + 20 > mario_rect.y > Coin_position_y - 30:
        Coin_position_x = random.randrange(Coin_edge_l, Coin_edge_r)
        Coin_position_y = random.randrange(Coin_edge_upp, Coin_edge_down)
        Score += 1

    # Score counter
    score_font = pygame.font.Font('freesansbold.ttf', 32)
    score_surface = score_font.render(f'Score: {Score}', True, (0, 0, 0))
    screen.blit(score_surface, (20, 20))

    if Score > 10:
        screen.blit(enemy_image, (Enemy_rect_2.x, Enemy_rect_2.y))
        Enemy_rect_2.x += direction_2
        if Enemy_rect_2.x + 20 >= mario_rect.x >= Enemy_rect_2.x - 20 and Enemy_rect_2.y + 30 >= mario_rect.y >= Enemy_rect_2.y - 40:
            Mario_dead = True
            Standing_ground.fill(Transparent)
            Background.fill(Transparent)
            direction = 0
            screen.blit(Death_image, mario_rect)
            screen.blit(Game_over, (800, 362))
            screen.blit(Game_over_text, (0, 0))

    if Score > 20:
        screen.blit(enemy_image, (Enemy_rect_3.x, Enemy_rect_3.y))
        Enemy_rect_3.x += direction_3
        if Enemy_rect_3.x + 20 >= mario_rect.x >= Enemy_rect_3.x - 20 and Enemy_rect_3.y + 30 >= mario_rect.y >= Enemy_rect_3.y - 40:
            Mario_dead = True
            Standing_ground.fill(Transparent)
            Background.fill(Transparent)
            direction = 0
            screen.blit(Death_image, mario_rect)
            screen.blit(Game_over, (800, 362))
            screen.blit(Game_over_text, (0, 0))
    # Sätter en maxhöjd på marios hopp och när den uppnås slutar han gå uppåt
    if mario_rect.y > Mario_max_height:
        mario_rect.y = Mario_max_height
        Y_velocity = 0

    # gör så att rätt bild på mario blir inlagd när
    if mario_rect.y == Mario_max_height:
        screen.blit(Standing_ground, mario_rect)

    # Annars ska mariobilden vara hopp bilden
    else:
        screen.blit(Jumping_ground, mario_rect)

    # så att enemy rör sig i directions hastighet vilket är -1
    Enemy_rect.x += direction
    # så att gubben rör sig tills hans x kordinat är -60 i -1 i direction
    if Enemy_rect.x >= Goomba_edge_l:
        direction = -1.8
    else:
        Enemy_rect.x = Goomba_edge_r

    if Enemy_rect_2.x >= Goomba_edge_l:
        direction = -1.8
    else:
        Enemy_rect_2.x = Goomba_edge_r

    # Border Collision
    if mario_rect.x < Border_edge_l:
        mario_rect.x = Border_edge_l
    if mario_rect.x >= Border_edge_r:
        mario_rect.x = Border_edge_r

    # Så allt försvinner förutom mario och enemy när man dör
    # så att game over skärmen kommer upp när man dör
    if Enemy_rect.x + 20 >= mario_rect.x >= Enemy_rect.x - 20 and Enemy_rect.y + 30 >= mario_rect.y >= Enemy_rect.y - 40:
        Mario_dead = True
        Standing_ground.fill(Transparent)
        Background.fill(Transparent)
        direction = 0
        screen.blit(Death_image, mario_rect)
        screen.blit(Game_over, (800, 362))
        screen.blit(Game_over_text, (0, 0))

    # Så att displayen uppdateras och bilderna inte bara är där
    pygame.display.update()
# så att pygame avslutas
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
# vilken framerate spelet ska ha
    CLOCK.tick(60)
print(mario_rect.x)

pygame.quit()
