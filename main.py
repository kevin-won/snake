import pygame
import random

pygame.init()
pygame.display.set_caption("Snake!")
screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width,screen_height))

black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

fps = pygame.time.Clock()

snake_pos = [295,295]

x_delta = 0
y_delta = 0

food_pos = [random.randint(0,590), random.randint(0,590)]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_delta = -10
                y_delta = 0
            elif event.key == pygame.K_RIGHT:
                x_delta = 10
                y_delta = 0
            elif event.key == pygame.K_UP:
                x_delta = 0
                y_delta = -10
            elif event.key == pygame.K_DOWN:
                x_delta = 0
                y_delta = 10
    snake_pos[0] += x_delta
    snake_pos[1] += y_delta
    if snake_pos[0] >= screen_width or snake_pos[0] < 0 or snake_pos[1] >= screen_height or snake_pos[1] < 0:
        running = False
    screen.fill(white)
    pygame.draw.rect(screen,blue,[snake_pos[0],snake_pos[1],10,10])
    pygame.display.update()

    fps.tick(30)
