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
from TraductorEstadoAConsola import TraductorEstadoAConsola

class TestTraductorEstadoAConsola(unittest.TestCase):

    def test_creamos_un_traductor_y_hacemos_traducir_un_estado_valido(self):
        traductor = TraductorEstadoAConsola()

        f = io.StringIO()
        with redirect_stdout(f):
            traductor.set_estado(EstadoBuild.PASSED)
        out = f.getvalue()

        self.assertEqual("CAMBIO DE ESTADO DEL BUILD A: PASSED\n", out)  

    def test_creamos_un_traductor_y_hacemos_traducir_un_estado_no_valido_esperando_excepcion(self):
        traductor = TraductorEstadoAConsola()
    
        with self.assertRaises(EstadoNoEspecificadoException):
            traductor.set_estado("ESTADO_NO_DEFINIDO")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
