import json
import os

ARCHIVO_CONFIGURACION = "config.json"
TRAVIS_API_URL = "https://api.travis-ci.org"

class ConfiguracionTravis:

    __data = {
        "TOKEN"       : None,
        "USUARIO"     : None,
        "REPOSITORIO" : None,
        "API_URL"     : None,
    }

    def __init__(self):
        self.__cargar_archivo_configuracion()

    """
    Dado un usuario, un repositorio, un token y opcionalmente una URL para la API, establece
    la configuracion
    """
    def configurar(self, usuario, repositorio, token, api_url=TRAVIS_API_URL):
        self.set_usuario(usuario)
        self.set_repositorio(repositorio)
        self.set_token(token)
        self.set_api_url(api_url)
        self.__guardar_archivo_configuracion()

    """
    Se considera que esta configurada si todos los parametros de configuracion son
    distinto de None
    """
    def esta_configurada(self):
        for x in self.__data:
            if(self.__data[x] == None):
                return False
        return True

    def set_api_url(self, api_url):
        self.__data["API_URL"] = api_url
        self.__guardar_archivo_configuracion()

    def set_repositorio(self, repositorio):
        self.__data["REPOSITORIO"] = repositorio
        self.__guardar_archivo_configuracion()

    def set_usuario(self, usuario):
        self.__data["USUARIO"] = usuario
        self.__guardar_archivo_configuracion()

    def set_token(self, token):
        self.__data["TOKEN"] = token
        self.__guardar_archivo_configuracion()

    def get_api_url(self):
        return self.__data["API_URL"]

    def get_repositorio(self):
        return self.__data["REPOSITORIO"]

    def get_usuario(self):
        return self.__data["USUARIO"]

    def get_token(self):
        return self.__data["TOKEN"]

    def __get_path_archivo_configuracion(self):
        path_scipt = os.path.realpath(__file__)
        path_directorio = os.path.dirname(path_scipt)
        return os.path.join(path_directorio, ARCHIVO_CONFIGURACION)

    def __guardar_archivo_configuracion(self):
        f = open(self.__get_path_archivo_configuracion(), "w")
        f.write(json.dumps(self.__data))
        f.close()
    
    def __cargar_archivo_configuracion(self):
        if(not self.existe_archivo_configuracion()):
            return False
        f = open(self.__get_path_archivo_configuracion(),"r")
        self.__data = json.loads(f.read())
        f.close()

    def __borrar_archivo_configuracion(self):
        if(self.existe_archivo_configuracion()):
            os.remove(self.__get_path_archivo_configuracion())

    """
    Devuelve True si existe guardado un archivo de configuracion
    """
    def existe_archivo_configuracion(self):
        return os.path.isfile(self.__get_path_archivo_configuracion())

    """
    Borra la configuracion actual y si el parametro borrar_archivo_configuracion esta en True tambien elimina el archivo guardado
    """
    def borrar_configuracion(self, borrar_archivo_configuracion=False):
        for x in self.__data:
            self.__data[x] = None
        if(borrar_archivo_configuracion):
            self.__borrar_archivo_configuracion()