
# ----------------------------------------------------------------------
# FUNCIONES DEL JUEGO
# ----------------------------------------------------------------------

def mostrar_tablero(tablero):
    """Muestra el tablero de Tic-Tac-Toe en la consola."""
    print()
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+---")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+---")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print()

def obtener_movimiento(tablero, jugador):
    """Solicita al jugador una posición válida y la retorna ajustada al índice."""
    while True:
        # Pide la posición al jugador
        posicion = input(f"Jugaor {jugador}, selecciona una posición (1-9): ")

        # 1. Verificar si es un número
        if not posicion.isdigit():
            print("Entrada no válida. Por favor, ingresa un número del 1 al 9.")
            continue

        posicion_idx = int(posicion) - 1

        # 2. Verificar si está en el rango (0 a 8)
        if not (0 <= posicion_idx <= 8):
            print("Posición fuera de rango. Elige un número entre 1 y 9.")
            continue

        # 3. Verificar si la casilla está vacía
        if tablero[posicion_idx] != " ":
            print("Esa casilla ya está ocupada. Elige otra.")
            continue
        
        # Si todo es válido, retorna el índice (0-8)
        return posicion_idx

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador actual ha ganado."""
    
    # Definir todas las combinaciones ganadoras (filas, columnas, diagonales)
    combinaciones_ganadoras = [
        # Filas
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columnas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonales
        (0, 4, 8), (2, 4, 6)
    ]
    
    # Comprobar si alguna combinación tiene las 3 marcas del jugador
    for a, b, c in combinaciones_ganadoras:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
            
    return False

def jugar_tres_en_raya():
    """Función principal que ejecuta el juego de Tic-Tac-Toe."""
    
    # Inicialización
    tablero = [" "] * 9
    jugador = "X"
    mostrar_tablero(tablero)
    
    # Bucle principal del juego
    for turno in range(9):
        
        # 1. Obtener y ejecutar el movimiento
        posicion = obtener_movimiento(tablero, jugador)
        tablero[posicion] = jugador
        
        # 2. Mostrar el tablero actualizado
        mostrar_tablero(tablero)
        
        # 3. Comprobar si hay un ganador
        if verificar_ganador(tablero, jugador):
            print(f" ¡Jugador  *{jugador}*  ha ganado! ")
            return # Termina la función y el juego
            
        # 4. Cambiar de jugador
        jugador = "O" if jugador == "X" else "X"

    # Si el bucle termina sin un ganador (es decir, los 9 turnos se completaron)
    print(" ¡Empate! Nadie ha ganado. ")

# INICIO DEL JUEGO

if __name__ == "__main__":
    print("--- Bienvenido al juego de Tres en Raya (Tic-Tac-Toe) ---")

# ----------------------------------------------------------------------
# FUNCIONES DEL JUEGO
# ----------------------------------------------------------------------

def mostrar_tablero(tablero):
    """Muestra el tablero de Tic-Tac-Toe en la consola."""
    print()
    print(tablero[0] + " | " + tablero[1] + " | " + tablero[2])
    print("--+---+---")
    print(tablero[3] + " | " + tablero[4] + " | " + tablero[5])
    print("--+---+---")
    print(tablero[6] + " | " + tablero[7] + " | " + tablero[8])
    print()

def obtener_movimiento(tablero, jugador):
    """Solicita al jugador una posición válida y la retorna ajustada al índice."""
    while True:
        # Pide la posición al jugador
        posicion = input(f"Jugaor {jugador}, selecciona una posición (1-9): ")

        # 1. Verificar si es un número
        if not posicion.isdigit():
            print("Entrada no válida. Por favor, ingresa un número del 1 al 9.")
            continue

        posicion_idx = int(posicion) - 1

        # 2. Verificar si está en el rango (0 a 8)
        if not (0 <= posicion_idx <= 8):
            print("Posición fuera de rango. Elige un número entre 1 y 9.")
            continue

        # 3. Verificar si la casilla está vacía
        if tablero[posicion_idx] != " ":
            print("Esa casilla ya está ocupada. Elige otra.")
            continue
        
        # Si todo es válido, retorna el índice (0-8)
        return posicion_idx

def verificar_ganador(tablero, jugador):
    """Verifica si el jugador actual ha ganado."""
    
    # Definir todas las combinaciones ganadoras (filas, columnas, diagonales)
    combinaciones_ganadoras = [
        # Filas
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        # Columnas
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        # Diagonales
        (0, 4, 8), (2, 4, 6)
    ]
    
    # Comprobar si alguna combinación tiene las 3 marcas del jugador
    for a, b, c in combinaciones_ganadoras:
        if tablero[a] == tablero[b] == tablero[c] == jugador:
            return True
            
    return False

def jugar_tres_en_raya():
    """Función principal que ejecuta el juego de Tic-Tac-Toe."""
    
    # Inicialización
    tablero = [" "] * 9
    jugador = "X"
    mostrar_tablero(tablero)
    
    # Bucle principal del juego
    for turno in range(9):
        
        # 1. Obtener y ejecutar el movimiento
        posicion = obtener_movimiento(tablero, jugador)
        tablero[posicion] = jugador
        
        # 2. Mostrar el tablero actualizado
        mostrar_tablero(tablero)
        
        # 3. Comprobar si hay un ganador
        if verificar_ganador(tablero, jugador):
            print(f" ¡Jugador  *{jugador}*  ha ganado! ")
            return # Termina la función y el juego
            
        # 4. Cambiar de jugador
        jugador = "O" if jugador == "X" else "X"

    # Si el bucle termina sin un ganador (es decir, los 9 turnos se completaron)
    print(" ¡Empate! Nadie ha ganado. ")

# INICIO DEL JUEGO

if __name__ == "__main__":
    print("--- Bienvenido al juego de Tres en Raya (Tic-Tac-Toe) ---")

    jugar_tres_en_raya()