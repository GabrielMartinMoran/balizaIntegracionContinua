#Archivo main del ESP32
from ConfiguracionBaliza import ConfiguracionBaliza

#Instanciamos el singleton de configuracion
configuracionBaliza = ConfiguracionBaliza()

#Hardcodeamos las configuraciones
#Configuracion de Travis
TRAVIS_API_URL = "http://127.0.0.1:8080"
TOKEN = "9cHb1xMQyaGSSSsi6xTW5Q"
#TOKEN = "zIad7_tjIcVqyc3bo0agUw"
REPOSITORIO = "dyasc-2018"
USUARIO = "MrKupo"
#USUARIO = "cybercatnet"

#Configuracion de Red
SSID = "Fibertel WiFi589 2.4GHz"#"AP"
CLAVE = "00438829825"#"Passw0rd"

ConfiguracionBaliza.instancia.get_configuracion_travis().configurar(
    USUARIO,
    REPOSITORIO,
    TOKEN#,
    #TRAVIS_API_URL #COMENTAMOS PARA QUE USE LA API DE TRAVIS
)

config_red = ConfiguracionBaliza.instancia.get_configuracion_red()

config_red.configurar(
    SSID,
    CLAVE
)

config_led_rgb = ConfiguracionBaliza.instancia.get_configuracion_led_RGB()

config_led_rgb.configurar(
    12,
    13,
    14
)

config_buzzer = ConfiguracionBaliza.instancia.get_configuracion_buzzer()

config_buzzer.configurar(
    32
)

from ConectorWiFi import ConectorWiFi
conector_wifi = ConectorWiFi(config_red)
conector_wifi.conectar()

import LoopPrincipal
