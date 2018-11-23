#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
from EstadoBuild import EstadoBuild
from EstadoBuild import EstadoNoEspecificadoException
from ManejadorLedRGB import ManejadorLedRGB
from ConfiguracionLedRGB import ConfiguracionLedRGB

class ControladorLedRGBMockup:

    color = None

    def set_rgb(self, rgb):
        self.color = rgb

    def set_color(self, color):
        self.color = color

    def apagar_led(self):
        self.color = "APAGADO"


class TestManejadorLedRGB(unittest.TestCase):

    def test_creamos_un_manejador_y_hacemos_mostrar_un_estado_valido(self):
        configuracion = ConfiguracionLedRGB()
        configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")        
        manejador = ManejadorLedRGB(configuracion)
        #Cambiamos el mockup y lo seteamos
        controlador_led_rgb = ControladorLedRGBMockup()
        manejador._ManejadorLedRGB__controlador_led_rgb = controlador_led_rgb

        COLOR_VERDE = [0,255,0]

        manejador.set_estado(EstadoBuild.PASSED)

        self.assertEqual(COLOR_VERDE, controlador_led_rgb.color)

        #LIMPIAMOS LA CONFIGURACION RESULTANTE
        configuracion.borrar_configuracion(True)    

    
    def test_creamos_un_manejador_y_hacemos_mostrar_un_estado_no_valido_esperando_excepcion(self):
        configuracion = ConfiguracionLedRGB()
        configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
        manejador = ManejadorLedRGB(configuracion)
        #LIMPIAMOS LA CONFIGURACION RESULTANTE
        configuracion.borrar_configuracion(True)

        with self.assertRaises(EstadoNoEspecificadoException):
            manejador.set_estado("ESTADO_NO_DEFINIDO")
    

def main():
    unittest.main()

if __name__ == '__main__':
    main()
