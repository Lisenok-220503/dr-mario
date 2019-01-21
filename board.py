import pygame
from random import randrange
from classes import Object, Virus, Pill

spawn_pos = (110, 0)
class Board:
    
    def __init__(self,  left, top):
        self.width = 250
        self.height = 450
        self.left = left
        self.top = top
        self.display = pygame.Surface((240, 450))
        self.board = []
        for h in range(0, 16):
            self.board.append([])
            for w in range(0, 9):
                self.board[h].append(Object(w, h))
        # self.left = 10
        # self.top = 10
        self.cell_size = 30
    
    def start_spawn_virus(self):
        self.virus_list = []
        for i in range(6):
            self.virus_list.append(Virus())
            self.virus.draw(self.display, (randrange(0, 241, 30), randrange(225, 451, 30)))
    
    def spawn_pill(self):
        pill = Pill()
        pill.draw(self.display, ((110, 0), (30, 30)), self.cell_size, self.cell_size)
        
    def move_pill(self):
        pass
    
    def rotate_pill(self):
        pass


pygame.quit()
