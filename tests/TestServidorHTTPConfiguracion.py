#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
import requests
from ServidorHTTPConfiguracion import ServidorHTTPConfiguracion
from ConfiguracionCI import ConfiguracionCI
from ConfiguracionRed import ConfiguracionRed

HOST = "localhost"
PUERTO_1 = 8081
PUERTO_2 = 8082

class TestServidorHTTPConfiguracion(unittest.TestCase):

    def test_establecemos_una_configuracion_para_travis_y_corroboramos(self):
        configuracion_ci = ConfiguracionCI()
        servidor = ServidorHTTPConfiguracion(HOST, PUERTO_1, configuracion_ci, None)

        response = requests.get("http://"+HOST+":"+str(PUERTO_1)+"/set_configuracion_ci?usuario=USUARIO&repositorio=REPOSITORIO&token=TOKEN&APIurl=http://test.url")
        
        self.assertEqual("USUARIO", configuracion_ci.get_usuario())
        self.assertEqual("REPOSITORIO", configuracion_ci.get_repositorio())
        self.assertEqual("TOKEN", configuracion_ci.get_token())

        servidor.detener()

    def test_establecemos_una_configuracion_de_red_y_corroboramos(self):
        configuracion_red = ConfiguracionRed()
        servidor = ServidorHTTPConfiguracion(HOST, PUERTO_2, None, configuracion_red)
        
        response = requests.get("http://"+HOST+":"+str(PUERTO_2)+"/set_configuracion_red?SSID=SSID&clave=CLAVE")

        self.assertEqual("SSID", configuracion_red.get_SSID())
        self.assertEqual("CLAVE", configuracion_red.get_clave())

        servidor.detener()
        

def main():
    unittest.main()

if __name__ == '__main__':
    main()
