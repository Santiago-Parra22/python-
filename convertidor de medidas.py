# -*- coding: utf-8 -*-
"""Untitled

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1JsR0kh5nvxacDqtQoi05i-SyT-aKRPyY
"""

def Kilometros_a_millas():
   kilometros=float(input("Ingrese los kilometros a convertir: " ))
   millas = kilometros * 0.621371
   print( f"{kilometros} son equivalentes a {millas} millas")

def millas_a_kilometros():
   print("Bienvenido al Convertidor de Millas a Kilometros ")
   millas=float(input("Ingrese las millas a convertir: " ))
   kilometros = millas / 0.621371
   print( f"{kilometros}KM son equivalentes a {millas} millas")
   print("")

def farenheit_a_celsius():
  farenheit=float(input("Ingrese los grados farenheit a convertir: "))
  celsius = (farenheit - 32 ) * (5/9)
  print(f"sus grados farenheit:{farenheit}° equivalen a:{celsius}°celsius ")

def celsius_a_farenheit():
  celsius=float(input("Ingrese los grados Celsius a convertir: "))
  farenheit= (celsius - 32) * 5/9
  print(f"sus grados celsius:{celsius}° equivalen a:{farenheit}°farenheit ")

def menu():

    while True:
      print("Bienvenid@ al Convertidor de Unidades")
      print("Selecciona la conversión que deseas realizar:")
      print("1. Kilómetros a Millas")
      print("2. Millas a Kilómetros")
      print("3. Grados Celsius a Fahrenheit")
      print("4. Grados Fahrenheit a Celsius")
      print("5. Salir")

      decision =input(" Ingrese el convertidor a usar: ")


      #Conversion de millas a kilometros
      if decision == "1":
        print("Bienvenido al Convertidor de Kilometros a Millas ")
        Kilometros_a_millas()

        print("1.Otra conversion\n2.salir")
        salir=int(input("Ingrese la accion: "))
        if salir=="1":
          Kilometros_a_millas()
        elif salir=="2":
          menu()

      #Conversion de kilometros a millas
      if decision == "2":
        print("Bienvenido al Convertidor de Kilometros a Millas")
        millas_a_kilometros()
        print("1.Otra conversion\n2.salir")
        salir=int(input("Ingrese la accion: "))
        if salir=="1":
          Kilometros_a_millas()
        elif salir=="2":
          menu()

      if decision=="3":
        #convertidor de grados celsius a farenheit
        print("Bienvenido al convertidor de Celsius a farenheit")
        farenheit_a_celsius()

      if decision=="4":
        #convertidor de grados farenheit a celsius
        print("Bienvenido al convertidor farenheit a Celsius")
        celsius_a_farenheit()

      if decision=="5":
        break;

menu()