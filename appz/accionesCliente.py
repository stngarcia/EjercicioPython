from .funciones import *
from .class_ingresos import Ingresos
from .clases.persona import Persona
from .enum_regexp import EnumRegExp


# ---
# Funcion para obtener los datos del cliente.
# ---
def IngresarCliente(miCliente):
    tiposDeClientes = {'N': 'Cliente normal', 'P': 'Cliente preferencial'}
    mostrarTitulo("Ingresar cliente.")
    if len(miCliente.getRut()) > 0:
        print("Datos actuales del cliente:")
        print(miCliente)
        print()
    miIngreso = Ingresos()
    miCliente.setNombre(miIngreso.ingresarCadena("nombre cliente", EnumRegExp.NOMBRE, True))
    miCliente.setRut(miIngreso.ingresarCadena("rut cliente",EnumRegExp.RUT, True))
    miCliente.setMail(miIngreso.ingresarCadena("correo electronico", EnumRegExp.EMAIL, False))
    miCliente.setTipoCliente(miIngreso.ingresarCaracter(
        "tipo de cliente", tiposDeClientes))
    PresionarEnter("El cliente ha sido creado.")
