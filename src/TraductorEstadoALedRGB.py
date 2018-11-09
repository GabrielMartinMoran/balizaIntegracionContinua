from EstadoBuild import EstadoBuild
from ControladorLedRGBExtendido import ControladorLedRGBExtendido
import ColoresLed

class EstadoNoEspecificadoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class TraductorEstadoALedRGB:
    
    __COLORES_ESTADOS = {
        EstadoBuild.PASSED:             ColoresLed.VERDE,
        EstadoBuild.FAILED:             ColoresLed.ROJO,
        EstadoBuild.RUNNING:            ColoresLed.CYAN,
        EstadoBuild.CONNECTION_ERROR:   ColoresLed.AMARILLO,
        EstadoBuild.ACCESS_DENIED:      ColoresLed.MAGENTA
    }

    def __init__(self, configuracion_led_rgb):
        self.__manejador_led_rgb = ControladorLedRGBExtendido(configuracion_led_rgb)
    
    def set_estado(self, estado):
        if(estado in self.__COLORES_ESTADOS):
            self.__manejador_led_rgb.parpadear(self.__COLORES_ESTADOS[estado])
        else:
            raise EstadoNoEspecificadoException("La estado " + estado + " no esta especificado")


