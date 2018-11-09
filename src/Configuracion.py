from json import loads, dumps
from os import getcwd, remove, listdir

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
        return getcwd() + '/' + self._ARCHIVO_CONFIGURACION

    def _guardar_archivo_configuracion(self):
        f = open(self.__get_path_archivo_configuracion(), "w")
        f.write(dumps(self._data))
        f.close()
    
    def _cargar_archivo_configuracion(self):
        if(not self.existe_archivo_configuracion()):
            return False
        f = open(self.__get_path_archivo_configuracion(),"r")
        self._data = loads(f.read())
        f.close()

    def __borrar_archivo_configuracion(self):
        if(self.existe_archivo_configuracion()):
            remove(self.__get_path_archivo_configuracion())

    """
    Devuelve True si existe guardado un archivo de configuracion
    """
    def existe_archivo_configuracion(self):
        lista_directorio = listdir()
        return self._ARCHIVO_CONFIGURACION in lista_directorio

    """
    Borra la configuracion actual y si el parametro borrar_archivo_configuracion esta en True tambien elimina el archivo guardado
    """
    def borrar_configuracion(self, borrar_archivo_configuracion=False):
        for x in self._data:
            self._data[x] = None
        if(borrar_archivo_configuracion):
            self.__borrar_archivo_configuracion()