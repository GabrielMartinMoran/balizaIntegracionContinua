from json import loads
from ClienteCI import *
from EstadoBuild import EstadoBuild
from gc import collect
import HttpRequests
from ConfiguracionCI import ConfiguracionCI
collect()

class ClienteGitLab(ClienteCI):    

    def __init__(self, configuracion_ci):
        self.set_configuracion_ci(configuracion_ci)

    def set_configuracion_ci(self, configuracion_ci):
        self.__configuracion_ci = configuracion_ci

    def get_configuracion_ci(self):
        return self.__configuracion_ci

    def __consultar_estado(self):
        #Definimos los headers para el request
        headers = {
            "PRIVATE-TOKEN": self.__configuracion_ci.get_token()
        }
        request_url = (self.__configuracion_ci.get_api_url() + "/projects/" +
                            self.__configuracion_ci.get_usuario() +"%2F"+ self.__configuracion_ci.get_repositorio() +
                            "/pipelines?per_page=1&page=1")
        response = HttpRequests.get(request_url, headers=headers)
        return response.text

    def __parsear_estado(self, response_json):
        #Traemos el string que representa el estado del build
        estado = response_json['status']
        #Si paso los tests
        if(estado == "success"):
            return EstadoBuild.PASSED
        #Si fallo los tests
        elif(estado == "failed"):
            return EstadoBuild.FAILED
        #Si en este momento esta corriendo los tests
        else:            
            return EstadoBuild.RUNNING

    def __obtener_estado(self, response):        
        #Transformamos el response a JSON
        response_json = loads(response)
        #Si no fue compilado nunca
        if(type(response_json) == list):
            if(len(response_json) == 0):
                return EstadoBuild.NOT_YET_BUILT
            else:
                return self.__parsear_estado(response_json[0])
        if("message" in response_json):
            #Si existe algun problema de credenciales
            if(response_json['message'] == "401 Unauthorized"):         
                return EstadoBuild.ACCESS_DENIED        
            #Cuando ocurre un error al estar mal el nombre de usuario o el repositorio
            if(response_json['message'] == "404 Project Not Found"):
                return EstadoBuild.CONNECTION_ERROR
        #Si no es ninguna de estas
        return EstadoBuild.CONNECTION_ERROR

    def get_estado(self):
        if(not self.__configuracion_ci.esta_configurada()):
            return EstadoBuild.CONNECTION_ERROR
        try:
            response = self.__consultar_estado()
        except HttpRequests.ConnectionError:
            #Si existe error de conexion
            return EstadoBuild.CONNECTION_ERROR
        estado = self.__obtener_estado(response)
        #Ejecutamos el Garbage Collector
        collect()
        return estado