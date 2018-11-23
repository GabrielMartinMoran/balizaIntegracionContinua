#----------------------------- IMPORTAMOS EL DIRECTORIO src ---------------------------
import os
import sys

#Bibliotecas necesarias para la captura de salida
import io
from contextlib import redirect_stdout
#--------------------------------------------------------------------------------------

#IMPORTAMOS DEL PADRE
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
#--------------------------------------------------------------------------------------

import unittest
from EstadoBuild import EstadoBuild
from EstadoBuild import EstadoNoEspecificadoException
from ImpresorPorConsola import ImpresorPorConsola

class TestImpresorPorConsola(unittest.TestCase):

    def test_creamos_un_impresor_y_hacemos_traducir_un_estado_valido(self):
        impresor = ImpresorPorConsola()

        f = io.StringIO()
        with redirect_stdout(f):
            impresor.set_estado(EstadoBuild.PASSED)
        out = f.getvalue()

        self.assertEqual("CAMBIO DE ESTADO DEL BUILD A: PASSED\n", out)  

    def test_creamos_un_impresor_y_hacemos_traducir_un_estado_no_valido_esperando_excepcion(self):
        impresor = ImpresorPorConsola()
    
        with self.assertRaises(EstadoNoEspecificadoException):
            impresor.set_estado("ESTADO_NO_DEFINIDO")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
