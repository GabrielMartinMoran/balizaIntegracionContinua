from ServidorHTTP import *
from json import dumps

PATH_CARPETA_PLANTILLAS = "./plantillas_html/"
PLANTILLA_HTML = PATH_CARPETA_PLANTILLAS + "plantilla.html"
CONFIGURACION_RED = PATH_CARPETA_PLANTILLAS + "configuracion_red.html"
CONFIGURACION_CI = PATH_CARPETA_PLANTILLAS + "configuracion_ci.html"

class ServidorHTTPConfiguracion:
    
    ETIQUETA_REEEMPLAZO = "{{FORMULARIOS_CONFIGURACION}}"
    ETIQUETA_HOST = "{{HOST_URL}}"

    def __init__(self, host, puerto, configuracion_ci, configuracion_red):
        self.__host = host
        self.__puerto = puerto
        self.__configuracion_ci = configuracion_ci
        self.__configuracion_red = configuracion_red
        self.__servidor_HTTP = ServidorHTTP(host, puerto)
        self.__definir_ruteos()
        self.__servidor_HTTP.iniciar()

    def __definir_ruteos(self):
        self.__servidor_HTTP.agregar_ruteo("/",self.get_html_configuracion)
        self.__servidor_HTTP.agregar_ruteo("/set_configuracion_ci",self.set_configuracion_ci)
        self.__servidor_HTTP.agregar_ruteo("/set_configuracion_red",self.set_configuracion_red)
        self.__servidor_HTTP.agregar_ruteo("/get_configuracion_ci",self.get_configuracion_ci)
        self.__servidor_HTTP.agregar_ruteo("/get_configuracion_red",self.get_configuracion_red)

    def __get_contenido_archivo(self, path):
        archivo = open(path,'rb')
        contenido = archivo.read().decode('utf-8')
        archivo.close()
        return contenido    

    def get_html_configuracion(self, *args):
        plantilla_html = self.__get_contenido_archivo(PLANTILLA_HTML)
        formulario_red = self.__get_contenido_archivo(CONFIGURACION_RED)
        formulario_ci = self.__get_contenido_archivo(CONFIGURACION_CI)
        plantilla_html = plantilla_html.replace(self.ETIQUETA_HOST, "http://"+self.__host+":"+str(self.__puerto))
        return plantilla_html.replace(self.ETIQUETA_REEEMPLAZO,formulario_red + formulario_ci)

    def set_configuracion_ci(self, parametros):
        if(parametros["APIurl"] != ""):
            self.__configuracion_ci.configurar(parametros["usuario"], parametros["repositorio"], parametros["token"], api_url=parametros["APIurl"], servidor_ci=parametros["servidorCI"])
        else:
            self.__configuracion_ci.configurar(parametros["usuario"], parametros["repositorio"], parametros["token"], servidor_ci=parametros["servidorCI"])
        return '{"resultado":"Configuracion CI establecida!"}'

    def set_configuracion_red(self, parametros):
        self.__configuracion_red.configurar(parametros["SSID"], parametros["clave"])
        return '{"resultado":"Configuracion de red establecida!"}'

    def get_configuracion_ci(self, parametros):
        response = {
            "usuario" : self.__configuracion_ci.get_usuario(),
            "repositorio" : self.__configuracion_ci.get_repositorio(),
            "token" : self.__configuracion_ci.get_token(),
            "APIurl" : self.__configuracion_ci.get_api_url(),
            "servidorCI" : self.__configuracion_ci.get_servidor_ci()
        }
        return dumps(response)

    def get_configuracion_red(self, parametros):
        response = {
            "SSID" : self.__configuracion_red.get_SSID(),
            "clave" : self.__configuracion_red.get_clave(),
        }
        return dumps(response)

    def detener(self):
        self.__servidor_HTTP.detener()