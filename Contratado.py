from Empleado import Empleado
class Contratado(Empleado):
    __fecini = None
    __fecfin = None
    __sueldo = 0
    __horas = 0
    __pagohora = 300
    def __init__(self, dni, nombre, direccion, tel, fecini, fecfin, horas):
        super().__init__(dni, nombre, direccion, tel)
        self.__fecini = fecini
        self.__fecfin = fecfin
        self.__pagohora = 300
        self.__horas = horas
        self.__sueldo = 0
    def getSueldo(self):
        self.__sueldo = self.__horas * self.__pagohora
        return self.__sueldo
    def getDni(self):
        return super().getDni()
    def getNombre(self):
        return super().getNombre()
    def getTel(self):
        return super().getTel()
    def cambioHora(self, horas):
        self.__horas += horas
    def setSueldo(self, horas):
        self.__pagohoras = horas
        self.__sueldo = self.__horas * self.__pagohora
    def __str__(self):
        return "DNI: %d NOMBRE: %s DIRECCIÓN: %s" % (super().getDni(), super().getNombre(), super().getDireccion())
    