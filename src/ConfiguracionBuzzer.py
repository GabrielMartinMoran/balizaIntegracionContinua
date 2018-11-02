from Configuracion import Configuracion

class ConfiguracionBuzzer(Configuracion):

    def __init__(self):
        self._ARCHIVO_CONFIGURACION = "configuracion_buzzer.json"
        self._data = {
            "PIN_BUZZER"   : None
        }
        super(ConfiguracionBuzzer,self)._cargar_archivo_configuracion()

    def _set_valores_data(self, pin_buzzer):
        self.set_pin_buzzer(pin_buzzer)

    """
    Dado los pines correpsondientes a los puertos GPIO donde se encuentran conecta el buzzer
    """
    def configurar(self, pin_buzzer):
        super(ConfiguracionBuzzer,self).configurar(pin_buzzer)

    def set_pin_buzzer(self, pin_buzzer):
        self._data["PIN_BUZZER"] = pin_buzzer
        super(ConfiguracionBuzzer,self)._guardar_archivo_configuracion()

    def get_pin_buzzer(self):
        return self._data["PIN_BUZZER"]