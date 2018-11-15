from ClienteTravis import ClienteTravis
from ClienteGitLab import ClienteGitLab
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
from gc import collect
import ServidoresCI
collect()

class EvaluadorEstadoBuild:

    def __init__(self):
        self.estado_build = None
        self.__utilizar_servidor_ci_correcto()
    
    def evaluar_cambio_de_estado(self):
        if(not self.__servidor_ci_actual_correcto()):
            self.__utilizar_servidor_ci_correcto()
        estado_actual = self.cliente_ci.get_estado()
        hay_nuevo_estado = estado_actual != self.estado_build
        if(hay_nuevo_estado):
            self.estado_build = estado_actual
        collect()
        return (hay_nuevo_estado, self.estado_build)

    def __servidor_ci_actual_correcto(self):
        return ConfiguracionBaliza.instancia.get_configuracion_ci().get_servidor_ci() == self.__servidor_actual

    def __utilizar_servidor_ci_correcto(self):
        servidor_ci = ConfiguracionBaliza.instancia.get_configuracion_ci().get_servidor_ci()
        self.__servidor_actual = servidor_ci
        if(servidor_ci == ServidoresCI.GITLAB):            
            self.cliente_ci = ClienteGitLab(ConfiguracionBaliza.instancia.get_configuracion_ci())
        else:
            #Si es travis o no esta definido
            self.cliente_ci = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_ci())
        collect()
