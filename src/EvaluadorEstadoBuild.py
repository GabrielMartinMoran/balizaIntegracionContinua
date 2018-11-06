from ClienteTravis import ClienteTravis
from ConfiguracionBaliza import ConfiguracionBaliza
try:
    from ManejadorLedRGB import ManejadorLedRGB
    from EstadoABuzzer import EstadoABuzzer
    import _thread
except:
    #Si no pudo importar machine
    pass
import gc

class EvaluadorEstadoBuild:

    def __init__(self):
        self.estado_build = None
        try:
            self.clienteTravis = ClienteTravis(ConfiguracionBaliza.instancia.get_configuracion_travis())
            self.manejador_led_RGB = ManejadorLedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
            self.estadoABuzzer = EstadoABuzzer(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
        except:
            #Si ocurre algun error de inicializacion para testing
            pass

    def evaluar_estado(self):
        estado_actual = self.clienteTravis.get_estado()
        if(estado_actual != self.estado_build):
            self.estado_build = estado_actual
            print("CAMBIO DE ESTADO DEL BUILD A:",self.estado_build)
            _thread.start_new_thread(self.activar_led,([]))
            self.estadoABuzzer.set_estado(self.estado_build)
        gc.collect()

    def activar_led(self):
        self.manejador_led_RGB.set_estado(self.estado_build)