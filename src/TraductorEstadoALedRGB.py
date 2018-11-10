from EstadoBuild import EstadoBuild
from ManejadorLedRGB import ManejadorLedRGB

class EstadoNoEspecificadoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class TraductorEstadoALedRGB:
    __COLORES_ESTADOS = {
        EstadoBuild.PASSED:             "VERDE",
        EstadoBuild.FAILED:             "ROJO",
        EstadoBuild.RUNNING:            "CYAN",
        EstadoBuild.CONNECTION_ERROR:   "AMARILLO",
        EstadoBuild.ACCESS_DENIED:      "MAGENTA"
    }

    def __init__(self, configuracion_led_rgb):
        self.__manejador_led_rgb = ManejadorLedRGB(configuracion_led_rgb)
    
    def set_estado(self, estado):
        if(estado in self.__COLORES_ESTADOS):
            self.__manejador_led_rgb.parpadear(self.__COLORES_ESTADOS[estado])
        else:
            raise EstadoNoEspecificadoException("El estado " + estado + " no esta especificado")