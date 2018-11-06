from EstadoBuild import EstadoBuild
from ManejadorLedRGB import ManejadorLedRGB
import ColoresLed

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
        self.manejador_led_rgb.parpadear(self.COLORES_ESTADOS[estado])


