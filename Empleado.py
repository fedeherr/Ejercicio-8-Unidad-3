class Empleado(object):
    __dni = 0
    __nombre = ''
    __direccion = ''
    __tel = 0
    def __init__(self, dni, nombre, direccion, tel):
        self.__dni = dni
        self.__nombre = nombre
        self.__direccion = direccion
        self.__tel = tel
    def getDni(self):
        return self.__dni
    def getNombre(self):
        return self.__nombre
    def getDireccion(self):
        return self.__direccion
    def getTel(self):
        return self.__tel
