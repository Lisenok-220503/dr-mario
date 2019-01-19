import pygame
from random import choice
from color_const import * 

class Object():
    def __init__(self, x, y):
        self.pos = (x, y)

        self.color = choice(pill_colors)
        self.size = width, height = 30, 30

    def destruction(self):
        global points
        points += 50

class Pill(Object):
    def __init__(self, x1, y1, x2, y2):

        self.pos = (x, y)

        self.container = [Object(x1, y1), Object(x2, y2)]
        self.size = width, height = 60, 30
    def destruction(self):
        super().destruction()

    def draw(self, surface, position_1, position_2):
        pygame.draw.rect(surface, self.container[0].color, position_1) # position - (start_x, start_y, width, height)
        pygame.draw.rect(surface, self.container[1].color, position_2)


class Virus(Object):
    def __init__(self, x, y):
        super().__init__()

        self.pos = (x, y)
        self.size = width, height = 30, 30

    def destruction(self):
        global virus_amount
        virus_amount -= 1
        global points
        points += 200

    def draw(self, surface, position):
        pygame.draw.circle(surface, self.color, position, 15, 30)
        