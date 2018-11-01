from Configuracion import Configuracion

class ConfiguracionRed(Configuracion):

    def __init__(self):
        self._ARCHIVO_CONFIGURACION = "configuracion_red.json"
        self._data = {
            "SSID"  : None,
            "CLAVE" : None
        }
        super(ConfiguracionRed,self)._cargar_archivo_configuracion()

    def _set_valores_data(self, SSID, clave):
        self.set_SSID(SSID)
        self.set_clave(clave)

    """
    Dado un SSID de red y una clave establece la configuracion
    """
    def configurar(self, SSID, clave):
        super(ConfiguracionRed,self).configurar(SSID, clave)

    def set_SSID(self, SSID):
        self._data["SSID"] = SSID
        super(ConfiguracionRed,self)._guardar_archivo_configuracion()

    def set_clave(self, clave):
        self._data["CLAVE"] = clave
        super(ConfiguracionRed,self)._guardar_archivo_configuracion()

    def get_SSID(self):
        return self._data["SSID"]

    def get_clave(self):
        return self._data["CLAVE"]