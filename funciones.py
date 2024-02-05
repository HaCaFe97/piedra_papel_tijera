def correr_juego():
  victorias_jugador = 0
  victorias_computadora = 0
  ronda = 1
  while True:

    ronda += 1

    if victorias_jugador == 2:
      print("El ganador es el ussuario")
      break

    if victorias_computadora == 2:
       print("El ganador es la computadora")
       break

