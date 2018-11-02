from ControladorLedRGB import *
from EstadoBuild import EstadoBuild
import ColoresLed

class ColorNoEncontradoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ManejadorLedRGB:

    COLORES_ESTADOS = {
        EstadoBuild.PASSED:           ColoresLed.VERDE,
        EstadoBuild.FAILED:           ColoresLed.ROJO,
        EstadoBuild.RUNNING:          ColoresLed.CYAN,
        EstadoBuild.CONNECTION_ERROR: ColoresLed.AMARILLO
    }

    def __init__(self, configuracion_led_rgb):
        self.controlador_led_rgb = ControladorLedRGB(configuracion_led_rgb)
        self.__apagar_leds()

    def __apagar_leds(self):
        self.set_color((0,0,0))
    
    def set_color(self, valor_rgb):
        self.controlador_led_rgb.set_rgb(valor_rgb)
    
    def set_estado(self, estado):
        self.set_color(self.COLORES_ESTADOS[estado])