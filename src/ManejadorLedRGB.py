from time import sleep
from json import loads
import ImportadorMultiplataforma
CLRGB = ImportadorMultiplataforma.importar("ControladorLedRGB")
from EstadoBuild import EstadoBuild
from EstadoBuild import EstadoNoEspecificadoException


class ColorNoEncontradoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class ManejadorLedRGB:

    __COLORES_ESTADOS = {
        EstadoBuild.PASSED:             "VERDE",
        EstadoBuild.FAILED:             "ROJO",
        EstadoBuild.RUNNING:            "CYAN",
        EstadoBuild.CONNECTION_ERROR:   "AMARILLO",
        EstadoBuild.ACCESS_DENIED:      "MAGENTA"
    }

    def __init__(self, configuracion_led_rgb):
        self.__COLORES_LED = self.__obtener_recurso_json("ColoresLed.json")
        self.__controlador_led_rgb = CLRGB.ControladorLedRGB(
            configuracion_led_rgb)
        self.apagar_led()

    def __obtener_recurso_json(self, nombre_archivo):
        archivo = open("./resources/" + nombre_archivo, 'r')
        json = loads(archivo.read())
        archivo.close()
        return json
    
    def set_estado(self, estado):
        if(estado in self.__COLORES_ESTADOS):
            self.parpadear(self.__COLORES_ESTADOS[estado])
        else:
            raise EstadoNoEspecificadoException("El estado " + estado + " no esta especificado")

    def apagar_led(self):
        self.__controlador_led_rgb.set_rgb((0, 0, 0))

    def set_color(self, color):
        self.__controlador_led_rgb.set_rgb(self.__COLORES_LED[color])

    def parpadear(self, color):
        for i in range(3):
            self.set_color(color)
            sleep(0.2)
            self.apagar_led()
            sleep(0.2)
        self.set_color(color)


def main():
    pass


if __name__ == '__main__':
    main()
