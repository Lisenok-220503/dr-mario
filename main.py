import pygame
from board import board

size = width, height = 600, 450
screen1 = pygame.display.set_mode(size)
clock = pygame.time.Clock()

running = True

while running:
    for i in pygame.event.get:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_RETURN:
            board()
            