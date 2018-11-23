import ImportadorMultiplataforma
CB = ImportadorMultiplataforma.importar("ControladorBuzzer")
from json import loads
from time import sleep
from EstadoBuild import EstadoBuild
from EstadoBuild import EstadoNoEspecificadoException

class PorcentajeInvalidoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class CancionNoEncontradaException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class ReproductorMusical:

    __CANCIONES_ESTADOS = {
        EstadoBuild.PASSED:             "PASSED",
        EstadoBuild.FAILED:             "FAILED",
        EstadoBuild.RUNNING:            "RUNNING",
        EstadoBuild.CONNECTION_ERROR:   "CONNECTION_ERROR",
        EstadoBuild.ACCESS_DENIED:      "ACCESS_DENIED"
    }
    
    def __init__(self, configuracion_buzzer):
        self.__controlador_buzzer = CB.ControladorBuzzer(configuracion_buzzer.get_pin_buzzer())
        self.__controlador_buzzer.set_intensidad(self.__map__(30))
        self.__NOTAS_MUSICALES = self.__obtener_recurso_json("NotasMusicales.json")
        self.__CANCIONES = self.__obtener_recurso_json("Canciones.json")

    def __obtener_recurso_json(self, nombre_archivo):
        archivo = open("./resources/" + nombre_archivo, 'r')
        json = loads(archivo.read())
        archivo.close()
        return json
    
    def set_estado(self, estado):
        if(estado in self.__CANCIONES_ESTADOS):
            self.reproducir(self.__CANCIONES_ESTADOS[estado])
        else:
            raise EstadoNoEspecificadoException("El estado " + estado + " no esta especificado")

    def __map__(self, n):
        if(n < 0 or n > 100):
            raise PorcentajeInvalidoException("El porcentaje debe estar entre 0 y 100")
        return int((float(n) / 100) * 1023)

    def reproducir(self, cancion):
        if(cancion in self.__CANCIONES):
            for nota in self.__CANCIONES[cancion]:
                if(nota == "SILENCIO"):
                    self.__controlador_buzzer.set_intensidad(self.__map__(0))
                else:
                    self.__controlador_buzzer.set_intensidad(self.__map__(30))
                    self.__controlador_buzzer.set_frecuencia(self.__NOTAS_MUSICALES[nota])
                sleep(0.150)
        else:
            raise CancionNoEncontradaException("La cancion " + cancion + " no esta especificada")

def main():
    import ConfiguracionBuzzer
    conf = ConfiguracionBuzzer.ConfiguracionBuzzer()
    conf.configurar(1)
    reproductor = ReproductorMusical(conf)
    reproductor.reproducir("mario")
    conf.borrar_configuracion(True)

if __name__ == '__main__':
    main()