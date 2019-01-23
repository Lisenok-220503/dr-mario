import pygame
from random import choice
from color_const import * 

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Object():
    def __init__(self, x, y):
        self.pos = [x, y]

        self.color = choice(pill_colors)
        self.size = width, height = 30, 30

    def destruction(self):
        global points
        points += 50

    def change_pos(self, x_new, y_new):
        self.pos = [x_new, y_new]

    def move_pos(self, k1, k2):
        self.pos[0] += k1
        self.pos[1] += k2

    def get_pos(self):
        return self.pos[0], self.pos[1]

class Pill(Object):
    def __init__(self, x1, y1, x2, y2):
        self.container = [Object(x1, y1), Object(x2, y2)]
        self.size = width, height = 60, 30
        self.rotate_phase = 1

    def destruction(self):
        super().destruction()

    def draw(self, surface, position_1, position_2):
        # position - (start_x, start_y, width, height)
        pygame.draw.rect(surface, self.container[0].color, position_1)
        pygame.draw.rect(surface, self.container[1].color, position_2)

    def rotate(self):
        self.rotate_phase += 1
        if self.rotate_phase > 4: self.rotate_phase -=4

        if self.rotate_phase == 1:
            self.container[0].move_pos(0, 30)
            self.container[1].move_pos(30, 0)

        if self.rotate_phase == 2:
            self.container[1].move_pos(-30, -30)

        if self.rotate_phase == 3:
            self.container[0].move_pos(30, 0)
            self.container[1].move_pos(0, 30)

        if self.rotate_phase == 4:
            self.container[0].move_pos(-30, -30)

    def move_left(self):
        self.container[0].move_pos(-30, 0)
        self.container[1].move_pos(-30, 0)

    def move_right(self):
        self.container[0].move_pos(30, 0)
        self.container[1].move_pos(30, 0)

    def move_down(self):
        self.container[0].move_pos(0, 30)
        self.container[1].move_pos(0, 30)


class Virus(Object):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.pos = [x, y]
        self.size = width, height = 30, 30

    def destruction(self):
        global virus_amount
        virus_amount -= 1
        global points
        points += 200

    def draw(self, surface, position):
        pygame.draw.circle(surface, self.color, position, 15, 30)
        