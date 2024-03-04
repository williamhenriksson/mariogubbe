import pygame

pygame.init()

screen_width = 800
screen_height = 700

screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((300, 250, 50, 50))

run = True

while run:

    pygame.draw.rect(screen, (255, 255, 255), player)
    key = pygame.key.get_pressed()
    if key[pygame.K_a] == True:
    for event in pygame.event.get():
        if event.type == event.QUIT:
            run = false
    pygame.display.update()


# Jump funktion

# Movement should contain: move right, move left och run


# Collisions: with blocks and enemies

# Enemies: Goomba

# Map, blocks and background drawings

# Character, Mario

# Powerups, mushroom


pygame.quit()