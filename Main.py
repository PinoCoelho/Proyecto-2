from pickle import FROZENSET
import pygame
import sys
import json
import csv
from Prueba import *


###############################################################################################################################
#Parte de toda la pantalla

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("BATTLESHIP")

fondo = pygame.image.load("Images\Fondo.jpg")

icono = pygame.image.load("Images\Fondo.jpg")
pygame.display.set_icon(icono)

#################################################################################################################################

#Obtener la fuente de la letra

def get_font(size): 
    return pygame.font.Font("Images/font.ttf", size)

#################################################################################################################################

#Ventana del botón Play

  #De la clase Input 
COLOR_INACTIVE = pygame.Color('green')
COLOR_ACTIVE = pygame.Color('#FFFF66')
FONT = get_font(27)

def play():

    #Input:

    clock = pygame.time.Clock()
    input_box1 = InputBox(350, 100, 140, 32)
    input_box2 = InputBox(350, 300, 140, 32)
    input_boxes = [input_box1, input_box2]

    #Text:

    text = FONT.render('INSERTE SU NOMBRE', True, "green", "black")
    textRect = text.get_rect()
    textRect.center = (460,50)

    text2 = FONT.render('CANTIDAD DE NAVES', True, "green", "black")
    textRect2 = text2.get_rect()
    textRect2.center = (460,250)

    while True:
        screen.blit(fondo,(0,0))

        play_mouse_pos = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(450, 530), 
                            text_input="BACK", font=get_font(40), base_color="#FFFF66", hovering_color="Green")
        PLAY_BACK.changeColor(play_mouse_pos)
        PLAY_BACK.update(screen)

        PLAY_ACCEPT = Button(image=None, pos=(450, 400), 
                            text_input="ACEPTAR", font=get_font(40), base_color="#FFFF66", hovering_color="Green")
        PLAY_ACCEPT.changeColor(play_mouse_pos)
        PLAY_ACCEPT.update(screen)
        
        screen.blit(text, textRect)
        screen.blit(text2, textRect2)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(play_mouse_pos):
                    main_menu()
                if PLAY_ACCEPT.checkForInput(play_mouse_pos):
                    main()
            for box in input_boxes:
                box.handle_event(event)

        for box in input_boxes:
            box.update()

        
        for box in input_boxes:
            box.draw(screen)
        
        clock.tick(30)
        pygame.display.update()

######################################################################################################################################

#Ventana del botón Score

def score():

    while True:
        screen.blit(fondo,(0,0))

        score_mouse_pos = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=pygame.image.load("Images\Play Rect.png"), pos=(450, 500), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(score_mouse_pos)
        PLAY_BACK.update(screen)

        datos = {}
        datos["lider"] = []
        lista = []
        puntos = []
        with open("puntajeJugadores.csv", newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if len(row) > 0:
                    if row[0] != "":
                        puntos.append([row[0], row[1]])
        for lis in lista:
            for row in puntos:
                if len(row) > 0:
                    if int(row[1]) == lis:
                        datos["lider"].append({"Jugador": row[0], "Puntuacion": row[1]})
                        
        with open("archivojson.json") as lider:
            high = json.load(lider)
            contador = 0
            for h in high:
                if contador < 5:
                    score = get_font(20).render(h["Jugador"] + ": Puntuacion ---> " + h["Puntuacion"],True,"green")
                    score_rect = score.get_rect(center=(500, 100))
                    screen.blit (score,score_rect)
                contador = contador + 1  
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(score_mouse_pos):
                    main_menu()
        pygame.display.update()


def help():
    while True:
        screen.blit(fondo,(0,0))

        help_mouse_pos = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=pygame.image.load("Images\Play Rect.png"), pos=(450, 500), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(help_mouse_pos)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(help_mouse_pos):
                    main_menu()
        pygame.display.update()



##########################################################################################################################################

#Ventana del menú principal

def main_menu ():
    while True:
        screen.blit(fondo,(0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(40).render("MAIN MENU", True, "green")
        menu_rect = menu_text.get_rect(center=(450, 100))
        
        #Color anterior (#d7fcd4)
        PLAY_BUTTON = Button(image=pygame.image.load("Images\Play Rect.png"), pos=(450, 200), 
                            text_input="JUGAR", font=get_font(40), base_color="#FFFF66", hovering_color="green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Images\Options Rect.png"), pos=(450, 350), 
                            text_input="PUNTAJES", font=get_font(40), base_color="#FFFF66", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("Images\Quit Rect.png"), pos=(450, 500), 
                            text_input="AYUDA", font=get_font(40), base_color="#FFFF66", hovering_color="green")

        screen.blit(menu_text,menu_rect)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(menu_mouse_pos)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(menu_mouse_pos):
                    play()
                if OPTIONS_BUTTON.checkForInput(menu_mouse_pos):
                    score()
                if QUIT_BUTTON.checkForInput(menu_mouse_pos):
                    help()
        pygame.display.update()

#################################################################################################################################################

#La clase de los botones

class Button():
	def __init__(self, image, pos, text_input, font, base_color, hovering_color):
		self.image = image
		self.x_pos = pos[0]
		self.y_pos = pos[1]
		self.font = font
		self.base_color, self.hovering_color = base_color, hovering_color
		self.text_input = text_input
		self.text = self.font.render(self.text_input, True, self.base_color)
		if self.image is None:
			self.image = self.text
		self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
		self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

	def update(self, screen):
		if self.image is not None:
			screen.blit(self.image, self.rect)
		screen.blit(self.text, self.text_rect)

	def checkForInput(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			return True
		return False

	def changeColor(self, position):
		if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
			self.text = self.font.render(self.text_input, True, self.hovering_color)
		else:
			self.text = self.font.render(self.text_input, True, self.base_color)

#################################################################################################################################################            

#La clase del input
def Tiempo_User (self,tiempo, usuario):
    archivo.SaveScores(self,minute=tiempo,user=usuario)

class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    #print(self.text)
                    #with open ("nombres.json","w",newline='') as f:
                        #json.dump(self.text, f)
                    Tiempo_User(self,45,self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width
        
        
    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

##################################################################################################################################################

class archivo:

    def __init__(self):
        pass

    def SaveScores(self, minute,user):
        self.user = user
        self.tiempo = minute
        self.lista = []
        with open("puntajeJugadores.csv", newline='') as File:
            reader = csv.reader(File)
            self.lista.append([self.user,self.tiempo])
            for row in reader:
                if len(row) > 0:
                    if self.user != row[0]:
                        self.lista.append(row)
        writer = csv.writer(open('puntajeJugadores.csv', 'w'), delimiter=",")
        writer.writerows(self.lista) 

    def LoadScores(self, user):
        self.user = user
        with open("puntajeJugadores.csv", newline='') as File:
            reader = csv.reader(File)
            for row in reader:
                if len(row) > 0:
                    if self.user == row[0]:
                        self.puntuacionAlta = int(row[1])
                        self.puntos = int(row[2])
                        if 1 == 1:
                            self.puntos = 0
                        else:
                            self.puntos = int(row[2])

#Llama a la función main_menu de primero


if __name__ == "__main__": 
    main_menu()