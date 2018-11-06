from ClienteTravis import ClienteTravis
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
from EstadoABuzzer import EstadoABuzzer
from EstadoALedRGB import EstadoALedRGB
import gc

class EvaluadorEstadoBuild:

    def __init__(self):
        self.estado_build = None
        try:
            self.clienteTravis = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_travis())
            self.manejador_de_estados = ManejadorDeEstados()
            estadoABuzzer = EstadoABuzzer(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
            estadoALedRGB = EstadoALedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
            self.manejador_de_estados.agregar_salida(estadoABuzzer)
            self.manejador_de_estados.agregar_salida(estadoALedRGB)
        except:
            #Si ocurre algun error de inicializacion para testing
            pass

    def evaluar_estado(self):
        estado_actual = self.clienteTravis.get_estado()
        if(estado_actual != self.estado_build):
            self.estado_build = estado_actual
            print("CAMBIO DE ESTADO DEL BUILD A:",self.estado_build)
            self.manejador_de_estados.set_estado(estado_actual)
        gc.collect()