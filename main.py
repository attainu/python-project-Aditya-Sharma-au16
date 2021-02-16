import sys
import pygame

pygame.init()

width = 500
height = 450

colour = 120, 180, 198

screen = pygame.display.set_mode((width, height))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()


    screen.fill(colour)

    pygame.display.flip()