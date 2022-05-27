import pygame
import sys

###############################################################################################################################
#Parte de toda la pantalla

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((900,600))
pygame.display.set_caption("BATTLESHIP")

fondo = pygame.image.load("Proyecto 2\Proyecto-2\Images\Fondo.jpg")

icono = pygame.image.load("Proyecto 2\Proyecto-2\Images\Fondo.jpg")
pygame.display.set_icon(icono)

#################################################################################################################################

#Obtener la funte de la letra

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("Proyecto 2/Proyecto-2/Images/font.ttf", size)

#################################################################################################################################

#Ventana del botón Play

def play ():
    while True:
        screen.blit(fondo,(0,0))

        play_mouse_pos = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(450, 400), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(play_mouse_pos)
        PLAY_BACK.update(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(play_mouse_pos):
                    main_menu()
        pygame.display.update()

######################################################################################################################################

#Ventana del botón Score

def score ():
    while True:
        screen.blit(fondo,(0,0))

        score_mouse_pos = pygame.mouse.get_pos()

        PLAY_BACK = Button(image=None, pos=(450, 400), 
                            text_input="BACK", font=get_font(40), base_color="White", hovering_color="Green")
        PLAY_BACK.changeColor(score_mouse_pos)
        PLAY_BACK.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BACK.checkForInput(score_mouse_pos):
                    main_menu()
        pygame.display.update()

##########################################################################################################################################

#Ventana del menú principal

def main_menu ():
    while True:
        screen.blit(fondo,(0,0))

        menu_mouse_pos = pygame.mouse.get_pos()

        menu_text = get_font(40).render("MAIN MENU", True, "black")
        menu_rect = menu_text.get_rect(center=(450, 100))
        
        #Color anterior (#d7fcd4)
        PLAY_BUTTON = Button(image=pygame.image.load("Proyecto 2\Proyecto-2\Images\Play Rect.png"), pos=(450, 200), 
                            text_input="PLAY", font=get_font(40), base_color="#d7fcd4", hovering_color="green")
        OPTIONS_BUTTON = Button(image=pygame.image.load("Proyecto 2\Proyecto-2\Images\Options Rect.png"), pos=(450, 350), 
                            text_input="SCORES", font=get_font(40), base_color="White", hovering_color="green")
        QUIT_BUTTON = Button(image=pygame.image.load("Proyecto 2\Proyecto-2\Images\Quit Rect.png"), pos=(450, 500), 
                            text_input="QUIT", font=get_font(40), base_color="White", hovering_color="green")

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
                    pygame.quit()
                    sys.exit()
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

#####################################################################################################################################################

#Llama a la función main_menu para que se inicie de primero

main_menu()