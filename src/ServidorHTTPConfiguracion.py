from ServidorHTTP import *

PATH_CARPETA_PLANTILLAS = "./plantillas_html/"
PLANTILLA_HTML = PATH_CARPETA_PLANTILLAS + "plantilla.html"
CONFIGURACION_RED = PATH_CARPETA_PLANTILLAS + "configuracion_red.html"
CONFIGURACION_CI = PATH_CARPETA_PLANTILLAS + "configuracion_ci.html"

class ServidorHTTPConfiguracion:
    
    ETIQUETA_REEEMPLAZO = "{{FORMULARIOS_CONFIGURACION}}"
    ETIQUETA_HOST = "{{HOST_URL}}"

    def __init__(self, host, puerto, configuracion_travis, configuracion_red):
        self.__host = host
        self.__puerto = puerto
        self.__configuracion_travis = configuracion_travis
        self.__configuracion_red = configuracion_red
        self.__servidor_HTTP = ServidorHTTP(host, puerto)
        self.__definir_ruteos()
        self.__servidor_HTTP.iniciar()

    def __definir_ruteos(self):
        self.__servidor_HTTP.agregar_ruteo("/",self.get_html_configuracion)
        self.__servidor_HTTP.agregar_ruteo("/set_configuracion_travis",self.set_configuracion_travis)
        self.__servidor_HTTP.agregar_ruteo("/set_configuracion_red",self.set_configuracion_red)

    def __get_contenido_archivo(self, path):
        archivo = open(path,'r')
        contenido = archivo.read()
        archivo.close()
        return contenido    

    def get_html_configuracion(self, *args):
        plantilla_html = self.__get_contenido_archivo(PLANTILLA_HTML)
        formulario_red = self.__get_contenido_archivo(CONFIGURACION_RED)
        formulario_ci = self.__get_contenido_archivo(CONFIGURACION_CI)
        plantilla_html = plantilla_html.replace(self.ETIQUETA_HOST, "http://"+self.__host+":"+str(self.__puerto))
        return plantilla_html.replace(self.ETIQUETA_REEEMPLAZO,formulario_red + formulario_ci)

    def set_configuracion_travis(self, parametros):
        self.__configuracion_travis.configurar(parametros["usuario"], parametros["repositorio"], parametros["token"])
        return "CONFIGURACION TRAVIS ESTABLECIDA"

    def set_configuracion_red(self, parametros):
        self.__configuracion_red.configurar(parametros["SSID"], parametros["clave"])
        return "CONFIGURACION RED ESTA"

    def detener(self):
        self.__servidor_HTTP.detener()