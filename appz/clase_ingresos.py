import re
from datetime import datetime, date, timedelta


# ---
# Clase para la manipulacion de los ingresos de la aplicacion
# ---
class Ingresos(object):

    # ---
    # Metodo para aceptar entradas numericas.
    # ---
    def ingresarNumero(self, mensaje, minimo, maximo, patron):
        valor = 0
        rango = ", debe ser igual o superior a " + \
            str(minimo) if maximo == 0 else ", se admiten valores entre ["+str(
                minimo)+"-"+str(maximo)+"]"
        while True:
            print(mensaje, rango, end=": ")
            miOpcion = input()
            if not self.__ValidarFormato(patron, miOpcion, "Solo se admiten números."):
                continue
            valor = int(miOpcion)
            if maximo == 0:
                if valor < minimo:
                    print("Debe ingresar valores superiora", minimo)
                    continue
            else:
                if valor < minimo or valor > maximo:
                    print("Debe ingresar solo valores entre ",
                          minimo, " y ", maximo)
                    continue
            break
        return valor


# ---
# Validar el formato de las entradas.
# ---
    def __ValidarFormato(self, patron, valor, mensajeError):
        if len(patron) == 0:
            return True
        if re.match(patron, valor) == None:
            print(mensajeError)
            return False
        return True


# ---
# Metodo para el ingreso de cadenas de caracteres.
# ---
    def ingresarCadena(self, campo, patron, requerido):
        mensajeError = "El formato de " + campo + " no es valido."
        while True:
            print("Ingrese", campo, end=": ")
            miOpcion = input()
            if requerido and len(miOpcion) == 0:
                print("El campo ", campo, " no puede quedar vacio.")
                continue
            if not self.__ValidarFormato(patron, miOpcion, mensajeError):
                continue
            break
        return miOpcion


# ---
# Metodo que permite seleccionar el caracter de una lista de opciones.
# ---
    def ingresarCaracter(self, campo, listaCaracteres):
        cadena = ""
        for clave, valor in listaCaracteres.items():
            cadena = cadena + "'"+clave+"':"+valor+", "
        while True:
            print("Ingrese ", campo, "[" + cadena.rstrip(', '), "]", end=": ")
            miOpcion = input()
            if miOpcion.upper() not in listaCaracteres:
                print("Se admiten solo las siguientes opciones:")
                print(cadena.rstrip(', '))
                continue
            break
        return miOpcion.upper()

    # ---
    # Metodo para aceptar entradas numericas.
    # ---
    def ingresarFecha(self, mensaje, minimo, maximo, patron):
        fmt = '%d/%m/%Y'
        fechaMin = self.__obtenerFecha(minimo)
        fechaMax = self.__obtenerFecha(maximo)
        rango = "" if len(minimo) == 0 else ", rangos aceptado ["+datetime.strftime(
            fechaMin, fmt) + "-"+datetime.strftime(fechaMax, fmt)
        while True:
            print(mensaje, rango, end=": ")
            miOpcion = input()
            if not self.__ValidarFormato(patron, miOpcion, "Formato de fecha inválido, el formato es dd/mm/yyyy."):
                continue
            valor = self.__obtenerFecha(miOpcion)
            if len(maximo) == 0:
                if valor < fechaMin:
                    print("Debe ingresar una fecha superior o igual a",
                          datetime.strftime(fechaMin, fmt))
                    continue
            else:
                if valor < fechaMin or valor > fechaMax:
                    print("Debe ingresar fecha entre ", datetime.strftime(
                        fechaMin, fmt), " y ", datetime.strftime(fechaMax, fmt))
                    continue
            break
        return valor


# ---
# Metodo para formatear las fechas y que sean comparables.
# ---
    def __obtenerFecha(self, cadenaFecha):
        fmt = '%d/%m/%Y'
        fechaActual = datetime.strftime(datetime.now().date(), fmt)
        return datetime.strptime(fechaActual, fmt) if len(cadenaFecha) == 0 else datetime.strptime(cadenaFecha, fmt)
