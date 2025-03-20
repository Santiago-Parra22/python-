
#se realiza el modulo de las prendas de niña recorriendo la cantidad y la talla respectiva
def Prenda_niña():
      #se crea una condicion para que valide la eleccion del usuario
  tallas=[]#lista de las tallas
  cantidad=[]#lista de las cantidades de cada talla
  while True:

    #se crea un menu para que el usuario navegue facilmente
    print("1.cantidad por Talla\n2.Consulta de inventario\n3.Eliminar talla\n4.Actualizar Cantidad\n5.Cantidad total del inventario\n6.Menu principal")
    decision=int(input("Selecione su opcion: "))


    if decision==1:
      #se crean dos listas vacias para almacenar datos como las tallas y la respectiva cantidad de cada talla

      print("Esta en el modulo de insertar la cantidad por talla ")
      print("Tenga en cuenta que las tallas que puede trabajar son las siguientes: 2-4-6-8-10-12-14-16")
      talla=int(input("Ingrese la cantidad de tallas con las que va a trabajar "))
      # se recorre las listas vacias para incluir las datos de la talla y la cantidad
      for t in range(talla):
        tal=int(input(f"Ingrese la talla { t + 1}: "))
        can=int(input(f"Ingrese la cantidad de la talla "))
        ca=cantidad.append(can)#adicion de las cantidades
        ta=tallas.append(tal)#adicion de las tallas

    elif decision==2:
      # se crea un for para que consulte la información anteriormente registrada
      if len(tallas)==0:
        print("No hay nada en inventario ")
      else:
        for i in range(len(tallas)):
          print(f"De la talla {tallas[i]} hay una cantidad de {cantidad[i]} prendas ")

    elif decision==3:
      #Se crea una opcion que permita al usuario eliminar alguna talla que halla registrado mal
      if len(tallas) == 0:
        print("No hay registros para eliminar.")
      elif len(tallas)>0:
          print("Ingrese la talla que desea eliminar:")
          talla_a_eliminar = int(input())
          if talla_a_eliminar in tallas:
            indice = tallas.index(talla_a_eliminar)
            tallas.pop(indice)
            cantidad.pop(indice)
            print("Talla ELiminada con exito\n")

    elif decision==4:
        if len(tallas)==0:
          print("No se puede actualizar nada mientras que el inventario este vacio")
        else:
          talla=int(input("Ingrese la talla a Actualizar"))
          if talla in tallas:
            can=int(input("Ingrese la nueva cantidad: "))
            talla=tallas.index(talla)
            cantidad[talla]=can

          else:
            print("La talla ingresada no se encuentra en el Inventario. ")
    elif decision==5:
      total=sum (cantidad)
      print("La cantidad de prendas en su inventario es de:", total)

    else:
      break
  return

#se realiza el modulo de las prendas de niña recorriendo la cantidad y la talla respectiva
def Prenda_niño():
      #se crea una condicion para que valide la eleccion del usuario
  tallas=[]#lista de las tallas
  cantidad=[]#lista de las cantidades de cada talla
  while True:

    #se crea un menu para que el usuario navegue facilmente
    print("1.cantidad por Talla\n2.Consulta de inventario\n3.Eliminar talla\n4.Actualizar Cantidad\n5.Cantidad total del inventario\n6.Menu principal")
    decision=int(input("Selecione su opcion: "))


    if decision==1:
      #se crean dos listas vacias para almacenar datos como las tallas y la respectiva cantidad de cada talla

      print("Esta en el modulo de insertar la cantidad por talla ")
      print("Tenga en cuenta que las tallas que puede trabajar son las siguientes: 2-4-6-8-10-12-14-16")
      talla=int(input("Ingrese la cantidad de tallas con las que va a trabajar "))
      # se recorre las listas vacias para incluir las datos de la talla y la cantidad
      for t in range(talla):
        tal=int(input(f"Ingrese la talla { t + 1}: "))
        can=int(input(f"Ingrese la cantidad de la talla "))
        ca=cantidad.append(can)#adicion de las cantidades
        ta=tallas.append(tal)#adicion de las tallas

    elif decision==2:
      # se crea un for para que consulte la información anteriormente registrada
      if len(tallas)==0:
        print("No hay nada en inventario ")
      else:
        for i in range(len(tallas)):
          print(f"De la talla {tallas[i]} hay una cantidad de {cantidad[i]} prendas ")

    elif decision==3:
      #Se crea una opcion que permita al usuario eliminar alguna talla que halla registrado mal
      if len(tallas) == 0:
        print("No hay registros para eliminar.")
      elif len(tallas)>0:
          print("Ingrese la talla que desea eliminar:")
          talla_a_eliminar = int(input())
          if talla_a_eliminar in tallas:
            indice = tallas.index(talla_a_eliminar)
            tallas.pop(indice)
            cantidad.pop(indice)
            print("Talla ELiminada con exito\n")

    elif decision==4:
        if len(tallas)==0:
          print("No se puede actualizar nada mientras que el inventario este vacio")
        else:
          talla=int(input("Ingrese la talla a Actualizar"))
          if talla in tallas:
            can=int(input("Ingrese la nueva cantidad: "))
            talla=tallas.index(talla)
            cantidad[talla]=can

          else:
            print("La talla ingresada no se encuentra en el Inventario. ")
    elif decision==5:
      total=sum (cantidad)
      print("La cantidad de prendas en su inventario es de:", total)

    else:
      break
  return


#se realiza el modulo de las prendas de niña recorriendo la cantidad y la talla respectiva
def Prenda_dama():
      #se crea una condicion para que valide la eleccion del usuario
  tallas=[]#lista de las tallas
  cantidad=[]#lista de las cantidades de cada talla
  while True:

    #se crea un menu para que el usuario navegue facilmente
    print("1.cantidad por Talla\n2.Consulta de inventario\n3.Eliminar talla\n4.Actualizar Cantidad\n5.Cantidad total del inventario\n6.Menu principal")
    decision=int(input("Selecione su opcion: "))


    if decision==1:
      #se crean dos listas vacias para almacenar datos como las tallas y la respectiva cantidad de cada talla

      print("Esta en el modulo de insertar la cantidad por talla ")
      print("Tenga en cuenta que las tallas que puede trabajar son las siguientes: 2-4-6-8-10-12-14-16")
      talla=int(input("Ingrese la cantidad de tallas con las que va a trabajar "))
      # se recorre las listas vacias para incluir las datos de la talla y la cantidad
      for t in range(talla):
        tal=int(input(f"Ingrese la talla { t + 1}: "))
        can=int(input(f"Ingrese la cantidad de la talla "))
        ca=cantidad.append(can)#adicion de las cantidades
        ta=tallas.append(tal)#adicion de las tallas

    elif decision==2:
      # se crea un for para que consulte la información anteriormente registrada
      if len(tallas)==0:
        print("No hay nada en inventario ")
      else:
        for i in range(len(tallas)):
          print(f"De la talla {tallas[i]} hay una cantidad de {cantidad[i]} prendas ")

    elif decision==3:
      #Se crea una opcion que permita al usuario eliminar alguna talla que halla registrado mal
      if len(tallas) == 0:
        print("No hay registros para eliminar.")
      elif len(tallas)>0:
          print("Ingrese la talla que desea eliminar:")
          talla_a_eliminar = int(input())
          if talla_a_eliminar in tallas:
            indice = tallas.index(talla_a_eliminar)
            tallas.pop(indice)
            cantidad.pop(indice)
            print("Talla ELiminada con exito\n")
# se crea un modulo por si el usuario quiere actualizar la cantidad de alguna talla en especifico
    elif decision==4:
        if len(tallas)==0:
          print("No se puede actualizar nada mientras que el inventario este vacio")
        else:
          talla=int(input("Ingrese la talla a Actualizar"))
          if talla in tallas:
            can=int(input("Ingrese la nueva cantidad: "))
            talla=tallas.index(talla)
            cantidad[talla]=can

          else:
            print("La talla ingresada no se encuentra en el Inventario. ")
    elif decision==5:
      total=sum (cantidad)
      print("La cantidad de prendas en su inventario es de:", total)

    else:
      break
  return


#se realiza el modulo de las prendas de niña recorriendo la cantidad y la talla respectiva
def Prenda_dama():
      #se crea una condicion para que valide la eleccion del usuario
  tallas=[]#lista de las tallas
  cantidad=[]#lista de las cantidades de cada talla
  while True:

    #se crea un menu para que el usuario navegue facilmente
    print("1.cantidad por Talla\n2.Consulta de inventario\n3.Eliminar talla\n4.Actualizar Cantidad\n5.Cantidad total del inventario\n6.Menu principal")
    decision=int(input("Selecione su opcion: "))


    if decision==1:
      #se crean dos listas vacias para almacenar datos como las tallas y la respectiva cantidad de cada talla

      print("Esta en el modulo de insertar la cantidad por talla ")
      print("Tenga en cuenta que las tallas que puede trabajar son las siguientes: 2-4-6-8-10-12-14-16")
      talla=int(input("Ingrese la cantidad de tallas con las que va a trabajar "))
      # se recorre las listas vacias para incluir las datos de la talla y la cantidad
      for t in range(talla):
        tal=int(input(f"Ingrese la talla { t + 1}: "))
        can=int(input(f"Ingrese la cantidad de la talla "))
        ca=cantidad.append(can)#adicion de las cantidades
        ta=tallas.append(tal)#adicion de las tallas

    elif decision==2:
      # se crea un for para que consulte la información anteriormente registrada
      if len(tallas)==0:
        print("No hay nada en inventario ")
      else:
        for i in range(len(tallas)):
          print(f"De la talla {tallas[i]} hay una cantidad de {cantidad[i]} prendas ")

    elif decision==3:
      #Se crea una opcion que permita al usuario eliminar alguna talla que halla registrado mal
      if len(tallas) == 0:
        print("No hay registros para eliminar.")
      elif len(tallas)>0:
          print("Ingrese la talla que desea eliminar:")
          talla_a_eliminar = int(input())
          if talla_a_eliminar in tallas:
            indice = tallas.index(talla_a_eliminar)
            tallas.pop(indice)
            cantidad.pop(indice)
            print("Talla ELiminada con exito\n")

    elif decision==4:
      # se crea un modulo por si el usuario quiere actualizar la cantidad de alguna talla en especifico
        if len(tallas)==0:
          print("No se puede actualizar nada mientras que el inventario este vacio")
        else:
          talla=int(input("Ingrese la talla a Actualizar"))
          if talla in tallas:
            can=int(input("Ingrese la nueva cantidad: "))
            talla=tallas.index(talla)
            cantidad[talla]=can

          else:
            print("La talla ingresada no se encuentra en el Inventario. ")
    elif decision==5:
      total=sum (cantidad)
      print("La cantidad de prendas en su inventario es de:", total)

    else:
      break
  return

def Prenda_hombre():
      #se crea una condicion para que valide la eleccion del usuario
  tallas=[]#lista de las tallas
  cantidad=[]#lista de las cantidades de cada talla
  while True:

    #se crea un menu para que el usuario navegue facilmente
    print("1.cantidad por Talla\n2.Consulta de inventario\n3.Eliminar talla\n4.Actualizar Cantidad\n5.Cantidad total del inventario\n6.Menu principal")
    decision=int(input("Selecione su opcion: "))


    if decision==1:
      #se crean dos listas vacias para almacenar datos como las tallas y la respectiva cantidad de cada talla

      print("Esta en el modulo de insertar la cantidad por talla ")
      print("Tenga en cuenta que las tallas que puede trabajar son las siguientes: 2-4-6-8-10-12-14-16")
      talla=int(input("Ingrese la cantidad de tallas con las que va a trabajar "))
      # se recorre las listas vacias para incluir las datos de la talla y la cantidad
      for t in range(talla):
        tal=int(input(f"Ingrese la talla { t + 1}: "))
        can=int(input(f"Ingrese la cantidad de la talla "))
        ca=cantidad.append(can)#adicion de las cantidades
        ta=tallas.append(tal)#adicion de las tallas

    elif decision==2:
      # se crea un for para que consulte la información anteriormente registrada
      if len(tallas)==0:
        print("No hay nada en inventario ")
      else:
        for i in range(len(tallas)):
          print(f"De la talla {tallas[i]} hay una cantidad de {cantidad[i]} prendas ")

    elif decision==3:
      #Se crea una opcion que permita al usuario eliminar alguna talla que halla registrado mal
      if len(tallas) == 0:
        print("No hay registros para eliminar.")
      elif len(tallas)>0:
          print("Ingrese la talla que desea eliminar:")
          eliminar = int(input())
          if eliminar in tallas:
            indice = tallas.index(eliminar)
            tallas.pop(indice)
            cantidad.pop(indice)
            print("Talla ELiminada con exito\n")

    elif decision==4:
        if len(tallas)==0:
          # se crea un modulo por si el usuario quiere actualizar la cantidad de alguna talla en especifico
          print("No se puede actualizar nada mientras que el inventario este vacio")
        else:
          talla=int(input("Ingrese la talla a Actualizar"))
          if talla in tallas:
            can=int(input("Ingrese la nueva cantidad: "))
            talla=tallas.index(talla)
            cantidad[talla]=can

          else:
            print("La talla ingresada no se encuentra en el Inventario. ")
    elif decision==5:
      total=sum (cantidad)
      print("La cantidad de prendas en su inventario es de:", total)

    else:
      break
  return

def menu():
  print("Bienvenido a su gestión de prendas producidas en el mes")
  while True:
    print("1. Ingresar Prendas de niña\n2. Ingresar Prendas de niño\n3. Ingresar Prendas de Dama\n4. Ingresar Prendas de Caballero\n5. Salir del programa")
    opcion = int(input("Ingrese una opción válida: "))

    if opcion == 1:
      Prenda_niña()
    elif opcion == 2:
      Prenda_niño()
    elif opcion == 3:
      Prenda_dama()
    elif opcion == 4:
      Prenda_hombre()
    else:
      break
      print("Número inválido")


menu()