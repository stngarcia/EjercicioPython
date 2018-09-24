# Archivo: funciones.py
# Funciones de uso comun.

import os


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
    if len(titulo) == 0:
        return
    print(titulo)
    print("-".rjust(len(titulo), '-'))
    print()


# pressEnter([mensaje]): Espera la pulsación de la tecla < ENTER >
# mostrando u mensaje(opcional).
def pressEnter(mensaje):
    print()
    if len(mensaje) > 0:
        print(mensaje)
    print("Presione <ENTER> para continuar...", end="")
    input()
