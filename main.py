import tkinter as tk
from PIL import Image, ImageTk
from formatos_textos import estilos_T1, estilos_T2, estilos_T3, estilos_T4, estilos_T5, estilos_T6, estilos_T7, estilos_T8, estilos_T9

#Ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

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

# Grid Maestro (_filas_columnas))
grid_1_2 = tk.Label(ventana)
grid_1_2.grid(row=1, column=2)

grid_2_2 = tk.Label(ventana)
grid_2_2.grid(row=2, column=2)

grid_3_2 = tk.Label(ventana)
grid_3_2.grid(row=3, column=2)

# Interior del grid_1_2
titulo_lv1 = tk.Frame(grid_1_2)
tk.Label(titulo_lv1, estilos_T1).grid(row=0, column=0)
titulo_lv1.grid(row=0, column=0)

titulo_lv2 = tk.Frame(grid_1_2)
tk.Label(titulo_lv2, estilos_T2).grid(row=0, column=0)
titulo_lv2.grid(row=1, column=0)

titulo_lv3 = tk.Frame(grid_1_2)
tk.Label(titulo_lv3, estilos_T3).grid(row=0, column=0)
titulo_lv3.grid(row=2, column=0)

texto_std = tk.Frame(grid_1_2)
tk.Label(texto_std, estilos_T4).grid(row=0, column=0)
texto_std.grid(row=3, column=0)

#Interior del grid_2_2

victorias_jugador = tk.Frame(grid_2_2)
victorias_jugador.grid(row=0, column=0)

boton_piedra = tk.Button(grid_2_2, image=piedra_tk)
boton_piedra.grid(row=0, column=1)

boton_papel = tk.Button(grid_2_2, image=papel_tk)
boton_papel.grid(row=0, column=2)

boton_tijera = tk.Button(grid_2_2, image=tijera_tk)
boton_tijera.grid(row=0, column=3)

victorias_computadora = tk.Frame(grid_2_2)
victorias_computadora.grid(row=0, column=4)

#Grid en el grid en el grid

texto_jugador = tk.Frame(victorias_jugador)
tk.Label(texto_jugador, estilos_T6).grid(row=0, column=0)
texto_jugador.grid(row=0, column=0)

contador_jugador = tk.Frame(victorias_jugador)
tk.Label(contador_jugador, estilos_T8).grid(row=0,column=0)
contador_jugador.grid(row=1, column=0)

texto_computadora = tk.Frame(victorias_computadora)
tk.Label(texto_computadora, estilos_T7).grid(row=0, column=0)
texto_computadora.grid(row=0, column=0)

contador_computadora = tk.Frame(victorias_computadora)
tk.Label(contador_computadora, estilos_T9).grid(row=0, column=0)
contador_computadora.grid(row=1, column=0)

#Interior del grid_3_2

firma= tk.Label(grid_3_2, estilos_T5)
firma.grid(row=0, column=0)

# Iniciar el bucle principal de la ventana
ventana.mainloop()