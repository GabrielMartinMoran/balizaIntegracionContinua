#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
from EstadoBuild import EstadoBuild
from TraductorEstadoABuzzer import *
from ConfiguracionBuzzer import ConfiguracionBuzzer

class ReproductorMusicalMockup:

	cancion_a_reproducir = None

	def reproducir(self, cancion):
		self.cancion_a_reproducir = cancion

class TestTraductorEstadoABuzzer(unittest.TestCase):

	def test_creamos_un_traductor_y_hacemos_traducir_un_estado_valido(self):
		configuracion = ConfiguracionBuzzer()
		configuracion.configurar("pin_buzzer")
		reproductor = ReproductorMusicalMockup()
		traductor = TraductorEstadoABuzzer(configuracion)
		#Cambiamos el reproductor que posee por el mockup
		traductor._TraductorEstadoABuzzer__reproductor = reproductor

		traductor.set_estado(EstadoBuild.PASSED)

		self.assertEqual("PASSED", reproductor.cancion_a_reproducir)		

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_creamos_un_traductor_y_hacemos_traducir_un_estado_no_valido_y_esperamos_excepcion(self):
		configuracion = ConfiguracionBuzzer()
		configuracion.configurar("pin_buzzer")
		reproductor = ReproductorMusicalMockup()
		traductor = TraductorEstadoABuzzer(configuracion)
		#Cambiamos el reproductor que posee por el mockup
		traductor._TraductorEstadoABuzzer__reproductor = reproductor
		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

		with self.assertRaises(EstadoNoEspecificadoException):
			traductor.set_estado("ESTADO_NO_DEFINIDO")

	
def main():
	unittest.main()

if __name__ == '__main__':
	main()
