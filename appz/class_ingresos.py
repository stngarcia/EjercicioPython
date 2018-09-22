import re


# ---
# Clase para la manipulacion de los ingresos de la aplicacion
# ---
class Ingresos(object):

    # ---
    # Metodo para aceptar entradas numericas.
    # ---
    def ingresarNumero(self, minimo, maximo, patron):
        valor = 0
        while True:
            print("Ingrese valor [", minimo, "-", maximo, "]", end=": ")
            miOpcion = input()
            if not self.__ValidarFormato(patron, miOpcion, "Solo se admiten números."):
                continue
            valor = int(miOpcion)
            if valor < minimo or valor > maximo:
                print("Debe ingresar solo valores entre ", minimo, " y ", maximo)
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
    def ingresarCadena(self, campo, patron, esObligatorio):
        mensajeError = "El formato de " + campo + " no es valido."
        while True:
            print("Ingrese ", campo, end=": ")
            miOpcion = input()
            if not self.__ValidarFormato(patron, miOpcion, mensajeError):
                continue
            if esObligatorio and len(miOpcion) == 0:
                print("El campo ", campo, " no puede quedar vacio.")
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
