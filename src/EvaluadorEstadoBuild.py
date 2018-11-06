from ClienteTravis import ClienteTravis
from ConfiguracionBaliza import ConfiguracionBaliza
#try:
from ManejadorLedRGB import ManejadorLedRGB
from EstadoABuzzer import EstadoABuzzer
from EstadoALedRGB import EstadoALedRGB
import _thread
#except:
    #Si no pudo importar machine
#    pass
import gc

class EvaluadorEstadoBuild:

    def __init__(self):
        self.estado_build = None
        try:
            self.clienteTravis = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_travis())
            self.estadoABuzzer = EstadoABuzzer(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
            self.estadoALedRGB = EstadoALedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
        except:
            #Si ocurre algun error de inicializacion para testing
            pass

    def evaluar_estado(self):
        estado_actual = self.clienteTravis.get_estado()
        if(estado_actual != self.estado_build):
            self.estado_build = estado_actual
            print("CAMBIO DE ESTADO DEL BUILD A:",self.estado_build)
            self.estadoABuzzer.set_estado(self.estado_build)
            self.estadoALedRGB.set_estado(self.estado_build)
        gc.collect()