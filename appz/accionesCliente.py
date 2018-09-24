import copy
from .clase_ingresos import Ingresos
from .enumeraciones.enum_regexp import EnumRegEx
from .funciones import pressEnter, titulo


def ingresarCliente(cliente):
    __cabecera(cliente)
    __leerDatos(cliente)
    pressEnter("El cliente ha sido creado.")


def __cabecera(cliente):
    if cliente.existeCliente():
        titulo("")
        cliente.mostrarDatos()
    else:
        titulo("Ingresar cliente.")


def __leerDatos(cliente):
    miIngreso = Ingresos()
    cliente.setNombre(__leeNombre(miIngreso))
    cliente.setRut(__leeRut(miIngreso))
    cliente.setMail(__leeMail(miIngreso))
    cliente.setTipoCliente(__leeTipo(miIngreso))


def __leeNombre(miIngreso):
    campo = "nombre cliente"
    requerido = True
    patron = EnumRegEx.NOMBRE
    return miIngreso.ingresarCadena(campo, patron, requerido).title()


def __leeRut(miIngreso):
    campo = "rut cliente"
    requerido = True
    patron = EnumRegEx.RUT
    return miIngreso.ingresarCadena(campo, patron, requerido)


def __leeMail(miIngreso):
    campo = "e-mail"
    requerido = False
    patron = EnumRegEx.EMAIL
    return miIngreso.ingresarCadena(campo, patron, requerido)


def __leeTipo(miIngreso):
    tipos = {'N': 'Cliente normal', 'P': 'Cliente preferencial'}
    campo = "tipo de cliente"
    return miIngreso.ingresarCaracter(campo, tipos)


def cambiarTipo(cliente):
    __cabecera(cliente)
    if not cliente.existeCliente():
        pressEnter("No se ha ingresado un cliente para cambiar su tipo.")
        return
    __cambiaTipo(cliente)
    pressEnter("El tipo de cliente ha sido cambiado.")


def __cambiaTipo(cliente):
    miIngreso = Ingresos()
    cliente.setTipoCliente(__leeTipo(miIngreso))


def AsignaCredito(cliente, credito):
    titulo("Asignación de credito a cliente.")
    __muestraClienteCredito(cliente, credito)
    if not cliente.existeCliente() or not credito.existeCredito():
        pressEnter(__msgAsignacion(cliente, credito))
        return
    if cliente.getCredito().getCodigoCredito() == credito.getCodigoCredito():
        pressEnter("El cliente ya posee el crédito.")
        return
    pagadas = cliente.getCredito().getCuotasPagadas()
    pactadas = cliente.getCredito().getCuotasPactadas()
    if (pactadas-pagadas) != 0:
        pressEnter("Cliente esta pagando el crédito, no puede asignar otro.")
        return
    miOpcion = __leeAsignacion()
    if miOpcion == "N":
        pressEnter("El crédito no se asocio.")
        return
    cliente.setCredito(copy.copy(credito))
    pressEnter("Crédito fue asociado al cliente.")


def __muestraClienteCredito(cliente, credito):
    if cliente.existeCliente():
        cliente.mostrarDatos()
    if credito.existeCredito():
        credito.mostrarDatos()


def __leeAsignacion():
    miIngreso = Ingresos()
    misOpciones = {'S': 'Asociar crédito', 'N': 'No asociar'}
    campo = "opción"
    return miIngreso.ingresarCaracter(campo, misOpciones)


def __msgAsignacion(cliente, credito):
    if not cliente.existeCliente() and not credito.existeCredito():
        return"No hay cliente ni crédito ingresado."
    if not cliente.existeCliente():
        return "No hay un cliente ingresado."
    if not credito.existeCredito():
        return "No hay un crédito ingresado."
    return""


def cambiaMorosidad(cliente):
    titulo("Cambiar el estado del crédito.")
    if not __verificaCliente(cliente):
        return
    miOpcion = __leerEstado()
    credito = cliente.getCredito()
    credito.setMorosidad(False if miOpcion == "A" else True)
    pressEnter("El estado del crédito del cliente ha cambiado.")


def __verificaCliente(cliente):
    if not cliente.existeCliente():
        pressEnter("No hay cliente ingresado")
        return False
    cliente.mostrarDatos()
    if not cliente.getCredito().existeCredito():
        pressEnter("El cliente no tiene un crédito asociado")
        return False
    return True


def __leerEstado():
    miIngreso = Ingresos()
    misOpciones = {'M': 'Cliente moroso', 'A': 'Cliente al día'}
    campo = "opción"
    return miIngreso.ingresarCaracter(campo, misOpciones)


def pagarCuota(cliente):
    while True:
        titulo("Pagar cuota de credito.")
        if not __verificaCliente(cliente):
            break
        cuota = cliente.getCredito().getCuotasPagadas()
        if cuota == cliente.getCredito().getCuotasPactadas():
            pressEnter(
                "Cliente finalizo el crédito, venda otro altiro!!")
            break
        print("Pagar cuota número", cuota + 1)
        opcion = __leerPago()
        if opcion == "X":
            break
        cuota = cuota+1
        cliente.getCredito().setCuotasPagadas(cuota)


def __leerPago():
    miIngreso = Ingresos()
    misOpciones = {'P': 'Pagar una cuota', 'X': 'Salir de pagos'}
    campo = "opción"
    return miIngreso.ingresarCaracter(campo, misOpciones)
