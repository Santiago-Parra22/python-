import random
def juego():
    options=["Piedra","Papel","Tijera"]
    decision= random.choice(options)
    jugador= input("Ingrese una opción entre piedra papel y tijera: ").lower()
    if decision == jugador:
        print("Empate")
    
    elif (decision == "piedra" and jugador == "papel") or \
         (decision == "papel" and jugador == "tijera") or \
         (decision == "tijera" and jugador == "piedra"):
        print("Ganó el jugador")
    else:
        print("gano la maquina")

    print(f"La maquina escojio {decision} y usted escojio {jugador.capitalize()}")        

juego()