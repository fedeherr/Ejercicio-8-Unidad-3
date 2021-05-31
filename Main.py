from datetime import date
from datetime import datetime
import csv
from Menu import Menu
from Colección import Coleccion
from Contratado import Contratado
from Planta import Planta
from Externo import Externo
from ITesorero import ITesorero
from IGerente import IGerente
import zope.interface
from zope.interface.verify import verifyObject 

def Gerente(empleado):
    menu = Menu()
    op = int(input("1. Modificar Básico \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Opcion: " ))
    while op > 0:
        menu.opcion(op+10, empleado)
        op = int(input("1. Modificar Báscio \n 2. Modificar Viatico \n 3. Modificar Valor de Hora \n 0. Salir \n Ingrese Opcion: " ))

def Tesorero(empleado):
    menu = Menu()
    empleado.modificarBasicoEPlanta(" ", " ") #aqui llamo a un método de Gerete
    print(" 1. Registrar Horas \n 2. Total de la tarea \n 3. Ayuda a empleados \n 4. Sueldos \n 5. Sueldo Empleado \n 0. Salir")
    op = int(input("\n Ingrese opcion: "))
    while op > 0:
        menu.opcion(op,empleado)
        print(" 1. Registrar Horas \n 2. Total de la tarea \n 3. Ayuda a empleados \n 4. Sueldos \n 5. Sueldo Empleado \n 0. Salir")
        op = int(input("\n Ingrese opcion: "))


if __name__ == "__main__":
    a = int(input("Ingrese la cantidad de componentes que quiera que tenga el arreglo: "))
    empleados=Coleccion(a)
    b = empleados.manejarEmpleadosCon()
    if (b == 1):
        b = empleados.manejarEmpleadosExt()
        if (b == 1):
            b = empleados.manejarEmpleadosPla()
    
    user = input("Ingrese Usuario: ")
    password = input("Ingrese Contraseña: ")

    if user == "t" and password == "t":
        Tesorero(ITesorero(empleados))

    elif user== "g" and password =="g":
        Gerente(IGerente(empleados))
    else:
        print("Credenciales incorrectas")