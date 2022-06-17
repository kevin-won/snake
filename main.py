import pygame
import random
from models import *
from consts import *

pygame.init()
pygame.display.set_caption("Snake!")
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps = pygame.time.Clock()
tick = 30

snake = Snake()
apple = Apple()
score = Score()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and snake.getDirection() != RIGHT:
                snake.changeDirection(LEFT)
            elif event.key == pygame.K_RIGHT and snake.getDirection() != LEFT:
                snake.changeDirection(RIGHT)
            elif event.key == pygame.K_UP and snake.getDirection() != DOWN:
                snake.changeDirection(UP)
            elif event.key == pygame.K_DOWN and snake.getDirection() != UP:
                snake.changeDirection(DOWN)
    screen.fill(white)

    snake.updateSnake()
    for pos in snake.getSnakeBody():
        pygame.draw.rect(screen,blue,[pos[0],pos[1],10,10])


    if snake.eatsApple(apple):
        score.increment()
        apple.newApple()
        snake.elongate()
        tick += 8

    pygame.draw.rect(screen, red, apple.getRect())

    pygame.display.update()

    fps.tick(30)
