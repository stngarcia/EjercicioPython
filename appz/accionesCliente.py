import copy
from .clase_ingresos import Ingresos
from .enumeraciones.enum_regexp import EnumRegEx
from .funciones import pressEnter, titulo


def ingresarCliente(cliente):
    __cabecera(cliente)
    __leerDatos(cliente)
    pressEnter("El cliente ha sido creado.")


def __cabecera(cliente):
    if cliente.existe():
        titulo("")
        cliente.getDatos()
    else:
        titulo("Ingresar cliente.")


def __leerDatos(cliente):
    miIngreso = Ingresos()
    cliente.setNombre(__leeNombre(miIngreso))
    cliente.setRut(__leeRut(miIngreso))
    cliente.setMail(__leeMail(miIngreso))
    cliente.setTipo(__leeTipo(miIngreso))


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
    if not cliente.existe():
        pressEnter("No se ha ingresado un cliente para cambiar su tipo.")
        return
    __cambiaTipo(cliente)
    pressEnter("El tipo de cliente ha sido cambiado.")


def __cambiaTipo(cliente):
    miIngreso = Ingresos()
    cliente.setTipo(__leeTipo(miIngreso))


def AsignaCredito(cliente, credito):
    titulo("Asignación de credito a cliente.")
    __muestraClienteCredito(cliente, credito)
    if not cliente.existe() or not credito.existe():
        pressEnter(__msgAsignacion(cliente, credito))
        return
    if cliente.getCredito().checkCodigo(credito.getCodigo()):
        pressEnter("El cliente ya posee el crédito.")
        return
    if cliente.getCredito().estaPagando():
        pressEnter("Cliente esta pagando el crédito, no puede asignar otro.")
        return
    miOpcion = __leeAsignacion()
    if miOpcion == "N":
        pressEnter("El crédito no se asocio.")
        return
    cliente.setCredito(copy.copy(credito))
    pressEnter("Crédito fue asociado al cliente.")


def __muestraClienteCredito(cliente, credito):
    if cliente.existe():
        cliente.getDatos()
    if credito.existe():
        credito.getDatos()


def __leeAsignacion():
    miIngreso = Ingresos()
    misOpciones = {'S': 'Asociar crédito', 'N': 'No asociar'}
    campo = "opción"
    return miIngreso.ingresarCaracter(campo, misOpciones)


def __msgAsignacion(cliente, credito):
    if not cliente.existe() and not credito.existe():
        return"No hay cliente ni crédito ingresado."
    if not cliente.existe():
        return "No hay un cliente ingresado."
    if not credito.existe():
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
    if not cliente.existe():
        pressEnter("No hay cliente ingresado")
        return False
    cliente.getDatos()
    if not cliente.getCredito().existe():
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
        if cliente.getCredito().fuePagado():
            pressEnter("Cliente finalizo el crédito, venda otro altiro!!")
            break
        print("Pagar cuota número", cuota + 1)
        cliente.getCredito().getEstadoCuota()
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
