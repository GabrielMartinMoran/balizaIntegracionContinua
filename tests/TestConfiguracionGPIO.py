#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from ConfiguracionGPIO import *
import unittest

def borrar_configuracion_GPIO_previa():
	#Borramos el archivo de configuracion que exista para que no haya basura al iniciar los tests
	conf = ConfiguracionGPIO()
	conf.borrar_configuracion(True)

class TestConfiguracionGPIO(unittest.TestCase):	
    
	def test_creamos_una_configuracion_GPIO_cuando_no_existe_archivo_de_configuracion_GPIO_y_preguntamos_si_esta_configurada(self):
		configuracion = ConfiguracionGPIO()
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_creamos_una_configuracion_GPIO_cuando_existe_archivo_de_configuracion_GPIO_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionGPIO()
		configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
		configuracion_nueva = ConfiguracionGPIO()
		
		configurada = configuracion_nueva.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_establecemos_la_cofiguracion_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionGPIO()
		configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_borramos_la_configuracion_GPIO_existente_y_corroboramos_que_no_este_configurada(self):
		configuracion = ConfiguracionGPIO()
		configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
		configuracion.borrar_configuracion(True)

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)


	def test_creamos_una_nueva_configuracion_GPIO_solo_configuramos_algunos_parametros_y_corroboramos_que_este_como_no_configurada(self):
		configuracion = ConfiguracionGPIO()
		configuracion.set_pin_led_rojo("pin_led_rojo")
		configuracion.set_pin_led_azul("pin_led_azul")

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
	

def main():
	borrar_configuracion_GPIO_previa()
	unittest.main()

if __name__ == '__main__':
	main()
