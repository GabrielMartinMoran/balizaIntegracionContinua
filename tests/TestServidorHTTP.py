#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
import requests
from ServidorHTTP import ServidorHTTP

HOST = "localhost"
PUERTO = 8181

class TestServidorHTTP(unittest.TestCase):

	def test_dato_un_string_correspondiente_a_un_request_corroboramos_que_sea_valido(self):
		servidor = ServidorHTTP(HOST, PUERTO)
		request_valido = "GET /url"

		es_valido = servidor._ServidorHTTP__es_request(request_valido)

		self.assertEqual(True, es_valido)

	def test_dato_un_string_correspondiente_a_un_request_corroboramos_que_no_sea_valido(self):
		servidor = ServidorHTTP(HOST, PUERTO)
		request_no_valido = "TEST /url"

		es_valido = servidor._ServidorHTTP__es_request(request_no_valido)

		self.assertEqual(False, es_valido)

	def test_dado_una_url_corroboramos_la_division_de_elementos(self):
		servidor = ServidorHTTP(HOST, PUERTO)
		url = "/test?param1=123&param2=321&param3=asd"
		esperado = ["/test", "param1=123", "param2=321", "param3=asd"]

		resultado = servidor._ServidorHTTP__dividir_url(url)

		self.assertEqual(esperado, resultado)

	def test_dado_un_array_con_parametros_crudos_corroboramos_el_mapeo_resultante(self):
		servidor = ServidorHTTP(HOST, PUERTO)
		parametros_crudos = ["a=1","b=asd","43=test"]
		mapa_esperado = {"a":"1","b":"asd","43":"test"}

		mapa_resultante = servidor._ServidorHTTP__mapear_parametros(parametros_crudos)

		self.assertEqual(mapa_esperado, mapa_resultante)

	def test_agregamos_ruteo_y_corroboramos_ruta(self):
		def test_funcion(params):
			return "OK"

		servidor = ServidorHTTP(HOST, PUERTO)
		servidor.agregar_ruteo("/test",test_funcion)

		resultado_esperado = servidor._ServidorHTTP__generar_response(test_funcion([]))
		resultado = servidor._ServidorHTTP__rutear("/test",[])

		self.assertEqual(resultado_esperado, resultado)

	def test_corroboramos_ruta_para_direccion_no_especificada(self):
		servidor = ServidorHTTP(HOST, PUERTO)

		resultado_esperado = servidor._ServidorHTTP__generar_response("URL NO ENCONTRADA", error = True)
		resultado = servidor._ServidorHTTP__rutear("/test",[])

		self.assertEqual(resultado_esperado, resultado)

	def test_iniciamos_servidor_y_corroboramos_un_ruteo_por_HTTP(self):
		def test_funcion(params):
			return "OK"

		servidor = ServidorHTTP(HOST, PUERTO)
		servidor.agregar_ruteo("/test",test_funcion)
		servidor.iniciar()
		resultado_esperado = test_funcion([])

		resultado = requests.get("http://"+HOST+":"+str(PUERTO)+"/test").text

		self.assertEqual(resultado_esperado, resultado)

		servidor.detener()

def main():
	unittest.main()

if __name__ == '__main__':
	main()
