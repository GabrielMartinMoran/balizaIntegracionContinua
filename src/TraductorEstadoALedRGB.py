from EstadoBuild import EstadoBuild
from ControladorLedRGBExtendido import ControladorLedRGBExtendido

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
        self.__controlador_led_rgb_extendido = ControladorLedRGBExtendido(configuracion_led_rgb)
    
    def set_estado(self, estado):
        if(estado in self.__COLORES_ESTADOS):
            self.__controlador_led_rgb_extendido.parpadear(self.__COLORES_ESTADOS[estado])
        else:
            raise EstadoNoEspecificadoException("El estado " + estado + " no esta especificado")