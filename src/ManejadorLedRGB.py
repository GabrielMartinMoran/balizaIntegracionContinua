from ControladorLedRGB import *
from EstadoBuild import EstadoBuild
import ColoresLed
import time

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
        self.__apagar_led()

    def __apagar_led(self):
        self.set_color((0,0,0))
    
    def set_color(self, valor_rgb):
        self.controlador_led_rgb.set_rgb(valor_rgb)
    
    def parpadear(self, valor_rgb):
        for i in range(3):
            self.set_color(valor_rgb)
            time.sleep(0.2)
            self.__apagar_led()
            time.sleep(0.2)
        self.set_color(valor_rgb)

    def set_estado(self, estado):
        self.parpadear(self.COLORES_ESTADOS[estado])