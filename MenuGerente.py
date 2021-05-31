from Colección import Coleccion
from Interfaces import IGerente
from Gerente import Gerente
class MenuGer(object):
    __switcher=None
    __manejoemp = None
    def __init__(self):
        self.__switcher = { 0:self.opcion0,
                            1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func()
    def opcion0(self):
        print('Chao')
    def opcion1(self):
        a = int(input("Ingrese el dni: "))
        b = int(input("Ingrese el nuevo sueldo basico: "))
        gerente(IGerente(manejadorProductos))
    def opcion2(self):
        dnie = int(input("Ingrese el DNI del empleado: "))
        hor = int(input("Ingrese las horas trabajadas hoy: "))
        self.__manejoemp.nuevaHoras(dnie, hor)
        
    def opcion3(self):
        tar = input("Ingrese la tarea a buscar: ")
        self.__manejoemp.totalTarea(tar)
