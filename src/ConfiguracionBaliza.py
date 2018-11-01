from ConfiguracionTravis import ConfiguracionTravis
from ConfiguracionRed import ConfiguracionRed
from ConfiguracionGPIO import ConfiguracionGPIO

class ConfiguracionBaliza:

    class __ConfiguracionBaliza:

        __configuracion_travis = None
        __configuracion_red = None
        __configuracion_GPIO = None

        def __init__(self):
            self.__configuracion_travis = ConfiguracionTravis()
            self.__configuracion_red = ConfiguracionRed()
            self.__configuracion_GPIO = ConfiguracionGPIO()

        def set_configuracion_travis(self, configuracion_travis):
            self.__configuracion_travis = configuracion_travis
        
        def set_configuracion_red(self, configuracion_red):
            self.__configuracion_red = configuracion_red

        def set_configuracion_GPIO(self, configuracion_GPIO):
            self.__configuracion_GPIO = configuracion_GPIO

        def get_configuracion_travis(self):
            return self.__configuracion_travis
        
        def get_configuracion_red(self):
            return self.__configuracion_red

        def get_configuracion_GPIO(self):
            return self.__configuracion_GPIO

        """
        Borra la configuacion de todas las subconfiguraciones
        """
        def borrar_configuracion(self, borrar_archivos_configuracion=False):
            self.__configuracion_travis.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_red.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_GPIO.borrar_configuracion(borrar_archivos_configuracion)

        def _delete_singleton(self):
            del ConfiguracionBaliza.instancia
            ConfiguracionBaliza.instancia = None

    instancia = None

    def __init__(self):
        if not ConfiguracionBaliza.instancia:
            ConfiguracionBaliza.instancia = ConfiguracionBaliza.__ConfiguracionBaliza()

    def __getattr__(self, nombre):
        return getattr(self.instancia, nombre)