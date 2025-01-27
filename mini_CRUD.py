import pymysql
#se realiza la conexion a la base de datos
coneection=pymysql.connect(host="localhost",user="root",password="",db="libreria shasan",port=3307)
cur=coneection.cursor()

#se crea una función para agregar los libros
def Insertar_Libro():
    try:
        nombre=input("Ingrese el nombre del libro: ")
        editorial=input("Ingrese la editorial del libro: ")
        autor=input("Ingrese el nombre del Autor: ")
        cur.execute("INSERT INTO libro (NombreLibro,EditorialLibro,AutorLibro) values(%s,%s,%s)",(nombre,editorial,autor))
        coneection.commit()
        print("Libro agregado con exito")
    except pymysql.MySQLError as E:    
        print(f"No se pudo agregar el libro: {E}")
# se crea una funcion para traer la informacion de los libros registrados
def traer_datos():
    try:
        cur.execute("select * from libro")
        libros=cur.fetchall()
        print("Los libros registrados son:")
        for libro in libros:
                print("------------------------")
                print("ID: ",libro[0])
                print("Nombre: ",libro[1])
                print("Editorial: ",libro[2])
                print("Autor: ",libro[3])
    except pymysql.MySQLError as E:
        print("No se pueden mostrar los datos: {E}")    

# se crea funcion para actualizar los datos 
def actualizar_datos():
    traer_datos()
    print("Que registro desea actualizar: ")
    eleccion=int(input("Ingrese la opcion: "))
    if eleccion==1:      
        cur.execute("select * from libro where IdLibro=%s",(eleccion))
        libro=cur.fetchone()
        print(libro)
        print("1.Nombre\n2.Editorial\n3.Autor")
        try:
            modificacion=int(input("Que dato quiere modificar: "))
            if modificacion==1:
                Nuevonombre=input("Ingrese el nuevo nombre: ")
                cur.execute('update libro set NombreLibro=%s where NombreLibro= %s ',(Nuevonombre,libro[1]))
                coneection.commit()
                print("Actualizacion realizada con exito")
            elif modificacion==2:
                NuevaEditorial=input("Ingrese la nueva editorial: ")
                cur.execute('update libro set EditorialLibro=%s where NombreLibro= %s ',(NuevaEditorial,libro[1]))
                coneection.commit()
                print("Actualizacion realizada con exito")
            elif modificacion==3:
                Autor=input("Ingrese el nuevo autor: ")
                cur.execute('update libro set AutorLibro=%s where NombreLibro= %s ',(Autor,libro[1]))
                coneection.commit()
                print("Actualizacion realizada con exito")        

        except pymysql.MySQLError as E:
            print("No se pudo realizar la actualizacion del registro: {E}")    

    if eleccion==2:      
        cur.execute("select * from libro where IdLibro=%s",(eleccion))
        libro=cur.fetchone()
        print(libro)
        print("1.Nombre\n2.Editorial\n3.Autor")
        try:
            modificacion=int(input("Que dato quiere modificar: "))
            if modificacion==1:
                Nuevonombre=input("Ingrese el nuevo nombre: ")
                cur.execute('update libro set NombreLibro=%s where NombreLibro= %s ',(Nuevonombre,libro[1]))
                coneection.commit()
                print("Actualizacion realizada con exito")
            elif modificacion==2:
                NuevaEditorial=input("Ingrese la nueva editorial: ")
                cur.execute('update libro set EditorialLibro=%s where NombreLibro= %s ',(NuevaEditorial,libro[1]))
                coneection.commit()
                print("Actualizacion realizada con exito")
            elif modificacion==3:
                Autor=input("Ingrese el nuevo autor: ")
                cur.execute('update libro set AutorLibro=%s where NombreLibro= %s ',(Autor,libro[1]))
                coneection.commit()
                print("Actualizacion realizada con exito")        

        except pymysql.MySQLError as E:
            print("No se pudo realizar la actualizacion del registro: {E}")

# se crea funcion para borrar datos
def borrar_datos():
    datoAEliminar=input("Ingrese el registro a borrar: ")
    cur.execute("delete from libro where IdLibro=%s",(datoAEliminar))
    coneection.commit()


 # se crea el menu para el usuario   
def menu():
    print("Bienvenido al sistema Bibliotecario SHASAN\nque deseas hacer hoy\n1.ingresar un libro\n2.Ver libros registrados\n3.Actualizar libros registrados")
    respuesta=int(input("Ingrese la opcion escogida: "))
    if respuesta==1:
        Insertar_Libro()
    if respuesta==2:
        traer_datos()
    if respuesta==3:
        actualizar_datos()
    if respuesta==4:
        borrar_datos()
    if respuesta==5:
        breakpoint                

menu()

#se cierra la conexion a base de datos
coneection.close()