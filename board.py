import pygame
from random import randrange
from classes import Object, Virus, Pill

spawn_pos = (110, 0)
class Board:
    
    def __init__(self):
        self.width = 250
        self.height = 450
        self.display = pygame.Surface((240, 450))
        self.board = []
        for h in range(0, 16):
            self.board.append([])
            for w in range(0, 9):
                self.board[h].append(Object(w, h))
        #self.left = 10
        #self.top = 10
        #self.cell_size = 30
        
    
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    def start_spawn_virus(self):
        for i in range(6):
            self.virus = Virus()
            self.virus.draw(self.display, (randrange(0, 240), randrange(0, 225)))
    
    def spawn_pill(self):
        pill = Pill()
        pill.draw(self.display, ((110, 0), (30, 30)), self.size, self.size)
        
    
        
    