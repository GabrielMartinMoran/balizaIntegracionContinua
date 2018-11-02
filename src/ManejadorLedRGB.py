from ControladorLedRGB import *
from EstadoBuild import EstadoBuild

class ColorNoEncontradoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ManejadorLedRGB:
    COLORES = {"apagado": (0, 0, 0),
                        "rojo": (255, 0, 0),
                        "verde": (0, 255, 0),
                        "azul": (0, 0, 255),
                        "blanco": (255, 255, 255),
                        "amarillo": (255, 255, 0),
                        "cyan": (0, 255, 255),
                        "magenta": (255, 0, 255)}
    COLORES_ESTADOS = {EstadoBuild.PASSED: "verde",
                        EstadoBuild.FAILED: "rojo",
                        EstadoBuild.RUNNING: "cyan",
                        EstadoBuild.CONNECTION_ERROR: "amarillo"}

    def __init__(self, configuracion_led_rgb):
        self.controlador_led_rgb = ControladorLedRGB(configuracion_led_rgb)

        self.set_color("apagado")

    def set_color(self, color):
        if(color in self.COLORES):
            rgb = self.COLORES[color]
            self.controlador_led_rgb.set_rgb(rgb)
        else:
            raise ColorNoEncontradoException("El color " + color + " no esta especificado")

    def set_estado(self, estado):
        self.set_color(self.COLORES_ESTADOS[estado])


    def get_colores(self):
        return self.COLORES
