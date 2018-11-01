#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
import HttpRequests

TEST_API_URL = "https://jsonplaceholder.typicode.com"

class TestHttpRequests(unittest.TestCase):

	def test_hacemos_post_con_url_valida(self):		
		esperado = {'id':101}

		response = HttpRequests.post(TEST_API_URL + "/posts")
		json_response = response.json()

		self.assertEqual(esperado, json_response)

	def test_hacemos_post_con_url_no_valida_esperando_excepcion(self):
		with self.assertRaises(HttpRequests.ConnectionError):
			HttpRequests.post("http://URL_NO_VALIDA:123456")
	
	def test_hacemos_get_con_url_valida(self):		
		esperado = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

		response = HttpRequests.get(TEST_API_URL + "/posts/1")
		json_response = response.json()

		self.assertEqual(esperado, json_response)

	def test_hacemos_get_con_url_no_valida_esperando_excepcion(self):
		with self.assertRaises(HttpRequests.ConnectionError):
			HttpRequests.get("http://URL_NO_VALIDA:123456")

	def test_hacemos_request_tipo_post_con_url_valida(self):		
		esperado = {'id':101}

		response = HttpRequests.request('POST', TEST_API_URL + "/posts")
		json_response = response.json()

		self.assertEqual(esperado, json_response)

	def test_hacemos_request_tipo_post_con_url_no_valida_esperando_excepcion(self):
		with self.assertRaises(HttpRequests.ConnectionError):
			HttpRequests.request('POST',"http://URL_NO_VALIDA:123456")
	
	def test_hacemos_request_tipo_get_con_url_valida(self):		
		esperado = {'userId': 1, 'id': 1, 'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'}

		response = HttpRequests.request('GET', TEST_API_URL + "/posts/1")
		json_response = response.json()

		self.assertEqual(esperado, json_response)

	def test_hacemos_request_tipo_get_con_url_no_valida_esperando_excepcion(self):
		with self.assertRaises(HttpRequests.ConnectionError):
			HttpRequests.request('GET', "http://URL_NO_VALIDA:123456")


def main():
	unittest.main()

if __name__ == '__main__':
	main()
