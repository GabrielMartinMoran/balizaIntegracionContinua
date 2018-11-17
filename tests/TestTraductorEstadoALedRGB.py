#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
from EstadoBuild import EstadoBuild
from TraductorEstadoALedRGB import TraductorEstadoALedRGB
from ConfiguracionLedRGB import ConfiguracionLedRGB

class ManejadorLedRGBMockup:

    color_a_mostrar = None

    def parpadear(self, color):
        self.color_a_mostrar = color

class TestTraductorEstadoALedRGB(unittest.TestCase):

    def test_creamos_un_traductor_y_hacemos_traducir_un_estado_valido(self):
        configuracion = ConfiguracionLedRGB()
        configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
        manejador_led_rgb = ManejadorLedRGBMockup()
        traductor = TraductorEstadoALedRGB(configuracion)
        #Cambiamos el reproductor que posee por el mockup
        traductor._TraductorEstadoALedRGB__manejador_led_rgb = manejador_led_rgb

        traductor.set_estado(EstadoBuild.PASSED)

        self.assertEqual("VERDE", manejador_led_rgb.color_a_mostrar)

        #LIMPIAMOS LA CONFIGURACION RESULTANTE
        configuracion.borrar_configuracion(True)    

    def test_creamos_un_traductor_y_hacemos_traducir_un_estado_no_valido_esperando_excepcion(self):
        configuracion = ConfiguracionLedRGB()
        configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
        manejador_led_rgb = ManejadorLedRGBMockup()
        traductor = TraductorEstadoALedRGB(configuracion)
        #Cambiamos el reproductor que posee por el mockup
        traductor._TraductorEstadoALedRGB__manejador_led_rgb = manejador_led_rgb
        #LIMPIAMOS LA CONFIGURACION RESULTANTE
        configuracion.borrar_configuracion(True)

        with self.assertRaises(EstadoNoEspecificadoException):
            traductor.set_estado("ESTADO_NO_DEFINIDO")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
