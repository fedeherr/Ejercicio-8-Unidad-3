from Empleado import Empleado
class Planta(Empleado):
    __sueldobas = 0
    __antiguedad = 0
    __sueldo = 0
    def __init__(self, dni, nombre, direccion, tel, sueldobas, antiguedad):
        super().__init__(dni, nombre, direccion, tel)
        self.__sueldobas = sueldobas
        self.__antiguedad = antiguedad
        self.__sueldo = self.__sueldobas + ((self.__sueldobas + self.__antiguedad)/100)
    def __str__(self):
        return "DNI: %d NOMBRE: %s DIRECCIÓN: %s" % (super().getDni(), super().getNombre(), super().getDireccion())
    def getSueldo(self):
        return self.__sueldo
    def getNombre(self):
        return super().getNombre()
    def getTel(self):
        return super().getTel()
    def setSueldo(self, suel):
        self.__sueldobas = suel
        self.__sueldo = self.__sueldobas + ((self.__sueldobas + self.__antiguedad)/100)
