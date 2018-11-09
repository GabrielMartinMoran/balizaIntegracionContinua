from EvaluadorEstadoBuild import EvaluadorEstadoBuild
from TraductorEstadoABuzzer import TraductorEstadoABuzzer
from TraductorEstadoALedRGB import TraductorEstadoALedRGB
from TraductorEstadoAConsola import TraductorEstadoAConsola
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
from time import sleep

def iniciar():
    manejador_de_estados = ManejadorDeEstados()
    estadoABuzzer = TraductorEstadoABuzzer(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
    estadoALedRGB = TraductorEstadoALedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
    estadoAConsola = TraductorEstadoAConsola()
    manejador_de_estados.agregar_salida(estadoABuzzer)
    manejador_de_estados.agregar_salida(estadoALedRGB)
    manejador_de_estados.agregar_salida(estadoAConsola)
    evaluador = EvaluadorEstadoBuild()

    while(True):
        hay_nuevo_estado, estado_actual = evaluador.evaluar_cambio_de_estado()
        if(hay_nuevo_estado):
            manejador_de_estados.set_estado(estado_actual)
        sleep(0.2)