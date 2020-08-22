import pygame
import sys
import random
pygame.init()

size = (25*25, 25*25)

#colors
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

BLOCK_SIZE = 25

x = random.randrange(0, size[0], BLOCK_SIZE)
y = random.randrange(0, size[1], BLOCK_SIZE)
#speed = BLOCK_SIZE
dx, dy = 0, 0

apple_x = random.randrange(0, size[0], BLOCK_SIZE)
apple_y = random.randrange(0, size[1], BLOCK_SIZE)


screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

snake = [(x, y), (x + BLOCK_SIZE, y), (x + BLOCK_SIZE*3, y)]

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    snake = [(i + dx, j + dy) for i, j in snake]

    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        dx = BLOCK_SIZE
        dy = 0
    if keys[pygame.K_LEFT]:
        dx = -BLOCK_SIZE
        dy = 0
    if keys[pygame.K_DOWN]:
        dy = BLOCK_SIZE
        dx = 0
    if keys[pygame.K_UP]:
        dy = -BLOCK_SIZE
        dx = 0
        
    for i in range(len(snake)):
        if snake[i][0] > size[0]:
            snake[i] = (0, snake[-1][i])
        # if i[0] < 0:
        #     snake[0] = (size[0], i[1])
        # if i[1] > size[1]:
        #     snake[0] = (i[0], 0)
        # if i[1] < 0:
        #     snake[0] = (i[0], size[1])


    screen.fill((180, 0, 180))
    
    [pygame.draw.rect(screen, BLACK, (i, j, BLOCK_SIZE, BLOCK_SIZE)) for i, j in snake]
    pygame.draw.rect(screen, GREEN, (apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE))
    
    
    if snake[0][0] == apple_x and snake[0][1] == apple_y:
        snake.append((apple_x, apple_y))
    print(snake)
    clock.tick(15)


    pygame.display.flip()