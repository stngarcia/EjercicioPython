from datetime import datetime


class Credito(object):

    # ---
    # Constructor.
    # ---
    def __init__(self):
        self.__codigo = ""
        self.__fechaSolicitud = datetime.strptime('01/01/2018', '%d/%m/%Y')
        self.__fechaVencimiento = datetime.strptime('01/01/2018', '%d/%m/%Y')
        self.__montoSolicitado = 0
        self.__morosidad = False
        self.__cuotasPagadas = 0


# ---
# Accesadores.
# ---
    def getCodigoCredito(self):
        return self.__codigo

    def getFechaSolicitud(self):
        return self.__fechaSolicitud

    def getFechaVencimiento(self):
        return self.__fechaVencimiento

    def getMonto(self):
        return self.__montoSolicitado

    def getMorosidad(self):
        return self.__morosidad

    def getCuotasPagadas(self):
        return self.__cuotasPagadas

    def getCuotasPactadas(self):
        diferencia = int((self.getFechaVencimiento() -
                          self.getFechaSolicitud()).days)
        cuotas = int((diferencia/30))
        return cuotas

    def getValorCuota(self):
        valor = int(self.getMonto()/self.getCuotasPactadas())
        return valor


# ---
# Mutadores.
# ---
    def setCodigoCredito(self, codigo):
        self.__codigo = codigo

    def setFechaSolicitud(self, fechaSolicitud):
        self.__fechaSolicitud = fechaSolicitud

    def setFechaVencimiento(self, fechaVencimiento):
        self.__fechaVencimiento = fechaVencimiento

    def setMonto(self, monto):
        self.__montoSolicitado = monto

    def setMorosidad(self, morosidad):
        self.__morosidad = morosidad

    def setCuotasPagadas(self, cuotasPagadas):
        self.__cuotasPagadas = cuotasPagadas


# ---
# Metodo que indica si hay un credito ingresado.
# ---
    def existeCredito(self):
        if len(self.getCodigoCredito()) == 0:
            return False
        return True


# ---
# Customers.
# ---
    def mostrarDatos(self):
        fmt = '%d/%m/%Y'
        print("Datos de credito")
        print("-".rjust(80, '-'))
        print("Código: ", self.getCodigoCredito())
        print("Fecha solicitud: ", datetime.strftime(
            self.getFechaSolicitud(), fmt))
        print("Fecha vencimiento: ", datetime.strftime(
            self.getFechaVencimiento(), fmt))
        print("Monto $", self.getMonto())
        print("Cuotas pactadas: ", self.getCuotasPactadas())
        print("Valor cuota $", self.getValorCuota())
        print("Tiene morosidad:", self.getMorosidad())
        print("Cuotas pagadas:", self.getCuotasPagadas())
        if self.getCuotasPactadas() == self.getCuotasPagadas():
            print("Credito finalizado!")
        print("-".rjust(80, '-'))
        print()


# ---
# Metodo str
# muestra el codigo del credito las fechas de solicitud y vencimiento
#  junto con el monto.
# ---
    def __str__(self):
        cadena = "Crédito {0}, solicitado {1} monto ${2} termina el {3}"
        cadena.format(self.getCodigoCredito(), self.getFechaSolicitud(
        ), self.getMonto(), self.getFechaVencimiento())
        return cadena
