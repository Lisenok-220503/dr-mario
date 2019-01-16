import pygame
from random import choice
from color_const import *

class Object():
    def __init__(self):
        self.color = choice(pill_colors)
        self.size = width, height = 30, 30

    def destruction(self):
        global points
        points += 50

class Pill(Object):
    def __init__(self, color1, color2):
        self.container = [Object(), Object()]
        self.size = width, height = 60, 30
    def destruction(self):
        super().destruction()

    def draw(self, surface, position):
        pygame.draw.rect(surface, self.container[0].color, )

class Virus(Object):
    def __init__(self):
        super().__init__()


    def destruction(self):
        global virus_amount
        virus_amount -= 1
        global points
        points += 200

    def draw(self, surface, position):
        pygame.draw.circle(surface, self.color, position, 15, 30)
        