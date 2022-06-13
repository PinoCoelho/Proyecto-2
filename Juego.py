import pygame
import sys

pygame.init()

window = pygame.display.set_mode((900,600))
pygame.display.set_caption("BATTLESHIP")
BG = pygame.image.load("Images\Fondo.jpg")



def main ():

    counter,text = 0,'0'.rjust(1)
    pygame.time.set_timer(pygame.USEREVENT, 1000)
    font = pygame.font.SysFont('Consolas', 30)
    clock = pygame.time.Clock()
    while True:
        window.blit(BG,(0,0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        for e in pygame.event.get():
            if e.type == pygame.USEREVENT: 
                counter += 1
                text = str(counter).rjust(1)

        clock.tick(60)
        window.blit(font.render(text, True, (0, 0, 0)), (32, 48))
        pygame.display.update() 
main()