from EstadoBuild import EstadoBuild
from ManejadorLedRGB import ManejadorLedRGB
import ColoresLed
import _thread

class EstadoALedRGB:
    COLORES_ESTADOS = {
        EstadoBuild.PASSED:             ColoresLed.VERDE,
        EstadoBuild.FAILED:             ColoresLed.ROJO,
        EstadoBuild.RUNNING:            ColoresLed.CYAN,
        EstadoBuild.CONNECTION_ERROR:   ColoresLed.AMARILLO,
        EstadoBuild.ACCESS_DENIED:      ColoresLed.MAGENTA
    }

    def __init__(self, configuracion_led_rgb):
        self.manejador_led_rgb = ManejadorLedRGB(configuracion_led_rgb)
    
    def set_estado(self, estado):
        _thread.start_new_thread(self.__set_estado,([self.COLORES_ESTADOS[estado]]))

    def __set_estado(self, estado):
        self.manejador_led_rgb.set_color(estado)

