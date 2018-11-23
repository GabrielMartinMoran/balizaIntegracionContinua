from EstadoBuild import EstadoBuild
from EstadoBuild import EstadoNoEspecificadoException

class ImpresorPorConsola:

    __mensaje_de_cambio_de_estado = "CAMBIO DE ESTADO DEL BUILD A:"

    __CONSOLA_ESTADOS = {
        EstadoBuild.PASSED:             "PASSED",
        EstadoBuild.FAILED:             "FAILED",
        EstadoBuild.RUNNING:            "RUNNING",
        EstadoBuild.CONNECTION_ERROR:   "CONNECTION_ERROR",
        EstadoBuild.ACCESS_DENIED:      "ACCESS_DENIED"
    }

    def __init__(self):
        pass
    
    def set_estado(self, estado):
        if(estado in self.__CONSOLA_ESTADOS):
            print(self.__mensaje_de_cambio_de_estado, estado)
        else:
            raise EstadoNoEspecificadoException("El estado " + estado + " no esta especificado")
        