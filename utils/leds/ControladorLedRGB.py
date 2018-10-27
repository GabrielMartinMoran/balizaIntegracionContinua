from ControladorLed import *

class IntensidadInvalidaException(Exception):

    def __init__(self, mensaje):
        self.mensaje = mensaje

class ControladorLedRGB:

  def __init__(self, controladorLedR, controladorLedG, controladorLedB)
    self.controladorLedR = controladorLedR
    self.controladorLedG = controladorLedG
    self.controladorLedB = controladorLedB
    

  def set_rgb(self, rgb):
    r,g,b = rgb
    self.controladorLedR.set_intensidad(self.__map__(r))
    self.controladorLedG.set_intensidad(self.__map__(g))
    self.controladorLedB.set_intensidad(self.__map__(b))

  def __map__(self, n):
    if(n < 0 or n > 255):
        raise IntensidadInvalidaException("La intensidad del led debe estar entre 0 y 255")
    return int((float(n) / 255) * 1023)

