import random

def seleccionar_palabra():
    """Selecciona una palabra al azar de la lista."""
    palabras = ["leonel", "koala", "programacion", "python", "ahorcado"]
    return random.choice(palabras)

def inicializar_juego(palabra_secreta):
    """Inicializa el progreso de la palabra con guiones bajos y muestra el mensaje de bienvenida."""
    progreso = ["_"] * len(palabra_secreta)
    vidas = 6  
    print("---Bienvenido al juego del Ahorcado---")
    print(f"Tienes {vidas} vidas para adivinar la palabra secreta.")
    print("Palabra: " + " ".join(progreso))
    return progreso, vidas

def procesar_intento(letra, palabra_secreta, progreso, vidas):
    """Procesa la letra ingresada por el usuario."""
    letra_correcta = False
    if letra in palabra_secreta:
        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] == letra:
                # Solo actualiza si la letra no ha sido adivinada ya
                if progreso[i] == "_":
                    progreso[i] = letra
                    letra_correcta = True
    
    if not letra_correcta and letra not in progreso: # Si la letra es incorrecta O ya fue adivinada, no pierdes vida.
        # Si la letra está en la palabra secreta, pero ya estaba en progreso, no pierdes vida y no hace falta indicarlo como incorrecto.
        vidas -= 1
        print(f"¡Letra incorrecta!  Te quedan *{vidas}* vidas.")
    elif letra_correcta:
         print(f"¡Letra correcta! ")
    else:
        print(f"La letra '{letra}' ya ha sido adivinada o no es la mejor opción. ")

    print("Palabra: " + " ".join(progreso))
    return progreso, vidas

def jugar_ahorcado():
    """Función principal que ejecuta el juego del Ahorcado."""
    palabra_secreta = seleccionar_palabra()
    progreso, vidas = inicializar_juego(palabra_secreta)
    
    letras_adivinadas = set() # Usamos un conjunto para almacenar letras intentadas
    
    while vidas > 0 and "_" in progreso:
        # Pide una letra válida
        while True:
            letra = input("\nIngresa una letra: ").lower()
            if len(letra) == 1 and letra.isalpha():
                if letra in letras_adivinadas:
                    print(f"Ya intentaste la letra '{letra}'. Prueba con otra.")
                else:
                    letras_adivinadas.add(letra)
                    break
            else:
                print("Por favor, ingresa solo una **única letra** válida.")

        # Procesa el intento
        progreso, vidas = procesar_intento(letra, palabra_secreta, progreso, vidas)
        
    # Muestra el resultado final
    if "_" not in progreso:
        print(f" ¡FELICIDADES! ¡Adivinaste la palabra!")
        print(f"La palabra era: *{palabra_secreta.upper()}*")
    else:
        print(" *GAME OVER*")
        print(f"¡Ya no te quedan más vidas!")
        print(f"La palabra era: *{palabra_secreta.upper()}*")

# Iniciar el juego
if __name__ == "__main__":
    jugar_ahorcado()