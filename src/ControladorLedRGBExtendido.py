from ControladorLedRGB import ControladorLedRGB
import ColoresLed
import time

class ColorNoEncontradoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ControladorLedRGBExtendido:

    def __init__(self, configuracion_led_rgb):
        self.controlador_led_rgb = CLRGB.ControladorLedRGB(configuracion_led_rgb)
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
