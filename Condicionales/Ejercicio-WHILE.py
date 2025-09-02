import random

# Opciones válidas
opciones = ["piedra", "papel", "tijera"]

# Marcadores
jugador_gana = 0
computadora_gana = 0

print(" Bienvenido al juego Piedra, Papel o Tijera contra la computadora")
print("Escribí 'salir' para terminar el juego.\n")

while True:
    # Menú de opciones
    print("Elige una opción:")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")
    print("Escribí tu elección (o 'salir' para terminar):")
    
    jugador = input(" ---> ").lower()
    
    if jugador == "salir":
        break
    if jugador not in opciones:
        print(" Opción inválida. Intentá de nuevo.\n")
        continue

    computadora = random.choice(opciones)
    print(f" La computadora eligió: {computadora}")

    # Comparación de jugadas
    if jugador == computadora:
        print(" ¡Empate!\n")
    elif (jugador == "piedra" and computadora == "tijera") or \
         (jugador == "tijera" and computadora == "papel") or \
         (jugador == "papel" and computadora == "piedra"):
        print(" ¡Ganaste esta ronda!\n")
        jugador_gana += 1
    else:
        print(" La computadora gana esta ronda.\n")
        computadora_gana += 1

# Resultado final
print(" Juego terminado.")
print(f"Marcador final: Jugador {jugador_gana} - Computadora {computadora_gana}")
if jugador_gana > computadora_gana:
    print(" ¡Felicitaciones, ganaste el juego!")
elif jugador_gana < computadora_gana:
    print(" La computadora ganó esta vez.")
else:
    print(" ¡Empate total!")
