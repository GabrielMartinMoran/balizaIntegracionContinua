from ControladorLedRGB import *


class ColorNoEncontradoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ManejadorLedRGB:
    def __init__(self, controlador_led_rgb):
        self.controlador_led_rgb = controlador_led_rgb

        self.colores = {"apagado": (0, 0, 0),
                        "rojo": (255, 0, 0),
                        "verde": (0, 255, 0),
                        "azul": (0, 0, 255),
                        "blanco": (255, 255, 255),
                        "amarillo": (255, 255, 0),
                        "cyan": (0, 255, 255),
                        "magenta": (255, 0, 255)}

        self.set_color("apagado")

    def set_color(self, color):
        if(color in self.colores):
            rgb = self.colores[color]
            self.controlador_led_rgb.set_rgb(rgb)
        else:
            raise ColorNoEncontradoException("El color " + color + " no esta especificado")

    def get_colores(self):
        return self.colores
