import pygame
import sys
import random
from time import sleep
pygame.init()

size = (25*25, 25*25)

def apple_spawn(snake):
    x = random.randrange(0, size[0], BLOCK_SIZE)
    y = random.randrange(0, size[1], BLOCK_SIZE)
    if (x, y) in snake:
        x, y = apple_spawn(snake)
    return (x, y)

#colors
WHITE = (255, 255, 255)
BLUE = (204, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

dirs = {"UP": True, "Down": True, "Right": True, "Left": True}

BLOCK_SIZE = 25
dx, dy = BLOCK_SIZE, 0

x = random.randrange(0, size[0], BLOCK_SIZE)
y = random.randrange(0, size[1], BLOCK_SIZE)

snake = [(x, y)]
snake_size = len(snake)

apple_x, apple_y = apple_spawn(snake)

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    x += dx
    y += dy
    snake.append((x, y))

    snake = snake[-snake_size:]
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and dirs["Right"]:
        dirs = {"UP": True, "Down": True, "Right": True, "Left": False}
        dx = BLOCK_SIZE
        dy = 0

    if keys[pygame.K_LEFT] and dirs["Left"]:
        dirs = {"UP": True, "Down": True, "Right": False, "Left": True}
        dx = -BLOCK_SIZE
        dy = 0

    if keys[pygame.K_DOWN] and dirs["Down"]:
        dirs = {"UP": False, "Down": True, "Right": True, "Left": True}
        dy = BLOCK_SIZE
        dx = 0

    if keys[pygame.K_UP] and dirs["UP"]:
        dirs = {"UP": True, "Down": False, "Right": True, "Left": True}
        dy = -BLOCK_SIZE
        dx = 0

    for i in range(len(snake)):
        if snake[i][0] > size[0]:
            x = 0
            snake[i] = (0, snake[i][1])

        if snake[i][0] < 0:
            x = size[0]
            snake[i] = (size[0], snake[i][1])

        if snake[i][1] > size[1]:
            snake[i] = (snake[i][0], 0)
            y = 0

        if snake[i][1] < 0:
            snake[i] = (snake[i][0], size[1])
            y = size[1]

    if snake[-1][0] == apple_x and snake[-1][1] == apple_y:
        snake_size += 1
        apple_x, apple_y = apple_spawn(snake)

    screen.fill((0, 0, 180))
    print(snake)
    if len(snake) != len(set(snake)):
        screen.blit(pygame.image.load('over.png'), (0, 0))
        break

    [pygame.draw.rect(screen, GREEN, (i, j, BLOCK_SIZE-2, BLOCK_SIZE-2)) for i, j in snake]
    pygame.draw.rect(screen, WHITE, (snake[-1][0], snake[-1][1], BLOCK_SIZE-2, BLOCK_SIZE-2))
    pygame.draw.rect(screen, RED, (apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE))

    screen.blit(pygame.font.SysFont('serif', 36).render((f"Scores: {snake_size}"), 0, (0, 180, 0)), (25, 25))

    clock.tick(7)
    pygame.display.flip()