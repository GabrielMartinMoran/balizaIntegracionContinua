#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from EvaluadorEstadoBuild import EvaluadorEstadoBuild
from ConfiguracionBaliza import ConfiguracionBaliza
from EstadoBuild import EstadoBuild
import unittest
import requests

TRAVIS_API_URL = "http://127.0.0.1:8080"
TOKEN = "9cHb1xMQyaGSSSsi6xTW5Q"
REPOSITORIO = "dyasc-2018"
USUARIO = "MrKupo"

class TestEvaluadorEstadoBuild(unittest.TestCase):

	def test_creamos_un_evaluador_estado_nuevo_y_evaluamos_la_primera_vez_para_ver_si_cambio_el_estado(self):
		evaluador = EvaluadorEstadoBuild()
		#Seteamos el estado del build
		requests.get(TRAVIS_API_URL + "/set_status/passed")		
		
		esperado = (True, EstadoBuild.PASSED)
		resultado = evaluador.evaluar_cambio_de_estado()

		self.assertEqual(esperado, resultado)

	def test_creamos_un_evaluador_estado_y_obtenemos_el_estado_cuando_no_cambio(self):
		evaluador = EvaluadorEstadoBuild()
		#Seteamos el estado del build
		requests.get(TRAVIS_API_URL + "/set_status/passed")		
		#Evaluamos la primera vez para que luego no cambie el estado
		evaluador.evaluar_cambio_de_estado()
		
		esperado = (False, EstadoBuild.PASSED)
		resultado = evaluador.evaluar_cambio_de_estado()

		self.assertEqual(esperado, resultado)

	def test_creamos_un_evaluador_estado_y_obtenemos_el_estado_cuando_cambio(self):
		evaluador = EvaluadorEstadoBuild()
		#Seteamos el estado del build
		requests.get(TRAVIS_API_URL + "/set_status/passed")
		#Evaluamos la primera vez
		evaluador.evaluar_cambio_de_estado()
		#Cambiamos el estado
		requests.get(TRAVIS_API_URL + "/set_status/failed")
		
		esperado = (True, EstadoBuild.FAILED)
		resultado = evaluador.evaluar_cambio_de_estado()

		self.assertEqual(esperado, resultado)

def main():
	try:
		response = requests.get(TRAVIS_API_URL + "/set_status/passed")
		response.close()
	except requests.exceptions.ConnectionError:
		print("ERROR: No es posible ejecutar las pruebas si el Servidor Mockup de Travis no esta corriendo en",TRAVIS_API_URL)
		return
	configuracion = ConfiguracionBaliza()
	configuracion_ci = ConfiguracionBaliza.instancia.get_configuracion_ci()
	configuracion_ci.configurar(USUARIO,REPOSITORIO,TOKEN,TRAVIS_API_URL)	
	unittest.main(exit=False)
	configuracion.borrar_configuracion(True)

if __name__ == '__main__':
	main()
