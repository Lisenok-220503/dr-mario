import pygame
import random
from classes import Virus

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
    
    def start_spawn(self):
        for i in range(6):
            self.virus = Virus()
    
        
    