from .cuotas import Cuotas


class CuotasMorosas(Cuotas):

    def __init__(self, cuota=0, fecha='01/01/2018', monto=0, interes=0.0):
        super().__init__(cuota, fecha, monto)
        self.__interes = interes

    def getInteres(self):
        return self.__interes

    def getValorInteres(self):
        return int(self.getMonto() * self.getInteres())

    def GetTotalCuota(self):
        return (self.getMonto() + self.getValorInteres())

    def setInteres(self, interes):
        self.__interes = interes

    def str(self):
        return "Cuota {0} pagada {1} monto ${2}.-".format(super.getNumero(), super.getFecha(), super.getMonto())
