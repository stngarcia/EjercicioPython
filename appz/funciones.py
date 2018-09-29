# Archivo: funciones.py
# Funciones de uso comun.

import os
from .clase_ingresos import Ingresos

# cls():
# Limpiar pantalla.


def cls():
    if os.name in ("ce", "nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")


# titulo([titulo]):
# Muestra un titulo en pantalla.
def titulo(titulo):
    cls()
    if not titulo:
        return
    print("{0:^80}".format(titulo.upper()))
    print("{0:^80}".format("-".rjust(len(titulo), '-')))
    print()


# pressEnter([mensaje]): Espera la pulsación de la tecla < ENTER >
# mostrando u mensaje(opcional).
def pressEnter(mensaje=""):
    print()
    if len(mensaje) > 0:
        print(mensaje)
    print("Presione <ENTER> para continuar...", end="")
    input()


def leee(campo, requerido, patron):
    miIngreso = Ingresos()
    return miIngreso.ingresarCadena(campo, patron, requerido)


def selecciona(campo, opciones):
    miIngreso = Ingresos()
    return miIngreso.ingresarCaracter(campo, opciones)


def leeNro(campo, minVal, maxVal, patron):
    miIngreso = Ingresos()
    return miIngreso.ingresaNumero(campo, minVal, maxVal, patron)
