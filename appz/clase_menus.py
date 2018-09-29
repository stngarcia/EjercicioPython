from .accionesCliente import ingresarCliente, cambiarTipo, pagarCuota
from .accionesCliente import AsignaCredito, cambiaMorosidad, mostrarCancelado
from .accionesCreditos import ingresaCredito
from .clase_ingresos import Ingresos
from .clases.credito import Credito
from .clases.persona import Persona
from .enumeraciones.enum_regexp import Exp
from .funciones import titulo


class Menus(object):

    def __opciones(self):
        titulo("Opciones disponibles.")
        print("1. Crear crédito.")
        print("2. Datos de cliente.")
        print("3. Cambiar tipo de cliente.")
        print("4. Asignar el crédito al cliente.")
        print("5. Cambiar estado del credito.")
        print("6. Pagar cuota.")
        print("7. Obtener meses de gracia.")
        print("8. Obtener el total a pagar.")
        print("0. Salir")
        print()

    def mostrarMenu(self):
        cliente = Persona()
        credito = Credito()
        opcion = 1
        miEntrada = Ingresos()
        while opcion != 0:
            self.__opciones()
            opcion = miEntrada.ingresaNumero(
                "Ingrese opción", 0, 7, Exp.NUMERO)
            if opcion == 1:
                ingresaCredito(credito)
            if opcion == 2:
                ingresarCliente(cliente)
            if opcion == 3:
                cambiarTipo(cliente)
            if opcion == 4:
                AsignaCredito(cliente, credito)
            if opcion == 5:
                cambiaMorosidad(cliente)
            if opcion == 6:
                pagarCuota(cliente)
            if opcion == 7:
                mostrarCancelado(cliente)
            if opcion == 0:
                print("Eso fue todo, chao!")
                break
