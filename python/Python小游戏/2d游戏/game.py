import pygame
import time
import random

pygame.init()

# 设置游戏窗口
width, height = 1000, 1000
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# 定义颜色
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# 蛇和食物的大小
block_size = 20
snake_speed = 15

# 蛇的初始位置和长度
snake = [(width // 2, height // 2)]
snake_length = 1
snake_direction = "RIGHT"

# 食物的初始位置
food_position = (random.randrange(0, width - block_size, block_size),
                 random.randrange(0, height - block_size, block_size))

# 设置字体
font = pygame.font.SysFont(None, 35)

# 定义函数：绘制蛇
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(window, green, [segment[0], segment[1], block_size, block_size])

# 定义函数：显示得分
def show_score(score):
    score_text = font.render("Score: " + str(score), True, white)
    window.blit(score_text, [10, 10])

# 游戏主循环
game_over = False
clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake_direction != "RIGHT":
                snake_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and snake_direction != "LEFT":
                snake_direction = "RIGHT"
            elif event.key == pygame.K_UP and snake_direction != "DOWN":
                snake_direction = "UP"
            elif event.key == pygame.K_DOWN and snake_direction != "UP":
                snake_direction = "DOWN"

    # 移动蛇
    if snake_direction == "UP":
        snake[0] = (snake[0][0], snake[0][1] - block_size)
    elif snake_direction == "DOWN":
        snake[0] = (snake[0][0], snake[0][1] + block_size)
    elif snake_direction == "LEFT":
        snake[0] = (snake[0][0] - block_size, snake[0][1])
    elif snake_direction == "RIGHT":
        snake[0] = (snake[0][0] + block_size, snake[0][1])

    # 检查是否吃到食物
    if snake[0] == food_position:
        food_position = (random.randrange(0, width - block_size, block_size),
                         random.randrange(0, height - block_size, block_size))
        snake_length += 1

    # 更新蛇的身体
    if len(snake) > 1:
        snake[1:] = snake[:-1]

 
    # 清空窗口
    window.fill(black)

    # 绘制食物
    pygame.draw.rect(window, red, [food_position[0], food_position[1], block_size, block_size])

    # 绘制蛇
    draw_snake(snake)

    # 显示得分
    show_score(snake_length - 1)

    # 更新显示
    pygame.display.update()

    # 控制蛇的速度
    clock.tick(snake_speed)

# 游戏结束后显示信息
window.fill(black)
game_over_text = font.render("Game Over", True, white)
window.blit(game_over_text, [width // 3, height // 3])
show_score_text = font.render("Your Score: " + str(snake_length - 1), True, white)
window.blit(show_score_text, [width // 3, height // 2])
pygame.display.update()

# 等待几秒钟后退出
time.sleep(10)

pygame.quit()