import sys

def __get_nombre_plataforma():
    if(sys.platform == "esp32"):
        return "MICROPYTHON"
    return "PYTHON"

if __get_nombre_plataforma() == "PYTHON":
    import os
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/mockups')))

MODULOS = {
    "requests" : { "PYTHON" : "requests",
                   "MICROPYTHON": "urequests"
                 },
    "machine"  : { "PYTHON" : "requests",
                   "MICROPYTHON": "urequests"
                 },
    "network"  : { "PYTHON" : "NetworkMockup",
                   "MICROPYTHON": "network"
                 },
    "ControladorBuzzer"  : { "PYTHON" : "ControladorBuzzerMockup",
                             "MICROPYTHON": "ControladorBuzzer"
                           },
    "ControladorLedRGB"  : { "PYTHON" : "ControladorLedRGBMockup",
                             "MICROPYTHON": "ControladorLedRGB"
                           },
}

def importar(modulo):
    nombre_modulo = modulo
    if(modulo in MODULOS):
        nombre_modulo = MODULOS[modulo][__get_nombre_plataforma()]
    return __import__(nombre_modulo)