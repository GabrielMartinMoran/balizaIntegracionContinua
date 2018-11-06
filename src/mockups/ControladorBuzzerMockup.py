import pyaudio
import numpy as np

p = pyaudio.PyAudio()

fs = 44100       # sampling rate, Hz, must be integer
duration = 1.0   # in seconds, may be float
f = 440.0        # sine frequency, Hz, may be float

class IntensidadPWMInvalidaException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class FrecuenciaPWMInvalidaException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class ControladorBuzzer:
    def __init__(self, pin_buzzer):
        self.__intensidad = 0

    def set_intensidad(self, intensidad):
        if(intensidad < 0 or intensidad > 1023):
            raise IntensidadPWMInvalidaException("La intensidad PWM debe estar entre 0 y 1023")
        self.__intensidad = intensidad/1023

    def set_frecuencia(self, frecuencia):
        if(frecuencia < 1 or frecuencia > 5000):
            raise IntensidadPWMInvalidaException("La frecuencia PWM debe estar entre 1 y 5000")
        duration = 0.150
        # generate samples, note conversion to float32 array
        samples = (np.sin(2*np.pi*np.arange(fs*duration)*frecuencia/fs)).astype(np.float32)

        # for paFloat32 sample values must be in range [-1.0, 1.0]
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1,
                        rate=fs,
                        output=True)

        # play. May repeat with different volume values (if done interactively) 
        stream.write(self.__intensidad*samples)
