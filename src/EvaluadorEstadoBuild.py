from ClienteTravis import ClienteTravis
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
import gc

class EvaluadorEstadoBuild:

    def __init__(self):
        self.estado_build = None
        try:
            self.clienteTravis = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_travis())
        except:
            #Si ocurre algun error de inicializacion para testing
            pass
    
    def evaluar_cambio_de_estado(self):
        estado_actual = self.clienteTravis.get_estado()
        hay_nuevo_estado = estado_actual != self.estado_build
        if(hay_nuevo_estado):
            self.estado_build = estado_actual
        gc.collect()
        return (hay_nuevo_estado, self.estado_build)