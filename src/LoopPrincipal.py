from EvaluadorEstadoBuild import EvaluadorEstadoBuild
from ManejadorLedRGB import ManejadorLedRGB
from ReproductorMusical import ReproductorMusical
from ImpresorPorConsola import ImpresorPorConsola
from ConfiguracionBaliza import ConfiguracionBaliza
from NotificadorDeSalidas import NotificadorDeSalidas
from time import sleep

def iniciar():
    notificador_de_salidas = NotificadorDeSalidas()
    reproductor_musical = ReproductorMusical(ConfiguracionBaliza.instancia.get_configuracion_buzzer())
    manejador_led_rgb = ManejadorLedRGB(ConfiguracionBaliza.instancia.get_configuracion_led_RGB())
    impresor_consola = ImpresorPorConsola()
    notificador_de_salidas.agregar_salida(reproductor_musical)
    notificador_de_salidas.agregar_salida(manejador_led_rgb)
    notificador_de_salidas.agregar_salida(impresor_consola)
    evaluador = EvaluadorEstadoBuild()

    while(True):
        hay_nuevo_estado, estado_actual = evaluador.evaluar_cambio_de_estado()
        if(hay_nuevo_estado):
            notificador_de_salidas.set_estado(estado_actual)
        sleep(0.2)