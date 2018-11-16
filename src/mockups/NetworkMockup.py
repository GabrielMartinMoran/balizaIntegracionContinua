STA_IF = "STA_IF"

class WLAN:

    __activo = False
    __conectado = False

    def __init__(self, *args):
        pass

    def active(self, valor):
        self.__activo = valor
        return valor

    def isconnected(self):
        return self.__conectado

    def connect(self, SSID, clave):
        self.__conectado = True

    def disconnect(self):
        self.__conectado = False