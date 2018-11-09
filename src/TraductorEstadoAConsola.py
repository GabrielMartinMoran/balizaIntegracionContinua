from EstadoBuild import EstadoBuild

class TraductorEstadoAConsola:

    __mensaje_de_cambio_de_estado = "CAMBIO DE ESTADO DEL BUILD A:"

    def __init__(self):
        pass
    
    def set_estado(self, estado):
        print(self.__mensaje_de_cambio_de_estado, estado)