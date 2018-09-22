# ---
# Funcion  para limpiar pantalla.
# ---
def limpiarPantalla():
    import os
    if os.name in ("ce", "nt", "dos"):
        os.system("cls")
    else:
        os.system("clear")


#---
# Mostrar un titulo en pantalla
#---
def mostrarTitulo(titulo):
    limpiarPantalla()
    print(titulo)
    for letra in titulo:
        print("-",end="")
    print()

def PresionarEnter(mensaje):
    print()
    if len(mensaje)>0:
        print(mensaje)
    print("Presione <ENTER> para continuar...", end="")
    input()
