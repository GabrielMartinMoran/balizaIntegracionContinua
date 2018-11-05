import sys

def __get_nombre_plataforma():
    if(sys.platform == "pyboard"):
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
}

def importar(modulo):
    nombre_modulo = ""
    if(modulo in MODULOS):
        nombre_modulo = MODULOS[modulo][__get_nombre_plataforma()]
    else:
        nombre_modulo = modulo
    return __import__(nombre_modulo)