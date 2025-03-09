import random

def juego():
    maquina=random.randint(1,10)
    print("Bienvenido al juego adivina el numero contra la maquina: ")
    usuario=int(input("Ingrese un numero del 1 al 10 para empezar el juego: "))
    if usuario<=10:
        if maquina==usuario:
            print("Haz ganado")
        else:
            print("Intente de nuevo")
            juego()
    else:
        print("ingrese un numero valido: ")
        juego()            

juego()

