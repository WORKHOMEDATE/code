import random
import pygame

pygame.init()
WIDTH, HEIGHT = 400, 400
WINDOW_SIZE = (WIDTH, HEIGHT)
CELL_SIZE = 20
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("贪吃蛇游戏")
snake = [(100, 100)]
snake_dir = (CELL_SIZE, 0)
food = (200, 200)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, CELL_SIZE):
        snake_dir = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -CELL_SIZE):
        snake_dir = (0, CELL_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (CELL_SIZE, 0):
        snake_dir = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-CELL_SIZE, 0):
        snake_dir = (CELL_SIZE, 0)
    x, y = snake[0]
    new_head = (x + snake_dir[0], y + snake_dir[1])
    snake.insert(0, new_head)
    if snake[0] == food:
        food = (random.randint(0, WIDTH // CELL_SIZE - 1) * CELL_SIZE,
                random.randint(0, HEIGHT // CELL_SIZE - 1) * CELL_SIZE)
    else:
        snake.pop()
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL_SIZE, CELL_SIZE))

    pygame.display.update()
    
    pygame.time.delay(100)

pygame.quit()