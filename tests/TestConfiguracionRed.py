#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from ConfiguracionRed import *
import unittest

def borrar_configuracion_red_previa():
	#Borramos el archivo de configuracion que exista para que no haya basura al iniciar los tests
	conf = ConfiguracionRed()
	conf.borrar_configuracion(True)

class TestConfiguracionRed(unittest.TestCase):	
    
	def test_creamos_una_configuracion_red_cuando_no_existe_archivo_de_configuracion_red_y_preguntamos_si_esta_configurada(self):
		configuracion = ConfiguracionRed()
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_creamos_una_configuracion_red_cuando_existe_archivo_de_configuracion_red_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionRed()
		configuracion.configurar("SSID","clave")
		configuracion_nueva = ConfiguracionRed()
		
		configurada = configuracion_nueva.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_establecemos_la_cofiguracion_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionRed()
		configuracion.configurar("SSID","clave")
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_borramos_la_configuracion_red_existente_y_corroboramos_que_no_este_configurada(self):
		configuracion = ConfiguracionRed()
		configuracion.configurar("SSID","clave")
		configuracion.borrar_configuracion(True)

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)


	def test_creamos_una_nueva_configuracion_red_solo_configuramos_un_parametro_y_corroboramos_que_este_como_no_configurada(self):
		configuracion = ConfiguracionRed()
		configuracion.set_SSID("SSID")

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
	

def main():
	borrar_configuracion_red_previa()
	unittest.main()

if __name__ == '__main__':
	main()
