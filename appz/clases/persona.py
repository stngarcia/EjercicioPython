class Persona(object):
    # Constructores
    def __init__(self):
        self.rut = ""
        self.nombre = ""
        self.mail = ""
        self.tipo = ""


# ---
    # Accesadores.
# ---
    def getRut(self):
        return self.rut

    def getNombre(self):
        return self.nombre

    def getMail(self):
        return self.mail

    def getTipoCliente(self):
        if self.tipo == "N":
            return "Cliente normal"
        if self.tipo == "P":
            return "Cliente preferencial"
        return ""


# ---
    # Mutadores.
# ---
    def setRut(self, rut):
        self.rut = rut

    def setNombre(self, nombre):
        self.nombre = nombre

    def setMail(self, mail):
        self.mail = mail

    def setTipoCliente(self, tipo):
        self.tipo = tipo

    def __str__(self):
        return self.getNombre()+" "+self.getRut()+" "+self.getMail()+" "+self.getTipoCliente()
