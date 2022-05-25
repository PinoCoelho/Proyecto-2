import pygame
import sys


pygame.init()
dimensiones = (800,500)
screen = pygame.display.set_mode(dimensiones)
pygame.display.set_caption("El Juego de los Barquitos :D")

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


