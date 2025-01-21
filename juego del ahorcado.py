import random

def Palabras():
    # Seleccionar una palabra al azar
    palabra = random.choice(["AGUJA", "MOUSE", "TORRE", "MESA", "MARCADOR", "TECLADO", "COMPUTADOR", "MINA", "ESFERO"])
    print("Bienvenido al juego del ahorcado. ¡Tienes 10 intentos para adivinar la palabra!")
    print(f"La palabra tiene {len(palabra)} letras.")

    # Inicializar variables
    intentos_restantes = 10
    adivinar = ["_"] * len(palabra)
    letras_usadas = []

    # Juego principal
    while intentos_restantes > 0 and "_" in adivinar:
        print("\nPalabra actual:", " ".join(adivinar))
        print(f"Intentos restantes: {intentos_restantes}")
        print(f"Letras usadas: {', '.join(letras_usadas)}")
        letra = input("Ingrese una letra: ").upper()

        # Validar la entrada
        if len(letra) != 1 or not letra.isalpha():
            print("Por favor, ingrese una sola letra válida.")
            continue

        if letra in letras_usadas:
            print(f"Ya has usado la letra '{letra}'. Intenta con otra.")
            continue

        # Agregar la letra a las usadas
        letras_usadas.append(letra)

        # Verificar si la letra está en la palabra
        if letra in palabra:
            print(f"¡Bien! La letra '{letra}' está en la palabra.")
            for idx, char in enumerate(palabra):
                if char == letra:
                    adivinar[idx] = letra
        else:
            print(f"La letra '{letra}' no está en la palabra.")
            intentos_restantes -= 1

    # Resultado del juego
    if "_" not in adivinar:
        print("\n¡Felicidades! Has adivinado la palabra:", palabra)
    else:
        print("\nSe te acabaron los intentos. La palabra era:", palabra)

# Llamar a la función para jugar
Palabras()
