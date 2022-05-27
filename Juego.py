import pygame
import sys

pygame.init()

window = pygame.display.set_mode((900,600))
pygame.display.set_caption("BATTLESHIP")
BG = pygame.image.load("Proyecto 2\Proyecto-2\Images\Fondo.jpg")

def main ():
    while True:
        window.blit(BG,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()