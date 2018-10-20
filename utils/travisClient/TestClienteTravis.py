import ClienteTravis
import unittest
import requests
from EstadoBuild import EstadoBuild
from ConfiguracionTravis import ConfiguracionTravis

TRAVIS_API_URL = "http://127.0.0.1:8080" #URL del Mockup de Travis
API_URL_INVALIDA = "http://URL_NO_VALIDA:123456"
TOKEN_CORRECTO = "9cHb1xMQyaGSSSsi6xTW5Q"
TOKEN_INCORRECTO = "ash8y12iugi1u2kkh"
REPOSITORIO = "dyasc-2018"
USUARIO = "MrKupo"

class TestClienteTravis(unittest.TestCase):

	def test_hacemos_un_request_con_credenciales_correctas_y_build_passed(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO,TRAVIS_API_URL)
		#Seteamos el mock para que devuelva Passed
		requests.get(TRAVIS_API_URL + "/set_status/passed")
		cliente = ClienteTravis.ClienteTravis(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.PASSED, estado)

	def test_hacemos_un_request_con_credenciales_correctas_y_build_failed(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO,TRAVIS_API_URL)
		#Seteamos el mock para que devuelva Failed
		requests.get(TRAVIS_API_URL + "/set_status/failed")
		cliente = ClienteTravis.ClienteTravis(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.FAILED, estado)

	def test_hacemos_un_request_con_credenciales_correctas_y_build_created(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO,TRAVIS_API_URL)
		#Seteamos el mock para que devuelva Created
		requests.get(TRAVIS_API_URL + "/set_status/created")
		cliente = ClienteTravis.ClienteTravis(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.RUNNING, estado)

	def test_hacemos_un_request_con_credenciales_incorrectas(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_INCORRECTO,TRAVIS_API_URL)
		cliente = ClienteTravis.ClienteTravis(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.ACCESS_DENIED, estado)

	def test_hacemos_un_request_a_un_servidor_incorrecto(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO, API_URL_INVALIDA)
		cliente = ClienteTravis.ClienteTravis(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.CONNECTION_ERROR, estado)

def main():
	try:
		response = requests.get(TRAVIS_API_URL + "/set_status/passed")
		response.close()
	except requests.exceptions.ConnectionError:
		print("ERROR: No es posible ejecutar las pruebas si el Servidor Mockup de Travis no esta corriendo en",TRAVIS_API_URL)
		return
	unittest.main()

if __name__ == '__main__':
	main()