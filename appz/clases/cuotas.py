from datetime import timedelta


class Cuotas(object):
    def __init__(self, cuota=0, fecha='01/01/2018', monto=0):
        self.__cuota = cuota
        self.__fecha = fecha+timedelta(days=(30*cuota))
        self.__monto = monto

    def getNumero(self):
        return self.__cuota

    def getFecha(self):
        return self.__fecha

    def getMonto(self):
        return self.__monto

    def GetTotalCuota(self):
        return (self.getMonto())

    def setNumero(self, cuota):
        self.__cuota = cuota

    def setFecha(self, fecha):
        self.__fecha = fecha

    def setMonto(self, monto):
        self.__monto = monto

        def str(self):
            return "Cuota {0} pagada {1} monto ${2}.-".format(self.getNumero(), self.getFecha(), self.getMonto())
