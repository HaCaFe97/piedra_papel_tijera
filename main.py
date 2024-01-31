import tkinter as tk
from formatos_textos import estilos_T1, estilos_T2, estilos_T3, estilos_T4, estilos_T5
from PIL import Image, ImageTk

#Caracteristicas de Ventana
ventana1 = tk.Tk()
ventana1.title("Piedra, Papel o Tijera")

#Imágenes de los botones
piedra = Image.open("Piedra.png")
papel = Image.open("Papel.png")
tijera = Image.open("Tijera.png")

piedra = piedra.resize((150, 221))
papel = papel.resize((150, 221))
tijera = tijera.resize((150, 221))

piedra_tk = ImageTk.PhotoImage(piedra)
papel_tk = ImageTk.PhotoImage(papel)
tijera_tk = ImageTk.PhotoImage(tijera)

#Textos en la ventana
titulo = tk.Label(ventana1, estilos_T1)
titulo.pack(pady=0)

etiqueta1 = tk.Label(ventana1, estilos_T2)
etiqueta1.pack(pady=0)

etiqueta2 = tk.Label(ventana1, estilos_T3)
etiqueta2.pack(pady=0)

etiqueta3 = tk.Label(ventana1, estilos_T4)
etiqueta3.pack(pady=0)

etiqueta4= tk.Label(ventana1, estilos_T5)
etiqueta4.pack(side="bottom", pady=0)

#Frame para botones
frame_botones = tk.Frame(ventana1)
frame_botones.pack(expand=True)

#Botón
boton1 = tk.Button(frame_botones, image=piedra_tk,text="Piedra")
boton1.pack(side="left", padx=(0, 5), pady=0)

boton2 = tk.Button(frame_botones,image=papel_tk, text="Papel")
boton2.pack(side="left", padx=(0, 5), pady=0)

boton3 = tk.Button(frame_botones,image=tijera_tk, text="Tijera")
boton3.pack(side="left", padx=(0, 5), pady=0)

#Loop de ejecución de ventana
ventana1.mainloop()