from Configuracion import Configuracion
import ServidoresCI

class ConfiguracionCI(Configuracion):

    _TRAVIS_API_URL = "https://api.travis-ci.org"

    def __init__(self):
        self._ARCHIVO_CONFIGURACION = "configuracion_ci.json"
        self._data = {
            "TOKEN"       : None,
            "USUARIO"     : None,
            "REPOSITORIO" : None,
            "API_URL"     : None,
            "SERVIDOR_CI" : None,
        }
        super(ConfiguracionCI,self)._cargar_archivo_configuracion()

    def _set_valores_data(self, usuario, repositorio, token, api_url, servidor_ci):
        self.set_usuario(usuario)
        self.set_repositorio(repositorio)
        self.set_token(token)
        self.set_api_url(api_url)
        self.set_servidor_ci(servidor_ci)

    """
    Dado un usuario, un repositorio, un token y opcionalmente una URL para la API, establece
    la configuracion
    """
    def configurar(self, usuario, repositorio, token, api_url=_TRAVIS_API_URL, servidor_ci=ServidoresCI.TRAVIS):
        super(ConfiguracionCI,self).configurar(usuario, repositorio, token, api_url, servidor_ci)

    def set_api_url(self, api_url):
        self._data["API_URL"] = api_url
        super(ConfiguracionCI,self)._guardar_archivo_configuracion()

    def set_repositorio(self, repositorio):
        self._data["REPOSITORIO"] = repositorio
        super(ConfiguracionCI,self)._guardar_archivo_configuracion()

    def set_usuario(self, usuario):
        self._data["USUARIO"] = usuario
        super(ConfiguracionCI,self)._guardar_archivo_configuracion()

    def set_token(self, token):
        self._data["TOKEN"] = token
        super(ConfiguracionCI,self)._guardar_archivo_configuracion()

    def set_servidor_ci(self, servidor_ci):
        self._data["SERVIDOR_CI"] = servidor_ci
        super(ConfiguracionCI,self)._guardar_archivo_configuracion()

    def get_api_url(self):
        return self._data["API_URL"]

    def get_repositorio(self):
        return self._data["REPOSITORIO"]

    def get_usuario(self):
        return self._data["USUARIO"]

    def get_token(self):
        return self._data["TOKEN"]

    def get_servidor_ci(self):
        return self._data["SERVIDOR_CI"]