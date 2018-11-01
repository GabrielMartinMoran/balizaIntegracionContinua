#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

from Configuracion import *
import unittest

def borrar_configuracion_previa():
	#Borramos el archivo de configuracion que exista para que no haya basura al iniciar los tests
	conf = Configuracion()
	conf.borrar_configuracion(True)

class TestConfiguracion(unittest.TestCase):	
    
	def test_creamos_una_configuracion_cuando_no_existe_archivo_de_configuracion_y_preguntamos_si_esta_configurada(self):
		configuracion = Configuracion()
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_creamos_una_configuracion_cuando_existe_archivo_de_configuracion_y_corroboramos_que_este_configurada(self):
		configuracion = Configuracion()
		configuracion.configurar("param1","param2","param3","param4","param5")
		configuracion_nueva = Configuracion()
		
		configurada = configuracion_nueva.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_establecemos_la_cofiguracion_y_corroboramos_que_este_configurada(self):
		configuracion = Configuracion()
		configuracion.configurar("param1","param2","param3","param4","param5")
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_borramos_la_configuracion_existente_y_corroboramos_que_no_este_configurada(self):
		configuracion = Configuracion()
		configuracion.configurar("param1","param2","param3","param4","param5")
		configuracion.borrar_configuracion(True)

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)
	

def main():
	borrar_configuracion_previa()
	unittest.main()

if __name__ == '__main__':
	main()
