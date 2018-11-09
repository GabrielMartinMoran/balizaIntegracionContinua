from Reproductor import Reproductor

class TraductorEstadoABuzzer:

    def __init__(self, configuracion_buzzer):
        self.reproductor = Reproductor(configuracion_buzzer)
    
    def set_estado(self, estado):
        self.reproductor.reproducir(estado)