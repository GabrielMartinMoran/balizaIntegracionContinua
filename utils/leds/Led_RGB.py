import Led


class ColorNoEncontradoException(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje


class RGBLed:

    colores = {"apagado": (0, 0, 0),
               "rojo": (255, 0, 0),
               "verde": (0, 255, 0),
               "azul": (0, 0, 255),
               "blanco": (255, 255, 255)}

    leds = []

    def __init__(self, pin_r, pin_g, pin_b):
        self.leds.append(Led(pin_r))
        self.leds.append(Led(pin_g))
        self.leds.append(Led(pin_b))
        self.set("apagado")

    def set_raw(self, r, g, b):
        self.leds[0].set(r)
        self.leds[1].set(g)
        self.leds[2].set(b)

    def set(self, color):
        if(color in self.colores):
            r, g, b = self.colores[color]
            self.set_raw(r, g, b)
        else:
            raise ColorNoEncontradoException("El color " + color + " no esta especificado")
