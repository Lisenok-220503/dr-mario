import pygame
from random import randrange
from classes import Object, Virus, Pill

spawn_pos = (110, 0)
class Board: # я решила переделать поле на клетки, ибо я просто не понимаю по другому, и мне кажется так будет проще. И я думаю, будет неплохо комбинировать работу с пикселями и с клетчатым полем, хз короче.
    # инициализация поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значени¤ по умолчанию
        self.left = 10
        self.top = 10
        self.cell_size = 30
 
    # настраеваем внешний вид
    def set_view(self, left, top, cell_size):
        self.left = left
        self.top = top
        self.cell_size = cell_size
    
    # прорисовываем поле
    def render(self):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left , y * self.cell_size
                    + self.top, self.cell_size, self.cell_size), 1)

    
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
        self.rotate()


pygame.quit()
