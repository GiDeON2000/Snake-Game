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

snake = [(x, y)]

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# snake = [(i + dx, j + dy) for i, j in snake]
	x += dx
	y += dy
	snake.append((x, y))

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
			snake[i] = (0, snake[i][1])
		if snake[i][0] < 0:
			snake[i] = (size[0], snake[i][1])
		if snake[i][1] > size[1]:
			snake[i] = (snake[i][0], 0)
		if snake[i][1] < 0:
			snake[i] = (snake[i][0], size[1])
	
	if snake[0][0] == apple_x and snake[0][1] == apple_y:
		snake.append((apple_x + dx, apple_y + dy))
		apple_x = random.randrange(0, size[0], BLOCK_SIZE)
		apple_y = random.randrange(0, size[1], BLOCK_SIZE)


	screen.fill((180, 0, 180))
    
	[pygame.draw.rect(screen, BLACK, (i, j, BLOCK_SIZE, BLOCK_SIZE)) for i, j in snake]
	pygame.draw.rect(screen, WHITE, (snake[-1][0], snake[-1][1], BLOCK_SIZE, BLOCK_SIZE))
	pygame.draw.rect(screen, GREEN, (apple_x, apple_y, BLOCK_SIZE, BLOCK_SIZE))

	print(snake)
	clock.tick(10)


	pygame.display.flip()