from .credito import Credito


class Persona(object):
    # Constructores
    def __init__(self):
        self.__rut = ""
        self.__nombre = ""
        self.__mail = ""
        self.__tipo = ""
        self.__credito = Credito()


# ---
    # Accesadores.
# ---
    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def getMail(self):
        return self.__mail

    def getTipoCliente(self):
        if self.__tipo == "N":
            return "Cliente normal"
        if self.__tipo == "P":
            return "Cliente preferencial"
        return ""

    def getCredito(self):
        return self.__credito


# ---
    # Mutadores.
# ---
    def setRut(self, rut):
        self.__rut = rut

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setMail(self, mail):
        self.__mail = mail

    def setTipoCliente(self, tipo):
        self.__tipo = tipo

    def setCredito(self, credito):
        self.__credito = credito


# ---
# Metodo para indicar si hay un cliente ingresado.
# ---
    def existeCliente(self):
        return False if len(self.getRut()) == 0 else True


# ---
# Metodo que indica si el cliente tiene un credito asociado.
# ---
    def tieneCredito(self):
        return False if len(self.__credito.getCodigoCredito()) == 0 else True


# ---
# Metodo para mostrar los datos del cliente.
# ---
    def mostrarDatos(self):
        print("Datos del cliente.")
        print("-".rjust(80, '-'))
        self.__visualizarCliente()
        self.__visualizarCredito()
        print("-".rjust(80, '-'))
        print()


# ---
#
# ---
    def __visualizarCliente(self):
        print("Nombre: ", self.getNombre())
        print("Rut: ", self.getRut())
        print("E-Mail: ", self.getMail())
        print("Tipo de cliente: ", self.getTipoCliente())

# ---
# Visualiza los datos del credito del cliente.
# ---
    def __visualizarCredito(self):
        if self.tieneCredito():
            print()
            self.__credito.mostrarDatos()
        else:
            print("Cliente sin credito asociado.")


# ---
# Metodo str muestra el nombre del cliente y el tipo.
# ---
    def __str__(self):
        return self.getNombre()+" "+self.getTipoCliente()
