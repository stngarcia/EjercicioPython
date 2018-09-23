from .clase_ingresos import Ingresos
from .funciones import mostrarTitulo
from .accionesCliente import *
from .accionesCreditos import *
from .clases.persona import Persona
from .clases.credito import Credito
from .enumeraciones.enum_regexp import EnumRegExp


# ---
# Clase para el manejo del menu principal.
# ---
class Menus(object):

    # ---
    # Metodo para mostrar las opciones de menu.
    # ---
    def __mostrarOpciones(self):
        mostrarTitulo("Opciones disponibles.")
        print("1. Crear crédito.")
        print("2. Datos de cliente.")
        print("3. Cambiar tipo de cliente.")
        print("4. Asignar el crédito al cliente.")
        print("5. Cambiar estado del credito.")
        print("6. Obtener meses de gracia.")
        print("7. Obtener el total a pagar.")
        print("0. Salir")
        print()


# ---
# Funcion para generar el menu principal de la aplicacion.
# ---
    def getMenuPrincipal(self):
        miCliente = Persona()
        miCredito = Credito()
        opcion = 1
        miEntrada = Ingresos()
        while opcion != 0:
            self.__mostrarOpciones()
            opcion = miEntrada.ingresarNumero(
                "Ingrese opción", 0, 7, EnumRegExp.NUMERO)
            if opcion == 1:
                IngresarCredito(miCredito)
            if opcion == 2:
                IngresarCliente(miCliente)
            if opcion==3:
                CambiarTipoCliente(miCliente)
            if opcion==4:
                AsignarCredito(miCliente,miCredito)
            if opcion == 0:
                print("Adios!")
                return
