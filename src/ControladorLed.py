from machine import PWM, Pin


class IntensidadPWMInvalidaException(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje


class ControladorLed:
    def __init__(self, pin_led):
        self.pin_led = PWM(Pin(pin_led))
        self.set_intensidad(0)

    def set_intensidad(self, intensidad):
        if(intensidad < 0 or intensidad > 1023):
            raise IntensidadPWMInvalidaException("La intensidad PWM debe estar entre 0 y 1023")
        self.pin_led.duty(intensidad)
