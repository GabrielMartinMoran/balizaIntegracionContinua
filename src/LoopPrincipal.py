from EvaluadorEstadoBuild import EvaluadorEstadoBuild
from EstadoABuzzer import EstadoABuzzer
from EstadoALedRGB import EstadoALedRGB
from ConfiguracionBaliza import ConfiguracionBaliza
from ManejadorDeEstados import ManejadorDeEstados
from time import sleep

def iniciar():
    manejador_de_estados = ManejadorDeEstados()
    estadoABuzzer = EstadoABuzzer(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
    estadoALedRGB = EstadoALedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
    manejador_de_estados.agregar_salida(estadoABuzzer)
    manejador_de_estados.agregar_salida(estadoALedRGB)
    evaluador = EvaluadorEstadoBuild()

    while(True):
        hay_nuevo_estado, estado_actual = evaluador.evaluar_cambio_de_estado()
        if(hay_nuevo_estado):
            print("CAMBIO DE ESTADO DEL BUILD A:", estado_actual)
            manejador_de_estados.set_estado(estado_actual)
        sleep(0.2)