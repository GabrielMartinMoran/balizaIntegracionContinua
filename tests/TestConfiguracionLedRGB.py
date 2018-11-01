#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from ConfiguracionLedRGB import *
import unittest

def borrar_configuracion_Led_RGB_previa():
	#Borramos el archivo de configuracion que exista para que no haya basura al iniciar los tests
	conf = ConfiguracionLedRGB()
	conf.borrar_configuracion(True)

class TestConfiguracionLedRGB(unittest.TestCase):	
    
	def test_creamos_una_configuracion_Led_RGB_cuando_no_existe_archivo_de_configuracion_Led_RGB_y_preguntamos_si_esta_configurada(self):
		configuracion = ConfiguracionLedRGB()
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_creamos_una_configuracion_Led_RGB_cuando_existe_archivo_de_configuracion_Led_RGB_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionLedRGB()
		configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
		configuracion_nueva = ConfiguracionLedRGB()
		
		configurada = configuracion_nueva.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_establecemos_la_cofiguracion_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionLedRGB()
		configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_borramos_la_configuracion_Led_RGB_existente_y_corroboramos_que_no_este_configurada(self):
		configuracion = ConfiguracionLedRGB()
		configuracion.configurar("pin_led_rojo","pin_led_verde","pin_led_azul")
		configuracion.borrar_configuracion(True)

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)


	def test_creamos_una_nueva_configuracion_Led_RGB_solo_configuramos_algunos_parametros_y_corroboramos_que_este_como_no_configurada(self):
		configuracion = ConfiguracionLedRGB()
		configuracion.set_pin_led_rojo("pin_led_rojo")
		configuracion.set_pin_led_azul("pin_led_azul")

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
	

def main():
	borrar_configuracion_Led_RGB_previa()
	unittest.main()

if __name__ == '__main__':
	main()
