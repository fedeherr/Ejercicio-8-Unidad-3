from zope.interface import Interface
from zope.interface import implementer

class IGerente (Interface):

    def modificarBasicoEPlanta(dni, nuevoBasico):
        pass

    def modificarViaticoEExterno(dni, nuevoViatico):
        pass

    def modificarValorEPorHora( nuevoValorHora):
        pass