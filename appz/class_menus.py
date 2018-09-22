from .class_ingresos import Ingresos
from .funciones import mostrarTitulo
from .accionesCliente import *
from .clases.persona import Persona
from .enum_regexp import EnumRegExp


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
        print("3. Obtener mese de gracia.")
        print("4. Obtener el total a pagar.")
        print("0. Salir")
        print()


# ---
# Funcion para generar el menu principal de la aplicacion.
# ---
    def getMenuPrincipal(self):
        miCliente = Persona()
        opcion = 1
        miEntrada = Ingresos()
        while opcion != 0:
            self.__mostrarOpciones()
            opcion = miEntrada.ingresarNumero(0, 4, EnumRegExp.NUMERO)
            if opcion == 2:
                IngresarCliente(miCliente)
            if opcion == 0:
                print("Adios!")
                return
