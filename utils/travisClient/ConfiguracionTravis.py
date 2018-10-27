from Configuracion import Configuracion

class ConfiguracionTravis(Configuracion):

    _TRAVIS_API_URL = "https://api.travis-ci.org"

    def __init__(self):
        self._ARCHIVO_CONFIGURACION = "configuracion_travis.json"
        self._data = {
            "TOKEN"       : None,
            "USUARIO"     : None,
            "REPOSITORIO" : None,
            "API_URL"     : None,
        }
        super(ConfiguracionTravis,self)._cargar_archivo_configuracion()

    def _set_valores_data(self, usuario, repositorio, token, api_url):
        self.set_usuario(usuario)
        self.set_repositorio(repositorio)
        self.set_token(token)
        self.set_api_url(api_url)

    """
    Dado un usuario, un repositorio, un token y opcionalmente una URL para la API, establece
    la configuracion
    """
    def configurar(self, usuario, repositorio, token, api_url=_TRAVIS_API_URL):
        super(ConfiguracionTravis,self).configurar(usuario, repositorio, token, api_url)

    def set_api_url(self, api_url):
        self._data["API_URL"] = api_url
        super(ConfiguracionTravis,self)._guardar_archivo_configuracion()

    def set_repositorio(self, repositorio):
        self._data["REPOSITORIO"] = repositorio
        super(ConfiguracionTravis,self)._guardar_archivo_configuracion()

    def set_usuario(self, usuario):
        self._data["USUARIO"] = usuario
        super(ConfiguracionTravis,self)._guardar_archivo_configuracion()

    def set_token(self, token):
        self._data["TOKEN"] = token
        super(ConfiguracionTravis,self)._guardar_archivo_configuracion()

    def get_api_url(self):
        return self._data["API_URL"]

    def get_repositorio(self):
        return self._data["REPOSITORIO"]

    def get_usuario(self):
        return self._data["USUARIO"]

    def get_token(self):
        return self._data["TOKEN"]