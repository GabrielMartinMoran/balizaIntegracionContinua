import sys

def __get_nombre_plataforma():
    if(sys.platform == "pyboard"):
        return "MICROPYTHON"
    return "PYTHON"

MODULOS = {
    "requests" : { "PYTHON" : "requests",
                   "MICROPYTHON": "urequests"
                 },
    "machine"  : { "PYTHON" : "requests",
                   "MICROPYTHON": "urequests"
                 },
    "network"  : { "PYTHON" : "networkMockup",
                   "MICROPYTHON": "network"
                 },
}

def p_import(modulo):
    nombre_modulo = ""
    if(modulo in MODULOS):
        nombre_modulo = MODULOS[modulo][__get_nombre_plataforma()]
    else:
        nombre_modulo = modulo
    return __import__(nombre_modulo)

def main():
    _os = p_import("os")
    print(_os.listdir())

if __name__ == '__main__':
    main()