from ReproductorMusical import ReproductorMusical
from EstadoBuild import EstadoBuild

class EstadoNoEspecificadoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class TraductorEstadoABuzzer:

    __CANCIONES_ESTADOS = {
        EstadoBuild.PASSED:             "PASSED",
        EstadoBuild.FAILED:             "FAILED",
        EstadoBuild.RUNNING:            "RUNNING",
        EstadoBuild.CONNECTION_ERROR:   "CONNECTION_ERROR",
        EstadoBuild.ACCESS_DENIED:      "ACCESS_DENIED"
    }

    def __init__(self, configuracion_buzzer):
        self.__reproductor = ReproductorMusical(configuracion_buzzer) 
    
    def set_estado(self, estado):
        if(estado in self.__CANCIONES_ESTADOS):
            self.__reproductor.reproducir(self.__CANCIONES_ESTADOS[estado])
        else:
            raise EstadoNoEspecificadoException("La estado " + estado + " no esta especificado")