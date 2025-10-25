
tablero = [" " for _ in range(9)]
jugador = "X"
print()#Mostrar el tablero
print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
print("--+---+---")
print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
print("--+---+---")
print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
print()

for turno in range (9):
    posicion = input(f"Jugaor {jugador}, selecciona una posición (1-9): ")

    while not posicion.isdigit() or int(posicion) < 1 or int(posicion) > 9 or tablero[int(posicion)-1] != " ":
        posicion = input("Posición no válida. Elige otra (1-9): ")

    posicion =  int(posicion) - 1    
    tablero[posicion] = jugador

    print()
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+--")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+--")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print()

#Comprobamos el ganador poniendo todas las posibles combinaciones para ganar
    if (tablero[0] == tablero[1] == tablero[2] != " ") or \
       (tablero[3] == tablero[4] == tablero[5] != " ") or \
       (tablero[6] == tablero[7] == tablero[8] != " ") or \
       (tablero[0] == tablero[3] == tablero[6] != " ") or \
       (tablero[1] == tablero[4] == tablero[7] != " ") or \
       (tablero[2] == tablero[5] == tablero[8] != " ") or \
       (tablero[0] == tablero[4] == tablero[8] != " ") or \
       (tablero[2] == tablero[4] == tablero[6] != " "):
        print(f"¡Jugador {jugador} ha ganado! ")
        break #Es importante romper para dar el ganador

    # Cambiar de jugador
    if jugador == "X":
        jugador = "O"
    else:
        jugador = "X"
else: # si no se cumple ningun posible ganador se dá empate
    print("¡Empate!")   