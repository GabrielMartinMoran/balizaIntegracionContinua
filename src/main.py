"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~ CONSTANTES ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""

IP_HOST_CONFIGURACION = "192.168.4.1"
PUERTO_HOST_CONFIGURACION = 80
CANTIDAD_INTENTOS_CONEXION_WIFI = 5

"""
~~~~~~~~~~~~~~~~~~~~~~~~~~ CONFIGURACION ~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
from ConfiguracionBaliza import ConfiguracionBaliza

#Instanciamos el singleton de configuracion
configuracion_baliza_singleton = ConfiguracionBaliza()

config_ci = ConfiguracionBaliza.instancia.get_configuracion_ci()
config_red = ConfiguracionBaliza.instancia.get_configuracion_red()
config_led_rgb = ConfiguracionBaliza.instancia.get_configuracion_led_RGB()
config_buzzer = ConfiguracionBaliza.instancia.get_configuracion_buzzer()

#Solo configuramos en caso de que no se encuentre el archivo de configuracion para no
#consumir usos de la EPROM
if(not config_led_rgb.esta_configurada()):
    config_led_rgb.configurar(12, 13, 14)

if(not config_buzzer.esta_configurada()):
    config_buzzer.configurar(32)

"""
~~~~~~~~~~~~~~~~~~~~~ CONEXION A WiFi INICIAL ~~~~~~~~~~~~~~~~~~~~~
"""
from ConectorWiFi import ConectorWiFi

conector_wifi = ConectorWiFi(config_red)
if(config_red.esta_configurada()):
    conector_wifi.conectar(cantidad_intentos = CANTIDAD_INTENTOS_CONEXION_WIFI)

"""
~~~~~~~~~~~~~~~~~ SERVIDOR HTTP DE CONFIGURACION ~~~~~~~~~~~~~~~~~~
"""
from _thread import start_new_thread
from ServidorHTTPConfiguracion import ServidorHTTPConfiguracion

#Iniciamos el servidor HTTP
start_new_thread(ServidorHTTPConfiguracion,(IP_HOST_CONFIGURACION, PUERTO_HOST_CONFIGURACION, config_ci, config_red))

"""
~~~~~~~~~~~~~~~~~ INICIO DE LA LOGICA DE LA BALIZA ~~~~~~~~~~~~~~~~~
"""
import LoopPrincipal

#Iniciamos el loop principal
LoopPrincipal.iniciar()