import pygame
from random import randrange
from classes import Object, Virus, Pill

#spawn_pos = (110, 0)
class Board():
    def __init__(self, width, height, surface):
        self.width = width
        self.height = height
        self.board = [] # содержит в себе все недвигающееся объекты игры.
        # После столкновения с объектом, пилюля становится частью этого board
        self.left = 10
        self.top = 10
        self.cell_size = 30
        self.surface = surface
 
    #
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size

    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(self.surface, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left , y * self.cell_size
                    + self.top, self.cell_size, self.cell_size), 1)

    def start_spawn_virus(self):
        self.virus_list = []
        for i in range(6):
            self.virus_list.append(Virus())
            self.virus.draw(self.display, (randrange(0, 241, 30), randrange(225, 451, 30)))
    
    def spawn_pill(self):
        self.active_pill = Pill(self.start_pos[0], self.start_pos[1], self.start_pos[0] + 30, self.start_pos[1])
        self.active_pill.draw()
        
    def move_pill_left(self):
        self.active_pill.move_left()

    def move_pill_right(self):
        self.active_pill.move_right()

    def move_pill_down(self):
        self.active_pill.move_down()

    def rotate_pill(self):
        self.active_pill.rotate()

    def check_collision(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if i == j:
                    pass
                else:
                    temp_1 = self.board[i].get_pos()
                    temp_2 = self.board[j].get_pos()
                    if temp_1[0][0] == temp_2[0][0] or \
                       temp_1[1][0] == temp_2[0][0] or \
                       temp_1[0][0] == temp_2[1][0] or \
                       temp_1[1][0] == temp_2[1][0]:
                        return True

    def check_destruction(self):
        pass
#       for i in len(self.board):
#           for j in len(self.board):
#               if i == j:
# чет типо этого



pygame.quit()
