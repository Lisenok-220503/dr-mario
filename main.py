import pygame
from board import Board

total_width = 900
total_height = 650

def init_window():
    pygame.init()
    screen1 = pygame.display.set_mode((total_width, total_heigth))
    pygame.display.set_caption('Dr Mario')

clock = pygame.time.Clock()

running = True

while running:
    for i in pygame.event.get:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_RETURN:
            Board()
            