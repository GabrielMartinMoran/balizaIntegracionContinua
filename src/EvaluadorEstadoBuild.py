from ClienteTravis import ClienteTravis
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorLedRGB import *
import gc

class EvaluadorEstadoBuild:

    def __init__(self):
        self.estado_build = None
        self.clienteTravis = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_travis())
        self.manejador_led_RGB = ManejadorLedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())

    def evaluar_estado(self):
        estado_actual = self.clienteTravis.get_estado()
        if(estado_actual != self.estado_build):
            self.estado_build = estado_actual
            print("CAMBIO DE ESTADO DEL BUILD A:",self.estado_build)
            self.manejador_led_RGB.set_estado(self.estado_build)
        gc.collect()
