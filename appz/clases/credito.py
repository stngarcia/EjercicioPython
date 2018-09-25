from datetime import datetime


class Credito(object):

    __interes = 0.15

    def __init__(self):
        self.__fmt = '%d/%m/%Y'
        self.__codigo = ""
        self.__fechaSolicitud = datetime.strptime('01/01/2018', self.__fmt)
        self.__fechaVencimiento = datetime.strptime('01/01/2018', self.__fmt)
        self.__montoSolicitado = 0
        self.__morosidad = False
        self.__cuotasPagadas = 0
        self.__cuotasMorosas = 1
        self.__montoCancelado = 0

    def getCodigo(self):
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
        if self.getMorosidad():
            self.__cuotasMorosas + 1
        return self.__cuotasPagadas

    def getCuotasMorosas(self):
        self.__cuotasMorosas

    def getCuotasPactadas(self):
        diferencia = int((self.getFechaVencimiento() -
                          self.getFechaSolicitud()).days)
        cuotas = int((diferencia/30))
        return cuotas

    def fuePagado(self):
        return True if self.getCuotasPactadas() == self.getCuotasPagadas() else False

    def estaPagando(self):
        if self.fuePagado():
            return False
        return True if self.getCuotasPagadas() > 0 else False

    def getValorCuota(self):
        valor = int(self.getMonto()/self.getCuotasPactadas())
        return valor

    def getValorInteres(self):
        valor = 0
        if self.getMorosidad():
            valor = int(self.getValorCuota() *
                        (self.__interes * self.__cuotasMorosas))
        return valor

    def getMontoCancelado(self):
        return self.__montoCancelado

    def setCodigo(self, codigo):
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
        valorCancelado = self.getValorCuota()
        if self.getMorosidad():
            self.__cuotasMorosas = self.__cuotasMorosas+1
            valorCancelado = valorCancelado + self.getValorInteres()
        self.__montoCancelado = self.__montoCancelado+valorCancelado

    def existe(self):
        return False if len(self.__codigo) == 0 else True

    def checkCodigo(self, codigo):
        return True if self.getCodigo() == codigo else False

    def getEstadoCuota(self):
        print("Valor cuota ${0}.-".format(self.getValorCuota()))
        if self.getMorosidad():
            valorInteres = self.getValorInteres()
            print(
                "Interés aplicado {0} %: ${1}.- ".format((self.__interes*self.__cuotasMorosas), valorInteres))
            print(
                "Total valor cuota a pagar ${0}.-".format((self.getValorCuota()+valorInteres)))

    def getDatos(self):
        print("Datos de credito")
        print("-".rjust(80, '-'))
        print("Código: ", self.getCodigo())
        print("Fecha solicitud: ", datetime.strftime(
            self.getFechaSolicitud(), self.__fmt))
        print("Fecha vencimiento: ", datetime.strftime(
            self.getFechaVencimiento(), self.__fmt))
        print("Monto $", self.getMonto())
        print("Cuotas pactadas: ", self.getCuotasPactadas())
        print("Valor cuota $", self.getValorCuota())
        print("Tiene morosidad:", self.getMorosidad())
        print("Cuotas pagadas:", self.getCuotasPagadas())
        if self.fuePagado():
            print("Credito finalizado!")
        print("-".rjust(80, '-'))
        print()

    def __str__(self):
        cadena = "Crédito {0}, solicitado {1} monto ${2} termina el {3}"
        cadena.format(self.getCodigo(), self.getFechaSolicitud(
        ), self.getMonto(), self.getFechaVencimiento())
        return cadena
