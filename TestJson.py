import json,csv
import pygame

"""
with open("archivojson.json") as lider:
            high = json.load(lider)
            contador = 0
            for h in high:
                if contador < 5:
                    score = get_font(20).render(h["Jugador"] + ": Puntuacion ---> " + h["Puntuacion"],True,"green")
                    score_rect = score.get_rect(center=(500, 100))
                    screen.blit (score,score_rect)
                contador = contador + 1

def Tiempo_User (self,tiempo, usuario):
    archivo.SaveScores(self,minute=tiempo,user=usuario)

"""

import pygame
import sys

pygame.init()

window = pygame.display.set_mode((900,600))
pygame.display.set_caption("BATTLESHIP")
BG = pygame.image.load("Images\Fondo.jpg")

done = False
secs = 0
mins = 0
hours = 0

font = pygame.font.Font("freesansbold.ttf",32)
text = font.render("{}:{}:{}".format(hours,mins,secs),True,(255,255,255),(0,0,0))
textRect = text.get_rect()
textRect.center = 500//2,500//2

clock = pygame.time.Clock()

while not done:
    clock.tick(1)
    secs += 1
    window.blit(text,textRect)
    if secs == 60:
        secs = 0
        mins += 1
    if mins == 60:
        mins = 0
        secs = 0
        hours == 1
    text = font.render("{}:{}:{}".format(hours,mins,secs),True,(255,255,255),(0,0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    pygame.display.update()