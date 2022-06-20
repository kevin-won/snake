from consts import *
import pygame
import random

class Snake(object):
    """
    A class representing a snake.
    """
    def __init__(self):
        self._snake_body = [[70, 50], [80, 50], [90, 50], [100, 50]]
        self._start_pos = [100,50]
        self._x_delta = 10
        self._y_delta = 0
        self._direction = RIGHT
        self._head = self._snake_body[len(self._snake_body) - 1]

    def getSnakeBody(self):
        result = []
        for element in self._snake_body:
            result.append(element)
        return result

    def getDirection(self):
        return self._direction

    def changeDirection(self, direction):
        if direction == LEFT:
            self._x_delta = -10
            self._y_delta = 0
            self._direction = LEFT
        elif direction == RIGHT:
            self._x_delta = 10
            self._y_delta = 0
            self._direction = RIGHT
        elif direction == UP:
            self._x_delta = 0
            self._y_delta = -10
            self._direction = UP
        else:
            self._x_delta = 0
            self._y_delta = 10
            self._direction = DOWN

    def updateSnake(self):
        self.elongate()
        self._snake_body.pop(0)

    def eatsApple(self,apple):
        return pygame.Rect.colliderect(apple.getRect(), pygame.Rect((self._head[0], self._head[1]), (10,10)))

    def elongate(self):
        new_pos = [0,0]
        last_index = len(self._snake_body) - 1
        new_pos[0] = self._snake_body[last_index][0] + self._x_delta
        new_pos[1] = self._snake_body[last_index][1] + self._y_delta
        self._snake_body.append(new_pos)
        print(self._snake_body)
        self._head = self._snake_body[len(self._snake_body) - 1]

    def hitItself(self):
        for coordinate in self._snake_body[:-1]:
            if self._head[0] == coordinate[0] and self._head[1] == coordinate[1]:
                return True
        return False

    def notInBounds(self):
        if self._head[0] < 0 or self._head[0]  + 10 > SCREEN_WIDTH:
            return True
        elif self._head[1] < 0 or self._head[1] + 10 > SCREEN_HEIGHT:
            return True
        return False

class Apple(object):
    """
    A class representing an apple for the snake to eat.
    """
    def __init__(self):
        self._x = random.randint(0,400)
        self._y = random.randint(0,400)
        self._rect = pygame.Rect((self._x, self._y), (10, 10))

    def getRect(self):
        return self._rect

    def newApple(self):
        self._x = random.randint(0,400)
        self._y = random.randint(0,400)
        self._rect = pygame.Rect((self._x, self._y), (10, 10))

class Score(object):
    """
    A class representing the score of the game.
    """
    def __init__(self):
        self._score = 0

    def increment(self):
        self._score += 1

    def getScore(self):
        return self._score
