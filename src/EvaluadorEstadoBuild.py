from ClienteTravis import ClienteTravis
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
import gc

class EvaluadorEstadoBuild:

    def __init__(self, manejador_de_estados):
        self.estado_build = None
        try:
            self.manejador_de_estados = manejador_de_estados
            self.clienteTravis = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_travis())
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