class Credito:
    def __init__(self, codigo, fechaSolicitud, fechaVencimiento, montoSolicitado,  morosidad, cuotasPagadas):
        self.__codigo = codigo
        self.__fechaSolicitud = fechaSolicitud
        self.__fechaVencimiento = fechaVencimiento
        self.__montoSolicitado = montoSolicitado
        selft.__morosidad = morosidad
        self.__cuotasPagadas = cuotasPagadas

    # Accesadores

    def getCodigo(self):
        return self.__codigo

    def getFechaSolicitud(self):
        return self.__fechaSolicitud

    def getFechaVencimiento(self):
        return self.__fechaVencimiento

    def getmontoSolicitado(self):
        return self.__montoSolicitado

    def getMorosidad(self):
        return self.__morosidad

    def getcuotasPagadas(self):
        return self.__cuotasPagadas

    # Mutadores.

    def setCodigo(self, codigo):
        self.__codigo = codigo

    def getFechaSolicitud(self, fechaSolicitud):
        self.__fechaSolicitud = fechaSolicitud

    def getFechaVencimiento(self, fechaVencimiento):
        self.__fechaVencimiento = fechaVencimiento

    def getMontoSolicitado(self, montoSolicitado):
        self.__montoSolicitado = montoSolicitado

    def getMorosidad(self, ModuleNotFoundError):
        self.__morosidad = morosidad

    def setCuotasPagadas(self):
        self.__cuotasPagadas = cuotasPagadas
