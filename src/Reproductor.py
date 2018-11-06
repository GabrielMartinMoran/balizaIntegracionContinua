import ImportadorMultiplataforma
CB = ImportadorMultiplataforma.importar("ControladorBuzzer")
import time

class PorcentajeInvalidoException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje

class CancionNoEncontradaException(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje


class Reproductor:
    
    def __init__(self, configuracion_buzzer):
        self.controladorBuzzer = CB.ControladorBuzzer(configuracion_buzzer.get_pin_buzzer())
        self.controladorBuzzer.set_intensidad(self.__map__(30))
        self.nota = {"SILENCIO": 0,
                     "B0": 31,
                     "C1": 33,
                     "CS1": 35,
                     "D1": 37,
                     "DS1": 39,
                     "E1": 41,
                     "F1": 44,
                     "FS1": 46,
                     "G1": 49,
                     "GS1": 52,
                     "A1": 55,
                     "AS1": 58,
                     "B1": 62,
                     "C2": 65,
                     "CS2": 69,
                     "D2": 73,
                     "DS2": 78,
                     "E2": 82,
                     "F2": 87,
                     "FS2": 93,
                     "G2": 98,
                     "GS2": 104,
                     "A2": 110,
                     "AS2": 117,
                     "B2": 123,
                     "C3": 131,
                     "CS3": 139,
                     "D3": 147,
                     "DS3": 156,
                     "E3": 165,
                     "F3": 175,
                     "FS3": 185,
                     "G3": 196,
                     "GS3": 208,
                     "A3": 220,
                     "AS3": 233,
                     "B3": 247,
                     "C4": 262,
                     "CS4": 277,
                     "D4": 294,
                     "DS4": 311,
                     "E4": 330,
                     "F4": 349,
                     "FS4": 370,
                     "G4": 392,
                     "GS4": 415,
                     "A4": 440,
                     "AS4": 466,
                     "B4": 494,
                     "C5": 523,
                     "CS5": 554,
                     "D5": 587,
                     "DS5": 622,
                     "E5": 659,
                     "F5": 698,
                     "FS5": 740,
                     "G5": 784,
                     "GS5": 831,
                     "A5": 880,
                     "AS5": 932,
                     "B5": 988,
                     "C6": 1047,
                     "CS6": 1109,
                     "D6": 1175,
                     "DS6": 1245,
                     "E6": 1319,
                     "F6": 1397,
                     "FS6": 1480,
                     "G6": 1568,
                     "GS6": 1661,
                     "A6": 1760,
                     "AS6": 1865,
                     "B6": 1976,
                     "C7": 2093,
                     "CS7": 2217,
                     "D7": 2349,
                     "DS7": 2489,
                     "E7": 2637,
                     "F7": 2794,
                     "FS7": 2960,
                     "G7": 3136,
                     "GS7": 3322,
                     "A7": 3520,
                     "AS7": 3729,
                     "B7": 3951,
                     "C8": 4186,
                     "CS8": 4435,
                     "D8": 4699,
                     "DS8": 4978}
        self.canciones = {"mario": ["E7",
                                    "E7",
                                    "SILENCIO",
                                    "E7",
                                    "SILENCIO",
                                    "C7",
                                    "E7",
                                    "SILENCIO",
                                    "G7",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "G6",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "C7",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "G6",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "E6",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "A6",
                                    "SILENCIO",
                                    "B6",
                                    "SILENCIO",
                                    "AS6",
                                    "A6",
                                    "SILENCIO",
                                    "G6",
                                    "E7",
                                    "SILENCIO",
                                    "G7",
                                    "A7",
                                    "SILENCIO",
                                    "F7",
                                    "G7",
                                    "SILENCIO",
                                    "E7",
                                    "SILENCIO",
                                    "C7",
                                    "D7",
                                    "B6",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "C7",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "G6",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "E6",
                                    "SILENCIO",
                                    "SILENCIO",
                                    "A6",
                                    "SILENCIO",
                                    "B6",
                                    "SILENCIO",
                                    "AS6",
                                    "A6",
                                    "SILENCIO",
                                    "G6",
                                    "E7",
                                    "SILENCIO",
                                    "G7",
                                    "A7",
                                    "SILENCIO",
                                    "F7",
                                    "G7",
                                    "SILENCIO",
                                    "E7",
                                    "SILENCIO",
                                    "C7",
                                    "D7",
                                    "B6",
                                    "SILENCIO",
                                    "SILENCIO"],
                            "PASSED":["G7",
                                    "SILENCIO",
                                    "D7",
                                    "SILENCIO",
                                    "F4",
                                    "E7",
                                    "B6",
                                    "SILENCIO","SILENCIO"],
                            "FAILED":["E7",
                                    "SILENCIO",
                                    "C4",
                                    "E5",
                                    "SILENCIO",
                                    "G2",
                                    "SILENCIO","SILENCIO"],
                            "RUNNING": ["B0","D4","SILENCIO","A5","B3","SILENCIO","SILENCIO"],
                            "CONNECTION_ERROR": ["A4","F4","E3","SILENCIO","B4","SILENCIO","SILENCIO"],
                            "ACCESS_DENIED": ["E7",
                                    "SILENCIO",
                                    "C3",
                                    "E7",
                                    "SILENCIO","SILENCIO"]}


    def __map__(self, n):
        if(n < 0 or n > 100):
            raise PorcentajeInvalidoException("El porcentaje debe estar entre 0 y 100")
        return int((float(n) / 100) * 1023)

    def reproducir(self, cancion):
        if(cancion in self.canciones):
            for nota in self.canciones[cancion]:
                if(nota == "SILENCIO"):
                    self.controladorBuzzer.set_intensidad(self.__map__(0))
                else:
                    self.controladorBuzzer.set_intensidad(self.__map__(30))
                    self.controladorBuzzer.set_frecuencia(self.nota[nota])
                #time.sleep_ms(150)
                time.sleep(0.150)
        else:
            raise CancionNoEncontradaException("La cancion " + cancion + " no esta especificada")

def main():
    import ConfiguracionBuzzer
    conf = ConfiguracionBuzzer.ConfiguracionBuzzer()
    conf.configurar(1)
    reproductor = Reproductor(conf)
    reproductor.reproducir("mario")
    conf.borrar_configuracion(True)

if __name__ == '__main__':
    main()