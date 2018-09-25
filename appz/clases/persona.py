from .credito import Credito


class Persona(object):

    def __init__(self):
        self.__rut = ""
        self.__nombre = ""
        self.__mail = ""
        self.__tipo = ""
        self.__credito = Credito()

    def getRut(self):
        return self.__rut

    def getNombre(self):
        return self.__nombre

    def getMail(self):
        return self.__mail

    def getTipo(self):
        if self.__tipo == "N":
            return "Cliente normal"
        if self.__tipo == "P":
            return "Cliente preferencial"
        return ""

    def getCredito(self):
        return self.__credito

    def setRut(self, rut):
        self.__rut = rut

    def setNombre(self, nombre):
        self.__nombre = nombre

    def setMail(self, mail):
        self.__mail = mail

    def setTipo(self, tipo):
        self.__tipo = tipo

    def setCredito(self, credito):
        self.__credito = credito

    def existe(self):
        return False if len(self.getRut()) == 0 else True

    def conCredito(self):
        return False if len(self.getCredito().getCodigo()) == 0 else True

    def getDatos(self):
        print("Datos del cliente.")
        print("-".rjust(80, '-'))
        self.__verCliente()
        self.__verCredito()
        print("-".rjust(80, '-'))
        print()

    def __verCliente(self):
        print("Nombre: ", self.getNombre())
        print("Rut: ", self.getRut())
        print("E-Mail: ", self.getMail())
        print("Tipo de cliente: ", self.getTipo())

    def __verCredito(self):
        if self.conCredito():
            print()
            self.getCredito().getDatos()
        else:
            print("Cliente sin credito asociado.")

    def __str__(self):
        return self.getNombre()+" "+self.getTipo()
