from engine import Player  

import pygame 
import random


pygame.init()
pygame.display.set_caption("Battle Ship")

#GLOBAL VARIABLES
SQ_SIZE = 45 
H_MARGIN = SQ_SIZE * 4 
V_MARGIN = SQ_SIZE 

WIDTH = SQ_SIZE * 5 * 4 + H_MARGIN
HEIGHT = SQ_SIZE * 5 * 3 +V_MARGIN
INDENT = 10 
#WIDTH = 1000
#HEIGHT=600
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
GREEN = (50,200, 150) 
#COLORS 
GREY = (40,50,60)
WHITE=(255, 250, 250)


#FUNCTION TO DRAW A GRID 
def draw_grid(left=0,top=0):
    for i in range(100):
        x = left +i % 10 * SQ_SIZE 
        y = top + i // 10 * SQ_SIZE 
        square = pygame.Rect(x , y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width=3)



player = Player() 
#function to draw ships onto the possition grids 
def draw_ships(player,left = 0, top = 0):
    for ship in player.ships:
        x = left + ship.col * SQ_SIZE + INDENT 
        y = top + ship.row * SQ_SIZE + INDENT 
        if ship.orientation == "h":
            width = ship.size * SQ_SIZE - 2 * INDENT  
            height = SQ_SIZE - 2 * INDENT 
        else:
            width = SQ_SIZE - 2 * INDENT 
            height = ship.size * SQ_SIZE - 2 * INDENT 
        rectangle = pygame.Rect(x, y, width, height)
        pygame.draw.rect(SCREEN, GREEN, rectangle, border_radius=15)


#pygame loop 


animation = True
pause = False 
while animation:

    #track user 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animation == False
            quit() 

    #USER PRESSES KEY ON KEYBOARD 
        if event.type == pygame.KEYDOWN:
            #ESCAPE KEY TO CLOSE THE ANIMATION 
            if event.key == pygame.K_ESCAPE:
                animation = False 
            #SPACE BAR TO PAUSE AND UNPAUSE THE ANIMATON 
            if event.key == pygame.K_SPACE:
               pause = not pause
        #execution 
    if not pause: 

        #draw BK
        SCREEN.fill(GREY)


        #draw search grids
        draw_grid()
        draw_grid(left =(WIDTH-H_MARGIN) // 2 + H_MARGIN)
        #draw_grid(left =100, top=60)  #top an dleft is the location
        #draw_grid(left = 600, top=60)

        # draw ships onto position grids 
        draw_ships(player)


        pygame.display.flip()
        
        
