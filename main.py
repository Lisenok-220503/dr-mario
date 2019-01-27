# *-* encoding=utf8 *-*
# https://www.pygame.org/docs/ref/key.html
import pygame
from board import Board
from classes import Background


total_width = 900
total_height = 650

# Каждые полторы секунды пилюля автоматически опускается.
# Для этого создаю свой ивент.
# В главной переменной я хз, что забивать. Пусть будет как в примере. 	¯\_(ツ)_/¯


running = True
game = False

class game:
    def __init__(self):
        pygame.init()
        
        self.music = pygame.mixer.music.load("fever.mp3")
        pygame.mixer.music.play(-1, 0.0)
        
        self.BackGround = Background('background.jpg', [0,0])
        
        clock = pygame.time.Clock()

        self.fpsClock = pygame.time.Clock()
        self.screen1 = pygame.display.set_mode((total_width, total_height))
        pygame.display.set_caption('Dr Mario')
        
        self.time_event = 30
        pygame.time.set_timer(self.time_event, 1500)        

    while running:
        self.screen1.fill([255, 255, 255])
        self.screen1.blit(BackGround.image, BackGround.rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.K_RETURN:
                self.board = Board()
                game = True
            if event.type == pygame.K_SPACE and game:
                self.board.rotate()

            if event.type == pygame.K_RIGHT and game:
                self.board.move_right()

            if event.type == pygame.K_LEFT and game:
                self.board.move_left()

            if (event.type == pygame.K_DOWN or event.type == time_event) and game:
                self.board.move_down()
        self.board.check()
        #board.render()
        self.screen1.blit(self.BackGround.image, self.BackGround.rect)
        pygame.display.flip()


pygame.quit()
