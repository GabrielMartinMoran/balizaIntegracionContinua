from EstadoABuzzer import EstadoABuzzer
from EstadoALedRGB import EstadoALedRGB
from _thread import start_new_thread

class ManejadorDeEstados:
    def __init__(self):
        self.lista_de_salidas = []
    
    def agregar_salida(self, salida):
        self.lista_de_salidas.append(salida)
    
    def set_estado(self, estado):
        for salida in self.lista_de_salidas:
            start_new_thread(self.__set_estado,(salida,estado))

    def __set_estado(self, salida, estado):
        salida.set_estado(estado)