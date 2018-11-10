#Archivo main del ESP32
from ConfiguracionBaliza import ConfiguracionBaliza

IP_HOST_CONFIGURACION = "192.168.4.1"#"localhost"
PUERTO_HOST_CONFIGURACION = 80#8080

#Instanciamos el singleton de configuracion
configuracionBaliza = ConfiguracionBaliza()

config_travis = ConfiguracionBaliza.instancia.get_configuracion_travis()
config_red = ConfiguracionBaliza.instancia.get_configuracion_red()
config_led_rgb = ConfiguracionBaliza.instancia.get_configuracion_led_RGB()
config_buzzer = ConfiguracionBaliza.instancia.get_configuracion_buzzer()

config_led_rgb.configurar(
    12,
    13,
    14
)

config_buzzer.configurar(
    32
)

from ConectorWiFi import ConectorWiFi
conector_wifi = ConectorWiFi(config_red)
if(config_red.esta_configurada()):
    conector_wifi.conectar(cantidad_intentos = 5)

from _thread import start_new_thread
from ServidorHTTPConfiguracion import ServidorHTTPConfiguracion
#Iniciamos el servidor HTTP
start_new_thread(ServidorHTTPConfiguracion,(IP_HOST_CONFIGURACION, PUERTO_HOST_CONFIGURACION, config_travis, config_red))

import LoopPrincipal
#Iniciamos el loop principal
LoopPrincipal.iniciar()