#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from EvaluadorEstadoBuild import EvaluadorEstadoBuild
from EstadoBuild import EstadoBuild
import unittest

class ClienteTravisMockup():

	estado = EstadoBuild.PASSED

	def set_estado(self, estado):
		self.estado = estado

	def get_estado(self):
		return self.estado

class ManejadorLedRGBMockup():

	cambio_estado = False

	def set_estado(self, estado):
		self.estado = estado
		self.cambio_estado = True

class TestClienteTravis(unittest.TestCase):

	def test_creamos_un_evaluador_estado_nuevo_y_evaluamos_la_primera_vez_para_ver_si_cambio_el_estado(self):
		evaluador = EvaluadorEstadoBuild()
		cliente_travis_mockup = ClienteTravisMockup()
		manejador_led_RGB_mockup = ManejadorLedRGBMockup()
		evaluador.clienteTravis = cliente_travis_mockup
		evaluador.manejador_led_RGB = manejador_led_RGB_mockup

		evaluador.evaluar_estado()

		self.assertEqual(True, manejador_led_RGB_mockup.cambio_estado)

	def test_creamos_un_evaluador_estado_y_obtenemos_el_estado_cuando_no_cambio(self):
		evaluador = EvaluadorEstadoBuild()
		cliente_travis_mockup = ClienteTravisMockup()
		manejador_led_RGB_mockup = ManejadorLedRGBMockup()
		evaluador.clienteTravis = cliente_travis_mockup
		evaluador.manejador_led_RGB = manejador_led_RGB_mockup

		evaluador.evaluar_estado()
		#Marcamos como que no cambio el estado
		manejador_led_RGB_mockup.cambio_estado = False
		evaluador.evaluar_estado()

		self.assertEqual(False, manejador_led_RGB_mockup.cambio_estado)

	def test_creamos_un_evaluador_estado_y_obtenemos_el_estado_cuando_cambio(self):
		evaluador = EvaluadorEstadoBuild()
		cliente_travis_mockup = ClienteTravisMockup()
		manejador_led_RGB_mockup = ManejadorLedRGBMockup()
		evaluador.clienteTravis = cliente_travis_mockup
		evaluador.manejador_led_RGB = manejador_led_RGB_mockup

		evaluador.evaluar_estado()
		#Marcamos como que no cambio el estado
		manejador_led_RGB_mockup.cambio_estado = False
		cliente_travis_mockup.set_estado(EstadoBuild.FAILED)
		evaluador.evaluar_estado()

		self.assertEqual(True, manejador_led_RGB_mockup.cambio_estado)	

def main():
	unittest.main()

if __name__ == '__main__':
	main()
