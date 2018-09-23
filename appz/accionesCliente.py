import copy
from .funciones import *
from .clase_ingresos import Ingresos
from .clases.persona import Persona
from.clases.credito import Credito
from .enumeraciones.enum_regexp import EnumRegExp


# ---
# Funcion para ingresar datos del cliente.
# ---
def IngresarCliente(miCliente):
    __mostrarCabecera(miCliente)
    __RealizarIngreso(miCliente)
    PresionarEnter("El cliente ha sido creado.")


# ---
# Mostrar cabecera del ingreso.
# ---
def __mostrarCabecera(miCliente):
    if miCliente.existeCliente():
        mostrarTitulo("")
        miCliente.mostrarDatos()
    else:
        mostrarTitulo("Ingresar cliente.")


# ---
# Realiza el ingreso de datos del cliente.
# ---
def __RealizarIngreso(miCliente):
    miIngreso = Ingresos()
    miCliente.setNombre(__IngresarNombre(miIngreso))
    miCliente.setRut(__IngresarRut(miIngreso))
    miCliente.setMail(__IngresarMail(miIngreso))
    miCliente.setTipoCliente(__IngresarTipoCliente(miIngreso))


# ---
# Funcion para el ingreso del nombre.
# ---
def __IngresarNombre(miIngreso):
    campo = "nombre cliente"
    requerido = True
    patron = EnumRegExp.NOMBRE
    return miIngreso.ingresarCadena(campo, patron, requerido).title()


# ---
# Funcion para el ingreso del rut.
# ---
def __IngresarRut(miIngreso):
    campo = "rut cliente"
    requerido = True
    patron = EnumRegExp.RUT
    return miIngreso.ingresarCadena(campo, patron, requerido)


# ---
# Funcion para el ingreso del email.
# ---
def __IngresarMail(miIngreso):
    campo = "e-mail"
    requerido = False
    patron = EnumRegExp.EMAIL
    return miIngreso.ingresarCadena(campo, patron, requerido)


# ---
# Funcion para ingresar el tipo de cliente.
# ---
def __IngresarTipoCliente(miIngreso):
    tipos = {'N': 'Cliente normal', 'P': 'Cliente preferencial'}
    campo = "tipo de cliente"
    return miIngreso.ingresarCaracter(campo, tipos)


# ---
# Funcion parapara la opcion de cambio de tipo de cliente.
# ---
def CambiarTipoCliente(miCliente):
    __mostrarCabecera(miCliente)
    if miCliente.existeCliente():
        __RealizarCambioTipo(miCliente)
        PresionarEnter("El tipo de cliente ha sido cambiado.")
    else:
        PresionarEnter("No se ha ingresado un cliente para cambiar su tipo.")


# ---
# Cambiar el tipo de cliente.
# ---
def __RealizarCambioTipo(miCliente):
    miIngreso = Ingresos()
    miCliente.setTipoCliente(__IngresarTipoCliente(miIngreso))


# ---
# Asignar un credito al cliente.
# ---
def AsignarCredito(miCliente, miCredito):
    mostrarTitulo("Asignación de credito a cliente.")
    __VisualizarClienteCredito(miCliente, miCredito)
    if miCliente.existeCliente() and miCredito.existeCredito():
        mensaje = ""
        if miCliente.getCredito().getCodigoCredito()==miCredito.getCodigoCredito():
            PresionarEnter("El cliente ya posee el crédito.")
            return
        miOpcion = __IngresarOpcionDeAsignacion()
        if miOpcion == "S":
            miCliente.setCredito(copy.copy(miCredito))
            mensaje = "Crédito fue asociado al cliente."
        else:
            mensaje = "El crédito no se asocio."
        PresionarEnter(mensaje)
    else:
        PresionarEnter(__ErrorAsignacion(miCliente, miCredito))


# ---
# Mostrar datos de cliente y credito para la asignacion.
# ---
def __VisualizarClienteCredito(miCliente, miCredito):
    if miCliente.existeCliente():
        miCliente.mostrarDatos()
    if miCredito.existeCredito():
        miCredito.mostrarDatos()


# ---
# Funcion para ingresaropcion de asignacion.
# ---
def __IngresarOpcionDeAsignacion():
    miIngreso = Ingresos()
    misOpciones = {'S': 'Asociar crédito', 'N': 'No asociar'}
    campo = "opción"
    return miIngreso.ingresarCaracter(campo, misOpciones)


# ---
# Muestra el mensaje de error de la asociacion.
# ---
def __ErrorAsignacion(miCliente, miCredito):
    if not miCliente.existeCliente() and not miCredito.existeCredito():
        return"No hay cliente ni crédito ingresado."
    if not miCliente.existeCliente():
        return "No hay un cliente ingresado."
    if not miCredito.existeCredito():
        return "No hay un crédito ingresado."
    return""
