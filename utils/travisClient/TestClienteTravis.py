import ClienteTravis
import unittest
import requests
from BuildStatus import BuildStatus

TOKEN_CORRECTO = "9cHb1xMQyaGSSSsi6xTW5Q"
TOKEN_INCORRECTO = "ash8y12iugi1u2kkh"
REPOSITORIO = "dyasc-2018"
USUARIO = "MrKupo"

class TestClienteTravis(unittest.TestCase):

	def test_hacemos_un_request_con_credenciales_correctas_y_build_passed(self):
		#CAMBIAMOS LA URL DEL CLIENTE PARA USAR EL MOCK
		ClienteTravis.TRAVIS_API_URL = "http://127.0.0.1:8080"
		#Seteamos el mock para que devuelva Passed
		response = requests.get(ClienteTravis.TRAVIS_API_URL + "/set_status/passed")
		cliente = ClienteTravis.ClienteTravis(USUARIO, REPOSITORIO, TOKEN_CORRECTO)

		estado = cliente.get_estado()

		self.assertEqual(BuildStatus.PASSED, estado)

	def test_hacemos_un_request_con_credenciales_correctas_y_build_failed(self):
		#CAMBIAMOS LA URL DEL CLIENTE PARA USAR EL MOCK
		ClienteTravis.TRAVIS_API_URL = "http://127.0.0.1:8080"
		#Seteamos el mock para que devuelva Passed
		response = requests.get(ClienteTravis.TRAVIS_API_URL + "/set_status/failed")
		cliente = ClienteTravis.ClienteTravis(USUARIO, REPOSITORIO, TOKEN_CORRECTO)

		estado = cliente.get_estado()

		self.assertEqual(BuildStatus.FAILED, estado)

	def test_hacemos_un_request_con_credenciales_correctas_y_build_created(self):
		#CAMBIAMOS LA URL DEL CLIENTE PARA USAR EL MOCK
		ClienteTravis.TRAVIS_API_URL = "http://127.0.0.1:8080"
		#Seteamos el mock para que devuelva Passed
		response = requests.get(ClienteTravis.TRAVIS_API_URL + "/set_status/created")
		cliente = ClienteTravis.ClienteTravis(USUARIO, REPOSITORIO, TOKEN_CORRECTO)

		estado = cliente.get_estado()

		self.assertEqual(BuildStatus.RUNNING, estado)

	def test_hacemos_un_request_con_credenciales_incorrectas(self):
		#CAMBIAMOS LA URL DEL CLIENTE PARA USAR EL MOCK
		ClienteTravis.TRAVIS_API_URL = "http://127.0.0.1:8080"
		cliente = ClienteTravis.ClienteTravis(USUARIO, REPOSITORIO, TOKEN_INCORRECTO)

		estado = cliente.get_estado()

		self.assertEqual(BuildStatus.ACCESS_DENIED, estado)

	def test_hacemos_un_request_a_un_servidor_incorrecto(self):
		#CAMBIAMOS LA URL DEL CLIENTE PARA USAR EL MOCK
		ClienteTravis.TRAVIS_API_URL = "http://127.0.0.1:12312"
		cliente = ClienteTravis.ClienteTravis(USUARIO, REPOSITORIO, TOKEN_CORRECTO)

		estado = cliente.get_estado()

		self.assertEqual(BuildStatus.CONNECTION_ERROR, estado)


if __name__ == '__main__':
	#REQUIERE QUE EL MOCK DE TRAVIS ESTE CORRIENDO EN http://127.0.0.1:8080
	unittest.main()