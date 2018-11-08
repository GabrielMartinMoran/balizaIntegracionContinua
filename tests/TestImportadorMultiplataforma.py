#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import ImportadorMultiplataforma
import unittest

class TestImportadorMultiplataforma(unittest.TestCase):

	def test_importamos_normalmente_y_comparamos_con_el_resultado_del_importador_cuando_no_esta_definido_como_import_especial(self):
		import os
		
		_os = ImportadorMultiplataforma.importar("os")

		self.assertEqual(os, _os)

	def test_importamos_normalmente_y_comparamos_con_el_resultado_del_importador_cuando_esta_definido_como_import_especial(self):
		import requests
		
		_requests = ImportadorMultiplataforma.importar("requests")

		self.assertEqual(requests, _requests)

def main():
	unittest.main()

if __name__ == '__main__':
	main()
