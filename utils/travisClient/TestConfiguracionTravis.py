from ConfiguracionTravis import *
import unittest

def borrar_configuracion_previa():
	#Borramos el archivo de configuracion que exista para que no haya basura al iniciar los tests
	conf = ConfiguracionTravis()
	conf.borrar_configuracion(True)

class TestConfiguracionTravis(unittest.TestCase):	
    
	def test_creamos_una_configuracion_cuando_no_existe_archivo_de_configuracion_y_preguntamos_si_esta_configurada(self):
		configuracion = ConfiguracionTravis()
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_creamos_una_configuracion_cuando_existe_archivo_de_configuracion_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar("usuario","repositorio","token")
		configuracion_nueva = ConfiguracionTravis()
		
		configurada = configuracion_nueva.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_establecemos_la_cofiguracion_y_corroboramos_que_este_configurada(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar("usuario","repositorio","token")
		
		configurada = configuracion.esta_configurada()

		self.assertEqual(True, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)

	def test_borramos_la_configuracion_existente_y_corroboramos_que_no_este_configurada(self):
		configuracion = ConfiguracionTravis()
		configuracion.configurar("usuario","repositorio","token")
		configuracion.borrar_configuracion(True)

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)


	def test_creamos_una_nueva_configuracion_solo_configuramos_algunos_parametros_y_corroboramos_que_este_como_no_configurada(self):
		configuracion = ConfiguracionTravis()
		configuracion.set_token("token")
		configuracion.set_repositorio("repositorio")

		configurada = configuracion.esta_configurada()

		self.assertEqual(False, configurada)

		#LIMPIAMOS LA CONFIGURACION RESULTANTE
		configuracion.borrar_configuracion(True)
	

def main():
	borrar_configuracion_previa()
	unittest.main()

if __name__ == '__main__':
	main()