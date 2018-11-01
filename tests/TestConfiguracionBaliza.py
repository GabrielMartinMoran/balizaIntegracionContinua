#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from ConfiguracionBaliza import *
import unittest

def borrar_configuracion_baliza_previa():
	#Borramos el archivo de configuracion que exista para que no haya basura al iniciar los tests
	conf = ConfiguracionBaliza()
	conf.borrar_configuracion(True)
	#DESTUIMOS EL SINGLETON
	ConfiguracionBaliza.instancia._delete_singleton()
	del conf

class TestConfiguracionBaliza(unittest.TestCase):	

	def test_creamos_una_configuracion_baliza_y_tratamos_de_accederla_como_singleton(self):

		configuracion = ConfiguracionBaliza()
		
		configuracion_travis = ConfiguracionBaliza.instancia.get_configuracion_travis()
		configuracion_red = ConfiguracionBaliza.instancia.get_configuracion_red()
		configuracion_led_RGB = ConfiguracionBaliza.instancia.get_configuracion_led_RGB()

		self.assertEqual(ConfiguracionTravis, type(configuracion_travis))
		self.assertEqual(ConfiguracionRed, type(configuracion_red))
		self.assertEqual(ConfiguracionLedRGB, type(configuracion_led_RGB))

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
		#DESTUIMOS EL SINGLETON
		ConfiguracionBaliza.instancia._delete_singleton()
		del configuracion
    
	def test_creamos_una_configuracion_baliza_cuando_no_existe_archivo_de_configuracion_baliza_y_preguntamos_si_cada_subconfiguracion_esta_configurada(self):
		configuracion = ConfiguracionBaliza()
		
		configuracion_travis = ConfiguracionBaliza.instancia.get_configuracion_travis()
		configuracion_red = ConfiguracionBaliza.instancia.get_configuracion_red()
		configuracion_led_RGB = ConfiguracionBaliza.instancia.get_configuracion_led_RGB()

		conf_travis_configurada = configuracion_travis.esta_configurada()
		conf_red_configurada = configuracion_red.esta_configurada()
		conf_GPIO_configurada = configuracion_led_RGB.esta_configurada()

		self.assertEqual(False, conf_travis_configurada)
		self.assertEqual(False, conf_red_configurada)
		self.assertEqual(False, conf_GPIO_configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
		#DESTUIMOS EL SINGLETON
		ConfiguracionBaliza.instancia._delete_singleton()
		del configuracion


	def test_creamos_una_configuracion_baliza_configuramos_la_red_probamos_que_este_configurada_borramos_la_configuracion_y_corroboramos_que_no_esta_configurada(self):
		configuracion = ConfiguracionBaliza()
		
		configuracion_red = ConfiguracionBaliza.instancia.get_configuracion_red()
		configuracion_red.configurar("SSID","CLAVE")

		conf_red_configurada = configuracion_red.esta_configurada()

		self.assertEqual(True, conf_red_configurada)

		ConfiguracionBaliza.instancia.borrar_configuracion(True)
		conf_red_configurada = configuracion_red.esta_configurada()

		self.assertEqual(False, conf_red_configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
		#DESTUIMOS EL SINGLETON
		ConfiguracionBaliza.instancia._delete_singleton()
		del configuracion
	

def main():
	borrar_configuracion_baliza_previa()
	unittest.main()

if __name__ == '__main__':
	main()
