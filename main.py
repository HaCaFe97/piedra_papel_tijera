import tkinter as tk
from PIL import Image, ImageTk
from formatos_textos import estilos_T1, estilos_T2, estilos_T3, estilos_T4, estilos_T5, estilos_T6, estilos_T7, estilos_T8, estilos_T9, estilos_T10, estilos_T11, estilos_T12
from funciones import correr_juego

def game_start():
  correr_juego()
  boton_inicio.config(text="Juego Iniciado")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Piedra, Papel o Tijera")

#Imágenes de los botones
piedra = Image.open("Piedra.png")
papel = Image.open("Papel.png")
tijera = Image.open("Tijera.png")

piedra = piedra.resize((75, 75))
papel = papel.resize((75, 75))
tijera = tijera.resize((75, 75))

piedra_tk = ImageTk.PhotoImage(piedra)
papel_tk = ImageTk.PhotoImage(papel)
tijera_tk = ImageTk.PhotoImage(tijera)

#Grid Maestro (_filas_columnas)
grid_titulos = tk.Label(ventana)
grid_titulos.grid(row=0, column=1)

grid_juego = tk.Label(ventana)
grid_juego.grid(row=1, column=1)

grid_firma = tk.Label(ventana)
grid_firma.grid(row=2, column=1)

# Interior grid_titulos
titulo_lv1 = tk.Frame(grid_titulos)
tk.Label(titulo_lv1, estilos_T1).grid(row=0, column=0)
titulo_lv1.grid(row=0, column=0)

titulo_lv2 = tk.Frame(grid_titulos)
tk.Label(titulo_lv2, estilos_T2).grid(row=0, column=0)
titulo_lv2.grid(row=1, column=0)

titulo_lv3 = tk.Frame(grid_titulos)
tk.Label(titulo_lv3, estilos_T3).grid(row=0, column=0)
titulo_lv3.grid(row=2, column=0)

# Interior grid_juego
hud_jugador = tk.Frame(grid_juego)
hud_jugador.grid(row=0, column=0)

hud_rondas = tk.Frame(grid_juego)
hud_rondas.grid(row=0, column=1)

hud_computadora = tk.Frame(grid_juego)
hud_computadora.grid(row=0, column=2)

# Grid del hud del jugador

mensaje_jugador = tk.Frame(hud_jugador)
tk.Label(mensaje_jugador, estilos_T4).grid(row=0, column=0)
mensaje_jugador.grid(row=0, column=0)

botones_jugador = tk.Frame(hud_jugador)
botones_jugador.grid(row=1, column=0)

boton_piedra = tk.Button(botones_jugador, image=piedra_tk)
boton_piedra.grid(row=0, column=1)

boton_papel = tk.Button(botones_jugador, image=papel_tk)
boton_papel.grid(row=0, column=2)

boton_tijera = tk.Button(botones_jugador, image=tijera_tk)
boton_tijera.grid(row=0, column=3)

victorias_jugador = tk.Frame(hud_jugador)
victorias_jugador.grid(row=2, column=0)

texto_vic_jugador = tk.Frame(victorias_jugador)
tk.Label(texto_vic_jugador, estilos_T10).grid(row=0, column=1)
texto_vic_jugador.grid(row=0, column=0)

contador_vic_jugador = tk.Frame(victorias_jugador)
tk.Label(contador_vic_jugador, text="0", font=('Times New Roman', 12 ,'bold')).grid(row=0, column=1)
contador_vic_jugador.grid(row=0, column=1)

#Grid del hud de las rondas

boton_inicio = tk.Button(hud_rondas, text="Iniciar", command=correr_juego)
boton_inicio.grid(row=0, column=0, pady=5)

mensaje_rondas = tk.Frame(hud_rondas)
tk.Label(mensaje_rondas, estilos_T5).grid(row=0, column=0)
mensaje_rondas.grid(row=1, column=0)

contador_rondas = tk.Frame(hud_rondas)
tk.Label(contador_rondas, text="0", font=('Times New Roman', 12 ,'bold')).grid(row=0, column=0)
contador_rondas.grid(row=2, column=0)

info_partida = tk.Frame(hud_rondas)
info_partida.grid(row=3, column=0)

eleccion_jugador = tk.Frame(info_partida)
tk.Label(eleccion_jugador, estilos_T7, borderwidth=2, relief="groove").grid(row=0, column=0)
eleccion_jugador.grid(row=0, column=0, padx=5)

eleccion_jugador_dec = tk.Frame(info_partida)
tk.Label(eleccion_jugador_dec, text="piedrapapeltijera").grid(row=0, column=0)
eleccion_jugador_dec.grid(row=1, column=0)

ganador_ronda = tk.Frame(info_partida)
tk.Label(ganador_ronda, estilos_T8, borderwidth=2, relief="groove").grid(row=0, column=0)
ganador_ronda.grid(row=0, column=1, padx=5)

ganado_declarado = tk.Frame(info_partida)
tk.Label(ganado_declarado, text="Ganador").grid(row=0, column=0)
ganado_declarado.grid(row=1, column=1)

eleccion_computadora = tk.Frame(info_partida)
tk.Label(eleccion_computadora, estilos_T9, borderwidth=2, relief="groove").grid(row=0, column=0)
eleccion_computadora.grid(row=0, column=2, padx=5)

eleccion_computadora_dec = tk.Frame(info_partida)
tk.Label(eleccion_computadora_dec, text="piedrapapeltijera").grid(row=0, column=0)
eleccion_computadora_dec.grid(row=1, column=2)

boton_reiniciar = tk.Button(hud_rondas, text="Reiniciar")
boton_reiniciar.grid(row=4, column=0, pady=5)

# Grid del hud de la computadora

mensaje_computadora = tk.Frame(hud_computadora)
tk.Label(mensaje_computadora, estilos_T6).grid(row=0, column=0)
mensaje_computadora.grid(row=0, column=0)

botones_computadora = tk.Frame(hud_computadora)
botones_computadora.grid(row=1, column=0)

boton_piedra = tk.Button(botones_computadora, image=piedra_tk)
boton_piedra.grid(row=0, column=1)

boton_papel = tk.Button(botones_computadora, image=papel_tk)
boton_papel.grid(row=0, column=2)

boton_tijera = tk.Button(botones_computadora, image=tijera_tk)
boton_tijera.grid(row=0, column=3)

victorias_computadora = tk.Frame(hud_computadora)
victorias_computadora.grid(row=2, column=0)

texto_vic_computadora = tk.Frame(victorias_computadora)
tk.Label(texto_vic_computadora, estilos_T11).grid(row=0, column=1)
texto_vic_computadora.grid(row=0, column=0)

contador_vic_computadora = tk.Frame(victorias_computadora)
tk.Label(contador_vic_computadora, text="0", font=('Times New Roman', 12 ,'bold')).grid(row=0, column=1)
contador_vic_computadora.grid(row=0, column=1)

#Interior grid_firma
firma= tk.Label(grid_firma, estilos_T12)
firma.grid(row=0, column=0)

# Iniciar el bucle principal
ventana.mainloop()
