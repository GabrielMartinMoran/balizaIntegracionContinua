from Configuracion import Configuracion

class ConfiguracionLedRGB(Configuracion):

    def __init__(self):
        self._ARCHIVO_CONFIGURACION = "configuracion_Led_RGB.json"
        self._data = {
            "PIN_LED_ROJO"   : None,
            "PIN_LED_VERDE"  : None,
            "PIN_LED_AZUL"   : None,
        }
        super(ConfiguracionLedRGB,self)._cargar_archivo_configuracion()

    def _set_valores_data(self, pin_led_rojo, pin_led_verde, pin_led_azul):
        self.set_pin_led_rojo(pin_led_rojo)
        self.set_pin_led_verde(pin_led_verde)
        self.set_pin_led_azul(pin_led_azul)

    """
    Dado los pines correpsondientes a los puertos GPIO donde se encuentran conectados los
    leds rojo, verde y azul, establece la configuracion
    """
    def configurar(self, pin_led_rojo, pin_led_verde, pin_led_azul):
        super(ConfiguracionLedRGB,self).configurar(pin_led_rojo, pin_led_verde, pin_led_azul)

    def set_pin_led_rojo(self, pin_led_rojo):
        self._data["PIN_LED_ROJO"] = pin_led_rojo
        super(ConfiguracionLedRGB,self)._guardar_archivo_configuracion()

    def set_pin_led_verde(self, pin_led_verde):
        self._data["PIN_LED_VERDE"] = pin_led_verde
        super(ConfiguracionLedRGB,self)._guardar_archivo_configuracion()

    def set_pin_led_azul(self, pin_led_azul):
        self._data["PIN_LED_AZUL"] = pin_led_azul
        super(ConfiguracionLedRGB,self)._guardar_archivo_configuracion()

    def get_pin_led_rojo(self):
        return self._data["PIN_LED_ROJO"]

    def get_pin_led_verde(self):
        return self._data["PIN_LED_VERDE"]

    def get_pin_led_azul(self):
        return self._data["PIN_LED_AZUL"]