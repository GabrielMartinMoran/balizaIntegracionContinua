#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from ConectorWiFi import ConectorWiFi
from ConfiguracionRed import ConfiguracionRed
import unittest

class TestConectorWiFi(unittest.TestCase):

	def test_creamos_un_conector_wifi_y_corroboramos_conexion_cuando_no_esta_conectado(self):
		configuracion = ConfiguracionRed()
		configuracion.configurar("SSID", "CLAVE")
		conector = ConectorWiFi(configuracion)

		conectado = conector.esta_conectado()

		self.assertEqual(False, conectado)

		configuracion.borrar_configuracion(True)
	
	def test_creamos_un_conector_wifi_establecemos_conexion_y_corroboramos_conexion_cuando_no_esta_conectado(self):
		configuracion = ConfiguracionRed()
		configuracion.configurar("SSID", "CLAVE")
		conector = ConectorWiFi(configuracion, 0)

		conector.conectar()

		conectado = conector.esta_conectado()

		self.assertEqual(True, conectado)

		configuracion.borrar_configuracion(True)
	

def main():
	unittest.main()

if __name__ == '__main__':
	main()
