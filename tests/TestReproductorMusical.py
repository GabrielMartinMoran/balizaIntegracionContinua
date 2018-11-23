#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
from EstadoBuild import EstadoBuild
from EstadoBuild import EstadoNoEspecificadoException
from ReproductorMusical import ReproductorMusical
from ConfiguracionBuzzer import ConfiguracionBuzzer

class ControladorBuzzerMockup:

	intensidad = None
	frecuencia = None

	def set_intensidad(self, valor):
		self.intensidad = valor

	def set_frecuencia(self, valor):
		self.frecuencia = valor

	def reprodujo_algo(self):
		return self.intensidad != None and self.frecuencia != None

class TestReproductorMusical(unittest.TestCase):
	
	def test_creamos_un_reproductor_y_hacemos_reproducir_un_estado_valido_sin_esperar_excepcion(self):
		configuracion = ConfiguracionBuzzer()
		configuracion.configurar("pin_buzzer")
		reproductor = ReproductorMusical(configuracion)
		#Creamos y seteamos el mockup
		controlador_buzzer_mockup = ControladorBuzzerMockup()
		reproductor._ReproductorMusical__controlador_buzzer = controlador_buzzer_mockup
		reproductor.set_estado(EstadoBuild.PASSED)

		self.assertEqual(True, controlador_buzzer_mockup.reprodujo_algo())		

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
	

	def test_creamos_un_reproductor_y_hacemos_reproducir_un_estado_no_valido_y_esperamos_excepcion(self):
		configuracion = ConfiguracionBuzzer()
		configuracion.configurar("pin_buzzer")
		reproductor = ReproductorMusical(configuracion)
		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

		with self.assertRaises(EstadoNoEspecificadoException):
			reproductor.set_estado("ESTADO_NO_DEFINIDO")

	
def main():
	unittest.main()

if __name__ == '__main__':
	main()
