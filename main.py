# *-* encoding=utf8 *-*
# https://www.pygame.org/docs/ref/key.html
import pygame
from board import Board
from classes import Background
import os

pygame.init()

total_width = 900
total_height = 650

music = pygame.mixer.music.load("fever.mp3")
pygame.mixer.music.play(-1, 0.0)

clock = pygame.time.Clock()


running = True

BackGround = Background('background.jpg', [0,0])

pygame.init()
screen1 = pygame.display.set_mode((total_width, total_height))
pygame.display.set_caption('Dr Mario')
game = False
while running:
    screen1.fill([255, 255, 255])
    screen1.blit(BackGround.image, BackGround.rect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_RETURN:
            board = Board()
            game = True
        if event.type == pygame.K_SPACE and game:
            board.rotate()

        if event.type == pygame.K_RIGHT and game:
            board.move_right()

        if event.type == pygame.K_LEFT and game:
            board.move_left()

        if event.type == pygame.K_DOWN and game:
            board.move_down()
    screen1.blit(BackGround.image, BackGround.rect)
    pygame.display.flip()


pygame.quit()
