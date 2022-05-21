from tkinter import *











ventana = Tk() #Se crea la ventana principal.
ventana.config(bg="black")
ventana.title("F1 Simulation") #Titulo de la pantalla principal. 
ventana.minsize(800,500) #Dimensiones de la pantalla.
ventana.resizable(width=NO,height=NO) #Que no se puede modificar. 
#fondo = cargarImagen("Fondo.gif") #Pone la imagen de fondo. 
#LabelFondo=Label(ventana, image=fondo) #Etiqueta que va a contener la imagen.
#LabelFondo.place (x=0, y=0) #Posición de la imagen.
menubar = Menu(ventana) #Se crea la barra del menú.
menubar.add_command(label="About") #Se crea el comando para que se dirija a la pantalla about.
menubar.add_command(label="Puntajes") #Se crea el comando para que se dirija a la pantalla scores.
ventana.config(menu=menubar) #Se posiciona la barra del menú.
ventana.mainloop() #El loop principal de toda la pantalla principal.