import json
import os

class Configuracion:

    def __init__(self):
        self._ARCHIVO_CONFIGURACION = "configuracion.json"
        self._data = {}
        self._cargar_archivo_configuracion()

    def _set_valores_data(self, *argv):
        for x in argv:
            self._data[str(x).upper()] = x

    def configurar(self, *argv):
        self._set_valores_data(*argv)
        self._guardar_archivo_configuracion()

    """
    Se considera que esta configurada si todos los parametros de configuracion son
    distinto de None
    """
    def esta_configurada(self):
        if len(self._data) == 0:
            return False
        for x in self._data:
            if(self._data[x] == None):
                return False
        return True

    def __get_path_archivo_configuracion(self):
        #path_scipt = os.path.realpath(__file__)
        #path_directorio = os.path.dirname(path_scipt)
        #return os.path.join(path_directorio, self._ARCHIVO_CONFIGURACION)
        return os.getcwd() + '/' + self._ARCHIVO_CONFIGURACION

    def _guardar_archivo_configuracion(self):
        f = open(self.__get_path_archivo_configuracion(), "w")
        f.write(json.dumps(self._data))
        f.close()
    
    def _cargar_archivo_configuracion(self):
        if(not self.existe_archivo_configuracion()):
            return False
        f = open(self.__get_path_archivo_configuracion(),"r")
        self._data = json.loads(f.read())
        f.close()

    def __borrar_archivo_configuracion(self):
        if(self.existe_archivo_configuracion()):
            os.remove(self.__get_path_archivo_configuracion())

    """
    Devuelve True si existe guardado un archivo de configuracion
    """
    def existe_archivo_configuracion(self):
        lista_directorio = os.listdir()
        return self._ARCHIVO_CONFIGURACION in lista_directorio
        #return os.path.isfile(self.__get_path_archivo_configuracion())

    """
    Borra la configuracion actual y si el parametro borrar_archivo_configuracion esta en True tambien elimina el archivo guardado
    """
    def borrar_configuracion(self, borrar_archivo_configuracion=False):
        for x in self._data:
            self._data[x] = None
        if(borrar_archivo_configuracion):
            self.__borrar_archivo_configuracion()