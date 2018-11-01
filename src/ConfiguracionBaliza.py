from ConfiguracionTravis import ConfiguracionTravis
from ConfiguracionRed import ConfiguracionRed
from ConfiguracionLedRGB import ConfiguracionLedRGB

class ConfiguracionBaliza:

    class __ConfiguracionBaliza:

        __configuracion_travis = None
        __configuracion_red = None
        __configuracion_Led_RGB = None

        def __init__(self):
            self.__configuracion_travis = ConfiguracionTravis()
            self.__configuracion_red = ConfiguracionRed()
            self.__configuracion_Led_RGB = ConfiguracionLedRGB()

        def set_configuracion_travis(self, configuracion_travis):
            self.__configuracion_travis = configuracion_travis
        
        def set_configuracion_red(self, configuracion_red):
            self.__configuracion_red = configuracion_red

        def set_configuracion_led_RGB(self, configuracion_led_RGB):
            self.__configuracion_Led_RGB = configuracion_led_RGB

        def get_configuracion_travis(self):
            return self.__configuracion_travis
        
        def get_configuracion_red(self):
            return self.__configuracion_red

        def get_configuracion_led_RGB(self):
            return self.__configuracion_Led_RGB

        """
        Borra la configuacion de todas las subconfiguraciones
        """
        def borrar_configuracion(self, borrar_archivos_configuracion=False):
            self.__configuracion_travis.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_red.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_Led_RGB.borrar_configuracion(borrar_archivos_configuracion)

        def _delete_singleton(self):
            del ConfiguracionBaliza.instancia
            ConfiguracionBaliza.instancia = None

    instancia = None

    def __init__(self):
        if not ConfiguracionBaliza.instancia:
            ConfiguracionBaliza.instancia = ConfiguracionBaliza.__ConfiguracionBaliza()

    def __getattr__(self, nombre):
        return getattr(self.instancia, nombre)