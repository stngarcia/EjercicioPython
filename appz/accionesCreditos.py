from datetime import datetime, timedelta
from .funciones import *
from .clase_ingresos import Ingresos
from .clases.credito import Credito
from .enumeraciones.enum_regexp import EnumRegExp


# ---
# Funcion para ingresar datos del credito.
# ---
def IngresarCredito(miCredito):
    __MostrarCabecera(miCredito)
    __RealizarIngreso(miCredito)
    PresionarEnter("El crédito ha sido creado.")


# ---
# Mostrar cabecera del ingreso.
# ---
def __MostrarCabecera(miCredito):
    if miCredito.existeCredito():
        mostrarTitulo("")
        miCredito.mostrarDatos()
    else:
        mostrarTitulo("Ingresar crédito.")


# ---
# Realiza el ingreso de datos del cliente.
# ---
def __RealizarIngreso(miCredito):
    miIngreso = Ingresos()
    miCredito.setCodigoCredito(__IngresarCodigo(miIngreso))
    miCredito.setFechaSolicitud(__IngresarFechaSolicitud(miIngreso))
    miCredito.setFechaVencimiento(__IngresarFechaVencimiento(
        miIngreso, miCredito.getFechaSolicitud()))
    miCredito.setMonto(__IngresarMontoSolicitado(miIngreso))


# ---
# Funcion para el ingreso del codigo del credito.
# ---
def __IngresarCodigo(miIngreso):
    campo = "Código crédito"
    requerido = True
    patron = EnumRegExp.CODIGO
    return miIngreso.ingresarCadena(campo, patron, requerido)


# ---
# Funcion para el ingreso de la fecha de solicitud.
# ---
def __IngresarFechaSolicitud(miIngreso):
    campo = "fecha de solicitud"
    patron = EnumRegExp.FECHA
    return miIngreso.ingresarFecha(campo, "", "", patron)


# ---
# Funcion para el ingreso de la fecha de solicitud.
# ---
def __IngresarFechaVencimiento(miIngreso, fechaInicio):
    campo = "fecha de vencimiento"
    fechaInicial = datetime.strftime(
        fechaInicio+timedelta(days=(30*12)), '%d/%m/%Y')
    fechaFinal = datetime.strftime(
        fechaInicio+timedelta(days=(30*120)), '%d/%m/%Y')
    patron = EnumRegExp.FECHA
    return miIngreso.ingresarFecha(campo, fechaInicial, fechaFinal, patron)


# ---
# Funcion para el ingreso del monto solicitado.
# ---
def __IngresarMontoSolicitado(miIngreso):
    campo = "monto solicitado"
    requerido = True
    patron = EnumRegExp.NUMERO
    return miIngreso.ingresarNumero(campo, 6000000, 0, patron)
