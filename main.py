# *-* encoding=utf8 *-*
import pygame
import os
from board import Board
from classes import Background
pygame.init()

total_width = 900
total_height = 650

pygame.mixer.music.load("fever.mp3")
pygame.mixer.music.play(-1, 0.0)

clock = pygame.time.Clock()

BackGround = Background('background.jpg', [0,0])


running = True


pygame.init()
screen1 = pygame.display.set_mode((total_width, total_height))
pygame.display.set_caption('Dr Mario')

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_RETURN:
            Board()
    
    
    screen1.fill([255, 255, 255])
    screen1.blit(BackGround.image, BackGround.rect)

pygame.quit()
