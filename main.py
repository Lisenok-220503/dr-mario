import pygame
from board import Board
from classes import Background

pygame.init()

total_width = 900
total_height = 650

pygame.mixer.music.load("music.mp3") 
pygame.mixer.music.play(-1,0.0)

clock = pygame.time.Clock()

BackGround = Background('background_image.png', [0,0])


running = True

def init_window():
    pygame.init()
    screen1 = pygame.display.set_mode((total_width, total_heigth))
    pygame.display.set_caption('Dr Mario')
    
    
while running:
    for i in pygame.event.get:
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.K_RETURN:
            Board()
    
    
    screen.fill([255, 255, 255]) 
    screen.blit(BackGround.image, BackGround.rect) # позволяет отображать изображение под всеми спрайтами и клетчатым полем   
            