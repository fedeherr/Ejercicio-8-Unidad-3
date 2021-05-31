from zope.interface import Interface
class ITesorero(Interface):
    def gastosSueldoPorEmpleado (dni):
       pass
class IGerente(Interface):
    def modificarBasicoEPlanta(dni, nuevoBasico):
        pass
    def modificarViaticoEExterno(dni, nuevoViatico):
        pass
    def modificarValorEPorHora(dni, nuevoValorHora):
        pass


def cajero(manejarVendedor):
    descripcion=input('Descripcion de producto a buscar: ')
    producto = manejarVendedor.buscarProductoPorDescripcion(descripcion)
    if producto == None:
        print('Producto {}, no encontrado'.format(descripcion))
    else:
        print(producto)
def supervisor(manejarSupervisor):
    codigo=int(input('Código del producto a cambiar precio: '))
    producto = manejarSupervisor.buscarProductoPorCodigo(codigo)
    if producto == None:
        print('No hay un Producto con código {}'.format(codigo))
    else:
        print(producto)
        precio=float(input('Nuevo precio: '))
        manejarSupervisor.modificarPrecio(codigo, precio)
        print(producto)
def testInterfaces():
    manejadorProductos = ManejadorProductos()
    unProducto=Producto(1,'Arroz 1kg',52)
    manejadorProductos.agregarProducto(unProducto)
    unProducto=Producto(2,'Yerba 1/2kg',120)
    manejadorProductos.agregarProducto(unProducto)
    usuario=input('Usuario (Admin/Cajero): ')
    clave=input('Clave:')
    if usuario.lower() == 'Admin'.lower() and clave =='a54321':
        #'''testeando supervisor '''
        supervisor(ISupervisor(manejadorProductos))
    else:
        if usuario.lower() == 'Cajero'.lower() and clave == 'c12345':
            #'''testeado cajero'''
            cajero(ICajero(manejadorProductos))
if __name__=='__main__':
    testInterfaces() 

