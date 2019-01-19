import pygame
from board import Board

window_size = total_width, total_height = 900, 650

def init_window():
    pygame.init()
    screen1 = pygame.display.set_mode(window_size)
    pygame.display.set_caption('Dr Mario')

clock = pygame.time.Clock()

running = True

while running:
    for i in pygame.event.get:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_RETURN:
            Board()
            