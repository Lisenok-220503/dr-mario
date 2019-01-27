# *-* encoding=utf8 *-*
# https://www.pygame.org/docs/ref/key.html
import pygame
from board import Board
from classes import Background


total_width = 900
total_height = 650

music = pygame.mixer.music.load("fever.mp3")
pygame.mixer.music.play(-1, 0.0)

clock = pygame.time.Clock()

# Каждые полторы секунды пилюля автоматически опускается.
# Для этого создаю свой ивент.
# В главной переменной я хз, что забивать. Пусть будет как в примере. 	¯\_(ツ)_/¯

BackGround = Background('background.jpg', [0,0])

running = True
game = False

class game:
    def __init__(self):
        self.board = Board()
        pygame.init()

        self.fpsClock = pygame.time.Clock()
        self.screen1 = pygame.display.set_mode((total_width, total_height))
        pygame.display.set_caption('Dr Mario')
        
        self.time_event = 30
        pygame.time.set_timer(self.time_event, 1500)        

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

            if (event.type == pygame.K_DOWN or event.type == time_event) and game:
                board.move_down()
        board.check()
        #board.render()
        screen1.blit(BackGround.image, BackGround.rect)
        pygame.display.flip()


pygame.quit()
