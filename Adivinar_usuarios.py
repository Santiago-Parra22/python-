import getpass
def Juego():
    print("jugador 2, por favor aléjese 5 minutos")
    numero = int(getpass.getpass("Ingrese el numero que el jugador 2 debe adivinar: "))
    jugador2(numero)

def jugador2(numero):    
    adivinar=0
    while numero!=adivinar:
        print("Ingrese el numero para que pueda adivinar")
        adivinar=int(input())
    print("Haz acertado Felicitaciones")    
Juego()
