import tkinter as tk
import random

opciones = ["piedra", "papel", "tijera"]
victorias_jugador = 0
victorias_computadora = 0
ronda = 1

def iniciar_juego():
  btn_iniciar.config(state=tk.DISABLED)  # Deshabilitar el botón iniciar
  btn_piedra.config(state=tk.NORMAL)
  btn_papel.config(state=tk.NORMAL)
  btn_tijera.config(state=tk.NORMAL)

def correr_juego(seleccion_jugador):
  global victorias_jugador, victorias_computadora, ronda
  lbl_elec_jugador_def.config(text=seleccion_jugador)
  seleccion_computadora = random.choice(opciones)
  lbl_elec_computadora_def.config(text=seleccion_computadora)
  if seleccion_jugador == seleccion_computadora:
    lbl_ganador.config(text="Empate")
  elif (seleccion_jugador == "piedra" and seleccion_computadora == "tijera") or \
       (seleccion_jugador == "papel" and seleccion_computadora == "piedra") or \
       (seleccion_jugador == "tijera" and seleccion_computadora == "papel"):
    lbl_ganador.config(text="Jugador")
    victorias_jugador += 1
    lbl_contsvicjugador.config(text=victorias_jugador)
  else:
    lbl_ganador.config(text="Computadora")
    victorias_computadora += 1
    lbl_contsviccomputadora.config(text=victorias_computadora)
  ronda +=1
  lbl_cuentaronda.config(text=str(ronda))
  if victorias_jugador == 2:
    lbl_campeondef.config(text="Jugador")
    btn_piedra.config(state=tk.DISABLED)
    btn_papel.config(state=tk.DISABLED)
    btn_tijera.config(state=tk.DISABLED)
  elif victorias_computadora == 2:
    lbl_campeondef.config(text="Computadora")
    btn_piedra.config(state=tk.DISABLED)
    btn_papel.config(state=tk.DISABLED)
    btn_tijera.config(state=tk.DISABLED)

def reiniciar_juego():
  global victorias_jugador, victorias_computadora, ronda
  victorias_jugador = 0
  victorias_computadora = 0
  ronda = 1
  lbl_elec_jugador_def.config(text="")
  lbl_elec_computadora_def.config(text="")
  lbl_ganador.config(text="")
  lbl_cuentaronda.config(text="1")
  lbl_campeondef.config(text="")
  lbl_contsvicjugador.config(text=0)
  lbl_contsviccomputadora.config(text=0)
  btn_iniciar.config(state=tk.NORMAL)

# Crear la ventana principal
root = tk.Tk()
root.title("Piedra, Papel o Tijera")

# Cargar las imágenes
img_piedra = tk.PhotoImage(file="Piedra.png").subsample(6)
img_papel = tk.PhotoImage(file="Papel.png").subsample(6)
img_tijera = tk.PhotoImage(file="Tijera.png").subsample(6)

# Titulos
frame_titulos = tk.Frame(root)
frame_titulos.grid(row=0, column=1)

titulo_nv1 = tk.Label(frame_titulos, text="Piedra, Papel o Tijera")
titulo_nv1.grid(row=0, column=0)

titulo_nv2 = tk.Label(frame_titulos, text="Juega contra la computadora en un juego de piedra, papel o tijera")
titulo_nv2.grid(row=1, column=0)

titulo_nv3 = tk.Label(frame_titulos, text="Quien gane dos de tres rondas, gana el juego")
titulo_nv3.grid(row=2, column=0)

# Crear el frame para los botones del jugador
frame_jugador = tk.Frame(root)
frame_jugador.grid(row=1, column=0, padx=10, pady=10)

# Crear los botones para piedra, papel y tijera para el jugador
texto_jugador = tk.Frame(frame_jugador)
texto_jugador.grid(row=0, column=0, padx=5, pady=5)
lbl_jugador = tk.Label(texto_jugador, text="Elige una opción")
lbl_jugador.grid(row=0, column=0, padx=5, pady=5)

botones_jugador = tk.Frame(frame_jugador)
botones_jugador.grid(row=1, column=0, padx=5, pady=5)
btn_piedra = tk.Button(botones_jugador, image=img_piedra, state=tk.DISABLED, command=lambda: correr_juego("piedra"))
btn_piedra.grid(row=0, column=0, pady=5)
btn_papel = tk.Button(botones_jugador, image=img_papel, state=tk.DISABLED, command=lambda: correr_juego("papel"))
btn_papel.grid(row=0, column=1, pady=5)
btn_tijera = tk.Button(botones_jugador, image=img_tijera, state=tk.DISABLED, command=lambda: correr_juego("tijera"))
btn_tijera.grid(row=0, column=2, pady=5)

contadores_jugador = tk.Frame(frame_jugador)
contadores_jugador.grid(row=2, column=0, padx=5, pady=5)
lbl_vicsjugador = tk.Label(contadores_jugador, text="Victorias Jugador: ")
lbl_vicsjugador.grid(row=0, column=0, padx=5, pady=0)
lbl_contsvicjugador = tk.Label(contadores_jugador, text=victorias_jugador)
lbl_contsvicjugador.grid(row=0, column=1, padx=5, pady=0)


# Crear el frame para los botones de iniciar y reiniciar
frame_rondas = tk.Frame(root)
frame_rondas.grid(row=1, column=1, padx=10, pady=10)

# Crear los botones para iniciar y reiniciar
btn_iniciar = tk.Button(frame_rondas, text="Iniciar", command=iniciar_juego)
btn_iniciar.grid(row=0, column=0, pady=5)
lbl_ronda = tk.Label(frame_rondas, text="Ronda")
lbl_ronda.grid(row=1, column=0, pady=5)
lbl_cuentaronda = tk.Label(frame_rondas, text=ronda)
lbl_cuentaronda.grid(row=2, column=0, pady=5)

frame_info = tk.Frame(frame_rondas)
frame_info.grid(row=3, column=0, pady=5)

lbl_elec_jugador = tk.Label(frame_info, text="El jugador escogió")
lbl_elec_jugador.grid(row=0, column=0, padx=5, pady=5)
lbl_elec_jugador_def = tk.Label(frame_info, text="piedrapapeltijera")
lbl_elec_jugador_def.grid(row=1, column=0, padx=5, pady=5)

lbl_ganaronda = tk.Label(frame_info, text="Ganador de ronda")
lbl_ganaronda.grid(row=0, column=1, pady=5)
lbl_ganador = tk.Label(frame_info, text="Ganador")
lbl_ganador.grid(row=1, column=1, pady=5)

lbl_elec_computadora = tk.Label(frame_info, text="La computadora escogió")
lbl_elec_computadora.grid(row=0, column=2, padx=5, pady=5)
lbl_elec_computadora_def = tk.Label(frame_info, text="piedrapapeltijera")
lbl_elec_computadora_def.grid(row=1, column=2, padx=5, pady=5)

btn_reiniciar = tk.Button(frame_rondas, text="Reiniciar", command=reiniciar_juego)
btn_reiniciar.grid(row=4, column=0, pady=5)

# Crear el frame para la zona de la computadora
frame_computadora = tk.Frame(root)
frame_computadora.grid(row=1, column=2, padx=10, pady=10)

# Crear los labels para piedra, papel y tijera para la computadora
texto_computadora = tk.Frame(frame_computadora)
texto_computadora.grid(row=0, column=0, padx=5, pady=5)
lbl_computadora = tk.Label(texto_computadora, text="La computadora elegirá")
lbl_computadora.grid(row=0, column=0, padx=5, pady=5)

labels_computadora = tk.Frame(frame_computadora)
labels_computadora.grid(row=1, column=0, padx=5, pady=5)
lbl_piedra = tk.Label(labels_computadora, image=img_piedra)
lbl_piedra.grid(row=0, column=0, pady=5)
lbl_papel = tk.Label(labels_computadora, image=img_papel)
lbl_papel.grid(row=0, column=1, pady=5)
lbl_tijera = tk.Label(labels_computadora, image=img_tijera)
lbl_tijera.grid(row=0, column=2, pady=5)

contadores_computadora = tk.Frame(frame_computadora)
contadores_computadora.grid(row=2, column=0, padx=5, pady=5)
lbl_vicscomputadora = tk.Label(contadores_computadora, text="Victorias Computadora: ")
lbl_vicscomputadora.grid(row=0, column=0, padx=5, pady=0)
lbl_contsviccomputadora = tk.Label(contadores_computadora, text=victorias_computadora)
lbl_contsviccomputadora.grid(row=0, column=1, padx=5, pady=0)

#Mensaje de Victoria
lbl_campeon = tk.Frame(root)
lbl_campeon.grid(row=2, column=1, padx=0, pady=5)
lbl_campeontext = tk.Label(lbl_campeon, text="El ganador del juego es: ")
lbl_campeontext.grid(row=0, column=0, padx=0, pady=5)
lbl_campeondef = tk.Label(lbl_campeon, text="jugadorcomputadora")
lbl_campeondef.grid(row=1, column=0, padx=0, pady=5)

# Ejecutar el bucle principal de la ventana
root.mainloop()
