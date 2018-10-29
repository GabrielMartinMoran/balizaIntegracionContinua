import machine


class IntensidadPWMInvalidaException(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje


class FrecuenciaPWMInvalidaException(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje


class ControladorBuzzer:
    def __init__(self, pin_buzzer):
        self.pin_buzzer = machine.PWM(machine.Pin(pin_buzzer))
        self.set_intensidad(0)
        self.set_frecuencia(1)

    def set_intensidad(self, intensidad):
        if(intensidad < 0 or intensidad > 1023):
            raise IntensidadPWMInvalidaException("La intensidad PWM debe estar entre 0 y 1023")
        self.pin_buzzer.duty(intensidad)

    def set_frecuencia(self, frecuencia):
        if(frecuencia < 1 or frecuencia > 5000):
            raise IntensidadPWMInvalidaException("La frecuencia PWM debe estar entre 1 y 5000")
        self.pin_buzzer.freq(frecuencia)
