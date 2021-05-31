import numpy as np
from Planta import Planta
from Externo import Externo
from Contratado import Contratado
from Empleado import Empleado
import csv
import datetime as dt
from ITesorero import ITesorero
from IGerente import IGerente
from zope.interface import implementer
@implementer(ITesorero)
@implementer(IGerente)
class Coleccion(object):
    __arr = None
    __contador = 0
    __total = 0
    def __init__(self, larr):
                self.__arr = np.empty(larr, dtype = Empleado)
                self.__total = larr
                self.__contador = 0
    def agregarEmpleado(self, unEmpleado):
        if (self.__contador != self.__total):
            self.__arr[self.__contador] = unEmpleado
            print(self.__arr[self.__contador])
            self.__contador += 1
            return 1
        else:
            print ("Cantidad máxima de empleados alcanzados")
            return 0
    def gastosSueldoPorEmpleado(self, dni):
        i = 0
        while ((self.__arr[i].getDni != dni)&(i < len(self.__arr) - 1)):
            i+=1
        if (self.__arr[i].getDni == dni): print("Sueldo %d" % (self.__arr[i].getSueldo()))
        else: print("Dni incorrecto")

    def modificarBasicoEPlanta(self, dni, nuevoBasico):
        i = 0
        while ((self.__arr[i].getDni() != dni)&(i < len(self.__arr) - 1)):
            i+=1
        if ((self.__arr[i].getDni() == dni)&(isinstance(self.__arr[i],Planta))):
            self.__arr[i].setSueldo(nuevoBasico)
            print("Se actualizó el sueldo")
            print("Nuevo Sueldo final:", self.__arr[i].getSueldo())
        else: print("Dni incorrecto o el empleado no es de planta")
        
    def modificarViaticoEExterno(self, dni, nuevoViatico):
        i = 0
        while ((self.__arr[i].getDni() != dni)&(i < len(self.__arr) - 1)):
            i+=1
        if ((self.__arr[i].getDni() == dni)&(isinstance(self.__arr[i],Externo))):
            self.__arr[i].setSueldo(nuevoViatico)
            print("Se actualizó el sueldo")
            print("Nuevo Sueldo final:", self.__arr[i].getSueldo())
        else: print("Dni incorrecto o el empleado no es Externo")
    def modificarValorEPorHora(self, nuevoValorHora):
        for i in range(len(self.__arr)):
            if (isinstance(self.__arr[i],Contratado)):
                self.__arr[i].setSueldo(nuevoValorHora)
                print("Se actualizo el sueldo del empleado con DNI %d" % (self.__arr[i].getDni()))
                print("Nuevo sueldo: %f" % (self.__arr[i].getSueldo()))

    def nuevaHoras(self, dni, horas):
        i = 0
        bandera = True
        while ((i < self.__total) & (bandera)):
            if (self.__arr[i].getDni() == dni): bandera = False
            else: i += 1
        if (i == self.__total):
            print ("El dni no se encontró")
            return()
        if(isinstance(self.__arr[i], Contratado)):
            self.__arr[i].cambioHora(horas)
            print ("Se cambio el sueldo")
        else: print("El empleado no es de tipo Contratado")

    def ayudaSueldo(self):
        print ("Los siguientes empleados les corresponde la ayuda: ")
        for i in range(len(self.__arr)):
            if(self.__arr[i].getSueldo() < 25000):
                print(self.__arr[i])
    def mostrarSueldo(self):
        print ("Total de los sueldos: ")
        for i in range(len(self.__arr)):
                print("Empleado: %s, Tel %d, Sueldo %d" % (self.__arr[i].getNombre(), self.__arr[i].getTel(), self.__arr[i].getSueldo()))

    def totalTarea(self, tarea):
        total = 0
        bandera = True
        for i in range(len(self.__arr)):
            if(isinstance(self.__arr[i], Externo)):
                if(self.__arr[i].getTarea() == tarea):
                    a = dt.date.fromisoformat(self.__arr[i].getFechaFin())
                    if(a > dt.date.today()):
                        total += self.__arr[i].getSueldo()
        print(total)

    def manejarEmpleadosPla(self):
        archivo = open('Planta.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        a = 1
        for fila in reader:
            if bandera:
                #Saltear bandera
                bandera = not bandera
            else:
                    dni = int(fila[0])
                    nombre = fila[1]
                    direccion = fila[2]
                    telefono = int(fila[3])
                    sb = int(fila[4])
                    antiguedad = int(fila[5])
                    unEmpleado = Planta(dni, nombre, direccion, telefono, sb, antiguedad)
                    a = self.agregarEmpleado(unEmpleado)
                    if (a == 0): return a
        return a
    def manejarEmpleadosExt(self):
        archivo = open('externos.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        a = 1
        for fila in reader:
            if bandera:
                #Saltear bandera
                bandera = not bandera
            else:
                    dni = int(fila[0])
                    nombre = fila[1]
                    direccion = fila[2]
                    telefono = int(fila[3])
                    tarea = fila[4]
                    fechainicio = fila[5]
                    fechafinal = fila[6]
                    mv = int(fila[7])
                    costoobra = int(fila[8])
                    seguro = int(fila[9])
                    unEmpleado = Externo(dni, nombre, direccion, telefono, fechainicio, fechafinal, tarea, mv, costoobra, seguro)
                    a = self.agregarEmpleado(unEmpleado)
                    if (a == 0): return a
        return a
    def manejarEmpleadosCon(self):
        archivo = open('contratados.csv')
        reader = csv.reader(archivo,delimiter=';')
        bandera = True
        a = 1
        for fila in reader:
            if bandera:
                #Saltear bandera
                bandera = not bandera
            else:
                    dni = int(fila[0])
                    nombre = fila[1]
                    direccion = fila[2]
                    telefono = int(fila[3])
                    fechainicio = fila[4]
                    fechafinal = fila[5]
                    horas = int(fila[6])
                    unEmpleado = Contratado(dni, nombre, direccion, telefono, fechainicio, fechafinal, horas)
                    a = self.agregarEmpleado(unEmpleado)
                    if (a == 0): return a
        return a
        

