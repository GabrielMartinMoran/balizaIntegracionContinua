import time
import network

class ConectorWiFi():

    def __init__(self, configuracion_red):
        self.__configuracion_red = configuracion_red

    def __inicializar_estacion(self):
        self.__sta_if = network.WLAN(network.STA_IF)
        self.__sta_if.active(True)

    def conectar(self):
        self.__inicializar_estacion()
        cantidad_intentos_conexion = 1
        while(not self.esta_conectado()):
            print("Tratando de conectarse a la red",self.__configuracion_red.get_SSID())
            print("\nIntento número",cantidad_intentos_conexion)
            self.__sta_if.connect(self.__configuracion_red.get_SSID(), self.__configuracion_red.get_clave())
            cantidad_intentos_conexion += 1
            time.sleep(5)
        print("Se ha establecido la conexión con la red:",self.__configuracion_red.get_SSID())

    def esta_conectado(self):
        return self.__sta_if.isconnected()     