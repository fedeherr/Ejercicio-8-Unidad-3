from Empleado import Empleado
class Externo(Empleado):
    __fecini = None
    __fecfin = None
    __tarea = ''
    __viatico = 0
    __costo = 0
    __seguro = 0
    __sueldo = 0
    def __init__(self, dni, nombre, direccion, tel, fecini, fecfin, tarea, viatico, costo, seguro):
        super().__init__(dni, nombre, direccion, tel)      
        self.__fecini = fecini
        self.__fecfin = fecfin
        self.__tarea = tarea
        self.__viatico = viatico
        self.__costo = costo
        self.__seguro = seguro
        self.__sueldo = self.__costo - self.__viatico - self.__seguro
    def getSueldo(self):
        return self.__sueldo
    def getNombre(self):
        return super().getNombre()
    def getTel(self):
        return super().getTel()
    def getDni(self):
        return super().getDni()
    def __str__(self):
        return "DNI: %d NOMBRE: %s DIRECCIÓN: %s" % (super().getDni(), super().getNombre(), super().getDireccion())
    def getTarea(self):
        return self.__tarea
    def getFechaFin(self):
        return self.__fecfin
    def setSueldo(self, suel):
        self.__viatico = suel
        self.__sueldo = self.__costo - self.__viatico - self.__seguro
