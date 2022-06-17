from consts import *
import pygame

class Snake(object):
    """
    A class representing a snake.
    """
    def __init__(self):
        self._snake_body = [[70, 50], [80, 50], [90, 50], [100, 50]]
        self._start_pos = [100,50]
        self._x_delta = 0
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
        new_pos = [0,0]
        last_index = len(self._snake_body) - 1
        new_pos[0] = self._snake_body[last_index][0] + self._x_delta
        new_pos[1] = self._snake_body[last_index][1] + self._y_delta
        self._snake_body.append(new_pos)
        self._snake_body.pop(0)

    def eatsFood(self,food):
        return pygame.Rect.colliderect(food, pygame.Rect((10,10),(self._head[0], self._head[1])))

class Food(object):
    """
    A class representing food for the snake to eat.
    """
    def __init__(self):
        self._x = random.randint(0,590)
        self.y = random.randint(0,590)

    def getX(self):
        return self._x
