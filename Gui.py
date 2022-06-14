from engine import Game

import pygame 
import random


pygame.init()
pygame.font.init()
pygame.display.set_caption("BattleShip")
myfont = pygame.font.SysFont("freesans.ttf", 100)

SQ_SIZE = 45 
H_MARGIN = SQ_SIZE * 4 
V_MARGIN = SQ_SIZE 

WIDTH = SQ_SIZE * 10 * 2 + H_MARGIN
HEIGHT = SQ_SIZE * 10 * 2 + V_MARGIN
INDENT = 10 
SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
HUMAN1 = False
HUMAN2 = False
#WIDTH = 1000
#HEIGHT=600

#COLORES 
GREEN = (50,200, 150) 
GREY = (40,50,60)
WHITE=(255, 250, 250)
RED = (250, 50, 100)
ORANGE = (250, 140, 20)
BLUE = (50, 150, 200)

COLORS = {"U": GREY, "M": BLUE, "H": ORANGE, "S": RED }


#FUNCIÓN PARA DIBUJAR UNA CUADRICULA 
def draw_grid(player, left=0,top=0, search = False  ):
    for i in range(100):
        x = left + i % 10 * SQ_SIZE 
        y = top + i // 10 * SQ_SIZE 
        square = pygame.Rect(x , y, SQ_SIZE, SQ_SIZE)
        pygame.draw.rect(SCREEN, WHITE, square, width=3)
        if search:
            x += SQ_SIZE // 2 
            y += SQ_SIZE // 2 
            pygame.draw.circle(SCREEN, COLORS[player.search[i]], (x,y), radius = SQ_SIZE//4)

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


game = Game(HUMAN1, HUMAN2)

#pygame loop 
animation = True
pause = False 
while animation:

    #rastrear al usuario 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animation == False
            quit()
    
        #El usuario hace clic en el mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = pygame.mouse.get_pos()
            if not  game.over and game.player1_turn and x < SQ_SIZE * 10 and y < SQ_SIZE * 10:
                row = y // SQ_SIZE
                col = x // SQ_SIZE 
                index = row * 10 + col
                game.make_move(index)
            elif not game.over and not game.player1_turn and x > WIDTH - SQ_SIZE * 10 and y > SQ_SIZE * 10 + V_MARGIN:
                row = (y - SQ_SIZE * 10 - V_MARGIN) // SQ_SIZE
                col = (x - SQ_SIZE * 10 - H_MARGIN) // SQ_SIZE
                index = row * 10 + col
                game.make_move(index)

    #USUARIO PRESIONA TECLA EN TECLADO
        if event.type == pygame.KEYDOWN:
            #TECLA ESCAPE PARA CERRAR LA ANIMACIÓN 
            if event.key == pygame.K_ESCAPE:
                animation = False 
            #BARRA ESPACIADORA PARA PAUSAR Y DESPAUSAR LA ANIMACIÓN 
            if event.key == pygame.K_SPACE:
               pause = not pause
            # return key to restart the game
            if event.key == pygame.K_RETURN:
                game = Game(HUMAN1, HUMAN2)
        #ejecución 
    if not pause: 

        #Dibujar fondo
        SCREEN.fill(GREY)
        
        # draw search grids
        draw_grid (game.player1,search=True)
        draw_grid(game.player2,search= True, left = (WIDTH-H_MARGIN)//2+ H_MARGIN, top=(HEIGHT-V_MARGIN)//2+ V_MARGIN)

        #draw position grids
        draw_grid(game.player1,top = (HEIGHT-V_MARGIN)//2+ V_MARGIN)
        draw_grid(game.player2,left = (WIDTH-H_MARGIN)//2+ H_MARGIN)

        #draw ships onto position grids
        draw_ships(game.player1,top = (HEIGHT-V_MARGIN)//2+ V_MARGIN)
        draw_ships(game.player2,top = (HEIGHT-V_MARGIN)//2+ V_MARGIN)
        
        # computer moves
        if not game.over and game.computer_turn:
            game.random_ai ()

        # Mensaje cuando finaliza el juego
        if game.over:
            text = "Jugador " + str(game.result) + "Ganaste!"
            textbox = myfont.render(text,False,GREY,WHITE)
            SCREEN.blit(textbox,(WIDTH // 2 - 240, HEIGHT // 2 -50))

        pygame.time.wait(100)
        pygame.display.flip()