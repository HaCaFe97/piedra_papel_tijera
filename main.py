import tkinter as tk
from formatos_textos import estilos_T1, estilos_T2, estilos_T3, estilos_T4, estilos_T5

#Caracteristicas de Ventana
ventana1 = tk.Tk()
ventana1.state("zoomed")
ventana1.title("Piedra, Papel o Tijera")

#Titutlo del programa en label
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

#Botones
boton1 = tk.Button(ventana1, text="Haz clic aquí")
boton1["command"] = lambda: etiqueta1.config(text='Este botón funciona')
boton1.pack(pady=0)

#Loop de ejecución de ventana
ventana1.mainloop()