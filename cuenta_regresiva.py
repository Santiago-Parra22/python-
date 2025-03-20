import time

def temporizador(segundos):
    while segundos:
        min = segundos // 60
        secs= segundos % 60
        print(f"el tiempo restantes es {min:02d}:{secs:02d}")
        time.sleep(1)
        segundos -=1

tiempo =int(input("Ingrese el tiempo que desee: "))
temporizador(tiempo)