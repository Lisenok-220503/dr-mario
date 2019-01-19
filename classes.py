from random import choice
from color_const import *

class Object():
    def __init__(self, x, y):
        self.color = choice(pill_colors)
        self.size = width, height = 30, 30

    def destruction(self):
        global points
        points += 50

class Pill(Object):
    def __init__(self, x, y):
        self.container = [Object(), Object()]
        self.size = width, height = 60, 30
    def destruction(self):
        super().destruction()

class Virus(Object):
    def __init__(self, x, y):
        super().__init__()

    def destruction(self):
        global virus_amount
        virus_amount -= 1
        global points
        points += 200