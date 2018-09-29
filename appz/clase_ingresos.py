import re
from datetime import datetime
from .enumeraciones.enum_msg import Msg


class Ingresos(object):

    def ingresaNumero(self, mensaje, minimo, maximo, patron):
        valor = 0
        if maximo == 0:
            rango = ", debe ser igual o mayor a {0}"
            rango = rango.format(str(minimo))
        else:
            rango = ", valores entre {0} y {1}"
            rango = rango.format(str(minimo), str(maximo))
        while True:
            print(mensaje, rango, end=": ")
            opcion = input()
            if not self.__validaExp(patron, opcion, Msg.NUMERO_INVALIDO):
                continue
            valor = int(opcion)
            if maximo == 0:
                if valor < minimo:
                    print(Msg.NUMERO_MENOR.format(str(minimo)))
                    continue
            else:
                if valor < minimo or valor > maximo:
                    print(Msg.NUMERO_FUERA_RANGO.format(
                        str(minimo), str(maximo)))
                    continue
            break
        return valor

    def __validaExp(self, patron, valor, msgError):
        if len(patron) == 0:
            return True
        if not re.match(patron, valor):
            print(msgError)
            return False
        return True

    def ingresarCadena(self, campo, patron, requerido):
        msgError = Msg.CADENA_INVALIDA.format(campo)
        while True:
            print("Ingrese", campo, end=": ")
            cadena = input()
            if requerido and len(cadena) == 0:
                print(Msg.CADENA_VACIA.format(campo))
                continue
            if not self.__validaExp(patron, cadena, msgError):
                continue
            break
        return cadena

    def ingresarCaracter(self, campo, listaOpc):
        cadena = ""
        for clave, valor in listaOpc.items():
            cadena += "'{0}': {1}, ".format(clave, valor)
        while True:
            print("Ingrese {0} [{1}]".format(
                campo, cadena.rstrip(', ')), end=": ")
            opcion = input()
            if opcion.upper() not in listaOpc:
                print(Msg.VALOR_INVALIDO)
                print(cadena.rstrip(', '))
                continue
            break
        return opcion.upper()

    def ingresarFecha(self, mensaje, minimo, maximo, patron):
        fmt = '%d/%m/%Y'
        msgError = Msg.FECHA_INVALIDA
        fecMin = self.__obtenerFecha(minimo)
        fecMax = self.__obtenerFecha(maximo)
        rango = "" if len(minimo) == 0 else ", rango ["+datetime.strftime(
            fecMin, fmt) + "-"+datetime.strftime(fecMax, fmt)
        while True:
            print(mensaje, rango, end=": ")
            fecha = input()
            if not self.__validaExp(patron, fecha, msgError):
                continue
            valor = self.__obtenerFecha(fecha)
            if len(maximo) == 0:
                if valor < fecMin:
                    print(Msg.FECHA_MENOR.format(
                        datetime.strftime(fecMin, fmt)))
                    continue
            else:
                if valor < fecMin or valor > fecMax:
                    print(Msg.FECHA_FUERA_RANGO.format(datetime.strftime(
                        fecMin, fmt), datetime.strftime(fecMax, fmt)))
                    continue
            break
        return valor


# ---
# Metodo para formatear las fechas y que sean comparables.
# ---
    def __obtenerFecha(self, valFecha):
        fmt = '%d/%m/%Y'
        fecha = datetime.strftime(datetime.now().date(), fmt)
        if len(valFecha) == 0:
            return datetime.strptime(fecha, fmt)
        return datetime.strptime(valFecha, fmt)
