from ConfiguracionCI import ConfiguracionCI
from ConfiguracionRed import ConfiguracionRed
from ConfiguracionLedRGB import ConfiguracionLedRGB
from ConfiguracionBuzzer import ConfiguracionBuzzer

class ConfiguracionBaliza:

    class __ConfiguracionBaliza:

        __configuracion_ci = None
        __configuracion_red = None
        __configuracion_Led_RGB = None
        __configuracion_buzzer = None

        def __init__(self):
            self.__configuracion_ci = ConfiguracionCI()
            self.__configuracion_red = ConfiguracionRed()
            self.__configuracion_Led_RGB = ConfiguracionLedRGB()
            self.__configuracion_buzzer = ConfiguracionBuzzer()

        def set_configuracion_ci(self, configuracion_ci):
            self.__configuracion_ci = configuracion_ci
        
        def set_configuracion_red(self, configuracion_red):
            self.__configuracion_red = configuracion_red

        def set_configuracion_led_RGB(self, configuracion_led_RGB):
            self.__configuracion_Led_RGB = configuracion_led_RGB
        
        def set_configuracion_buzzer(self, configuracion_buzzer):
            self.__configuracion_buzzer = configuracion_buzzer

        def get_configuracion_ci(self):
            return self.__configuracion_ci
        
        def get_configuracion_red(self):
            return self.__configuracion_red

        def get_configuracion_led_RGB(self):
            return self.__configuracion_Led_RGB
        
        def get_configuracion_buzzer(self):
            return self.__configuracion_buzzer

        """
        Borra la configuacion de todas las subconfiguraciones
        """
        def borrar_configuracion(self, borrar_archivos_configuracion=False):
            self.__configuracion_ci.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_red.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_Led_RGB.borrar_configuracion(borrar_archivos_configuracion)
            self.__configuracion_buzzer.borrar_configuracion(borrar_archivos_configuracion)

        def _delete_singleton(self):
            del ConfiguracionBaliza.instancia
            ConfiguracionBaliza.instancia = None

    instancia = None

    def __init__(self):
        if not ConfiguracionBaliza.instancia:
            ConfiguracionBaliza.instancia = ConfiguracionBaliza.__ConfiguracionBaliza()

    def __getattr__(self, nombre):
        return getattr(self.instancia, nombre)