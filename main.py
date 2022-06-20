import pygame
import random
from models import *
from consts import *

pygame.init()
pygame.display.set_caption("Snake!")
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps = pygame.time.Clock()
tick = 10

snake = Snake()
apple = Apple()
score = Score()

def game_over():
    screen.fill(white)
    font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = font.render("Your Score is " + str(score.getScore()), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/4)
    screen.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
    quit()

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
        tick += 2

    pygame.draw.rect(screen, red, apple.getRect())

    if snake.hitItself() or snake.notInBounds():
        game_over()

    pygame.display.update()

    fps.tick(tick)
