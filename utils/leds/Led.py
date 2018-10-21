import machine


class NumeroInvalidoException(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje


class Led:
    def __init__(self, pin_led):
        self.pin_led = machine.PWM(machine.Pin(pin_led))
        self.set(0)

    def set(self, intensidad):
        self.intensidad = int(intensidad)
        self.pin_led.duty(self.__map__(self.intensidad))

    def __map__(self, n):
        if(n < 0 or n > 255):
            raise NumeroInvalidoException("El valor debe estar entre 0 y 255")
        return int((float(n) / 255) * 1023)
