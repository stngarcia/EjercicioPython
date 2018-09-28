from datetime import datetime
from .cuotas import Cuotas
from .cuotasMorosas import CuotasMorosas


class Credito(object):

    __interes = 0.15
    __alDia = list()
    __morosas = list()

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
        self.__montoCanceladoMoroso = 0

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
        return (len(self.__alDia)+len(self.__morosas))

    def getCuotasMorosas(self):
        return len(self.__morosas)

    def getInteresAplicado(self):
        return self.__interes

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

    def getMontoCancelado(self):
        valor = 0
        for cta in self.__alDia:
            valor = valor + cta.getMonto()
        for cta in self.__morosas:
            valor = valor+cta.getMonto()
        return valor

    def getCanceladoConMora(self):
        valor = 0
        for cta in self.__morosas:
            valor = valor + cta.getValorInteres()
        return valor

    def getListaCanceladas(self):
        if not self.__alDia:
            return
            print()
            print()
            print("Cuotas canceladas al día.")
        print("Cuota\tFecha\t\tMonto")
        for cta in self.__alDia:
            print("{0:^5}\t{1:%d/%m/%Y}\t${2:>10}.-".format(cta.getNumero(),
                                                            cta.getFecha(), cta.getMonto()))

    def getListaMorosas(self):
        if not self.__morosas:
            return
            print()
            print()
            print("Cuotas morosas canceladas.")
        print("Cuota\tFecha\t\tMonto\t\tInterés\tValor interés\tTotal cancelado")
        for cta in self.__morosas:
            print("{0:^5}\t{1:%d/%m/%Y}\t${2:>10}.-\t{3:.2f}\t${4:>10}.-\t${5:>10}.-".format(cta.getNumero(),
                                                                                             cta.getFecha(), cta.getMonto(), cta.getInteres(), cta.getValorInteres(),  cta.GetTotalCuota()))

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
        if not self.getMorosidad():
            miCuota = Cuotas(cuotasPagadas, self.__fechaSolicitud,
                             self.getValorCuota())
            self.__alDia.append(miCuota)
        else:
            miCuota = CuotasMorosas(cuotasPagadas, self.__fechaSolicitud,
                                    self.getValorCuota(), self.__interes)
            self.__morosas.append(miCuota)

    def existe(self):
        return True if self.__codigo else False

    def checkCodigo(self, codigo):
        return True if self.getCodigo() == codigo else False

    def getEstadoCuota(self):
        if not self.getMorosidad():
            miCuota = CuotasMorosas(self.__cuotasPagadas+1, self.__fechaSolicitud,
                                    self.getValorCuota())
        else:
            miCuota = CuotasMorosas(self.__cuotasPagadas+1, self.__fechaSolicitud,
                                    self.getValorCuota(), self.__interes)
        print("Número de cuota a pagar: {0} ".format(miCuota.getNumero()))
        print("Valor cuota ${0}.-".format(miCuota.getMonto()))
        print("Interés a aplicar {0:.2f}% (${1}.-)".format(
            miCuota.getInteres(), miCuota.getValorInteres()))
        print("Total a pagar ${0}.-".format(miCuota.GetTotalCuota()))

    def getDatos(self):
        print("Datos de credito")
        print("-".rjust(80, '-'))
        print("Código: ", self.getCodigo(), sep="\t\t")
        print("Fecha solicitud {0:%d/%m/%Y} \t Fecha vencimiento {1:%d/%m/%Y} ".format(
            self.getFechaSolicitud(), self.getFechaVencimiento()))
        print("Monto ${0}.- \t\t Cuotas pactadas: {1}".format(
            self.getMonto(),  self.getCuotasPactadas()))
        print("Valor cuota ${0}.- \t\t Cuotas pagadas: {1}".format(
            self.getValorCuota(), self.getCuotasPagadas()))
        print("Tiene morosidad:", self.getMorosidad())
        if self.fuePagado():
            print("Credito finalizado!")
        print("-".rjust(80, '-'))
        print()

    def __str__(self):
        cadena = "Crédito {0:<6}, solicitado {1:%d/%m/%Y} monto ${2} termina el {3:%d/%m/%Y}"
        cadena.format(self.getCodigo(), self.getFechaSolicitud(
        ), self.getMonto(), self.getFechaVencimiento())
        return cadena
