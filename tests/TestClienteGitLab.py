#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import ClienteGitLab
import unittest
import requests
from EstadoBuild import EstadoBuild
from ConfiguracionCI import ConfiguracionCI

GITLAB_API_URL = "http://127.0.0.1:8080" #URL del Mockup de GitLab
API_URL_INVALIDA = "http://URL_NO_VALIDA:123456"
TOKEN_CORRECTO = "_6ExBju88GSiQvq-m4Rc"
TOKEN_INCORRECTO = "ash8y12iugi1u2kkh"
REPOSITORIO = "test_ci"
USUARIO = "MrKupo"

class TestClienteGitLab(unittest.TestCase):

	def test_hacemos_un_request_con_credenciales_correctas_y_build_success(self):
		configuracion = ConfiguracionCI()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO,GITLAB_API_URL)
		#Seteamos el mock para que devuelva Passed
		requests.get(GITLAB_API_URL + "/set_status/success")
		cliente = ClienteGitLab.ClienteGitLab(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.PASSED, estado)

	def test_hacemos_un_request_con_credenciales_correctas_y_build_failed(self):
		configuracion = ConfiguracionCI()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO,GITLAB_API_URL)
		#Seteamos el mock para que devuelva Failed
		requests.get(GITLAB_API_URL + "/set_status/failed")
		cliente = ClienteGitLab.ClienteGitLab(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.FAILED, estado)

	def test_hacemos_un_request_con_credenciales_correctas_y_build_running(self):
		configuracion = ConfiguracionCI()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO,GITLAB_API_URL)
		#Seteamos el mock para que devuelva Created
		requests.get(GITLAB_API_URL + "/set_status/running")
		cliente = ClienteGitLab.ClienteGitLab(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.RUNNING, estado)

	def test_hacemos_un_request_con_credenciales_incorrectas(self):
		configuracion = ConfiguracionCI()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_INCORRECTO,GITLAB_API_URL)
		cliente = ClienteGitLab.ClienteGitLab(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.ACCESS_DENIED, estado)

	def test_hacemos_un_request_a_un_servidor_incorrecto(self):
		configuracion = ConfiguracionCI()
		configuracion.configurar(USUARIO,REPOSITORIO,TOKEN_CORRECTO, API_URL_INVALIDA)
		cliente = ClienteGitLab.ClienteGitLab(configuracion)

		estado = cliente.get_estado()

		self.assertEqual(EstadoBuild.CONNECTION_ERROR, estado)

def main():
	try:
		response = requests.get(GITLAB_API_URL + "/set_status/success")
		response.close()
	except requests.exceptions.ConnectionError:
		print("ERROR: No es posible ejecutar las pruebas si el Servidor Mockup de GitLab no esta corriendo en",GITLAB_API_URL)
		return
	unittest.main()

if __name__ == '__main__':
	main()
