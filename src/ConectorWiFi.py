import time
import ImportadorMultiplataforma
network = ImportadorMultiplataforma.importar("network")

class ConectorWiFi:

    def __init__(self, configuracion_red, tiempo_entre_intentos = 5):
        self.__configuracion_red = configuracion_red
        self.__sta_if = None
        self.__tiempo_entre_intentos = tiempo_entre_intentos

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
            time.sleep(self.__tiempo_entre_intentos)
        print("Se ha establecido la conexión con la red:",self.__configuracion_red.get_SSID())

    def esta_conectado(self):
        if(self.__sta_if == None):
            return False
        return self.__sta_if.isconnected()