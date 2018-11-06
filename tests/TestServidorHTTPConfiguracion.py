#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
import requests
from ServidorHTTPConfiguracion import ServidorHTTPConfiguracion
from ConfiguracionTravis import ConfiguracionTravis
from ConfiguracionRed import ConfiguracionRed

HOST = "127.0.0.1"

class TestServidorHTTPConfiguracion(unittest.TestCase):

	def test_establecemos_una_configuracion_para_travis_y_corroboramos(self):
		configuracion_travis = ConfiguracionTravis()
		servidor = ServidorHTTPConfiguracion(HOST, 8081, configuracion_travis, None)

		response = requests.get("http://"+HOST+":"+str(8081)+"/set_configuracion_travis?usuario=USUARIO&repositorio=REPOSITORIO&token=TOKEN")

		self.assertEqual("USUARIO", configuracion_travis.get_usuario())
		self.assertEqual("REPOSITORIO", configuracion_travis.get_repositorio())
		self.assertEqual("TOKEN", configuracion_travis.get_token())

		servidor.detener()

	def test_establecemos_una_configuracion_de_red_y_corroboramos(self):
		configuracion_red = ConfiguracionRed()
		servidor = ServidorHTTPConfiguracion(HOST, 8082, None, configuracion_red)
		
		response = requests.get("http://"+HOST+":"+str(8082)+"/set_configuracion_red?SSID=SSID&clave=CLAVE")

		self.assertEqual("SSID", configuracion_red.get_SSID())
		self.assertEqual("CLAVE", configuracion_red.get_clave())

		servidor.detener()
		

def main():
	unittest.main()

if __name__ == '__main__':
	main()
