import random
palabras = ["leonel", "koala", "programación"]
palabraSecreta = random.choice(palabras)

progreso = ["_"] * len(palabraSecreta)

vidas = 3

print("---Bienvenido al juego del Ahorcado---")
print("Tienes 3 vidas para adivinar la palabra secreta.")
print(" ".join(progreso))

while vidas > 0 and "_" in progreso:
    letra = input("\nIngresa una letra: ").lower()



    if letra in palabraSecreta:
        for i in range(len(palabraSecreta)):
            if palabraSecreta[i] == letra:
                progreso[i] = letra
    else:
     vidas -= 1
    print(f"Letra incorrecta. Te quedan {vidas} vidas.")
    print(" ".join(progreso))#Mostramos el progreso
if "_" not in progreso:
    print("\n¡Muy bien!, la palabra es: ", palabraSecreta)
else:
    print("\nYa no te quedan más vidas.")
    print("La palabra era:", palabraSecreta)