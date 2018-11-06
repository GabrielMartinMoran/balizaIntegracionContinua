from EvaluadorEstadoBuild import EvaluadorEstadoBuild
from EstadoABuzzer import EstadoABuzzer
from EstadoALedRGB import EstadoALedRGB
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
import time

manejador_de_estados = ManejadorDeEstados()
estadoABuzzer = EstadoABuzzer(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
estadoALedRGB = EstadoALedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
manejador_de_estados.agregar_salida(estadoABuzzer)
manejador_de_estados.agregar_salida(estadoALedRGB)
evaluador = EvaluadorEstadoBuild(manejador_de_estados)

while(True):
    evaluador.evaluar_estado()
    time.sleep(0.2)