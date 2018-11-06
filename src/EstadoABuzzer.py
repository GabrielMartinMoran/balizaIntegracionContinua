from EstadoBuild import EstadoBuild
from Reproductor import Reproductor

class EstadoABuzzer:
    CANCIONES_ESTADOS = {
        EstadoBuild.PASSED:           "PASSED",
        EstadoBuild.FAILED:           "FAILED",
        EstadoBuild.RUNNING:          "RUNNING",
        EstadoBuild.CONNECTION_ERROR: "CONNECTION_ERROR",
        EstadoBuild.ACCESS_DENIED:    "ACCESS_DENIED"
    }

    def __init__(self, configuracion_buzzer):
        self.reproductor = Reproductor(configuracion_buzzer)
    
    def set_estado(self, estado):
        self.reproductor.reproducir(self.CANCIONES_ESTADOS[estado])

