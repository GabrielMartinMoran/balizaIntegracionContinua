import json
from ClienteCI import *
from EstadoBuild import EstadoBuild
import gc
import HttpRequests
from ConfiguracionTravis import ConfiguracionTravis

class ClienteTravis(ClienteCI):    

    def __init__(self, configuracion_travis):
        self.set_configuracion_travis(configuracion_travis)

    def set_configuracion_travis(self, configuracion_travis):
        self.__configuracion_travis = configuracion_travis

    def get_configuracion_travis(self):
        return self.__configuracion_travis

    def __consultar_estado(self):
        #Definimos los headers para el request
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token " + self.__configuracion_travis.get_token()
        }
        request_url = (self.__configuracion_travis.get_api_url() + "/repo/" +
                            self.__configuracion_travis.get_usuario() +"%2F"+ self.__configuracion_travis.get_repositorio() +
                            "/builds?limit=1&sort_by=finished_at:desc")
        response = HttpRequests.get(request_url, headers=headers)
        return response.text

    def __parsear_estado(self, response_json):
        #Traemos el string que representa el estado del build
        estado = response_json['builds'][0]['state']
        #Si paso los tests
        if(estado == "passed"):
            return EstadoBuild.PASSED
        #Si fallo los tests
        elif(estado == "failed"):
            return EstadoBuild.FAILED
        #Si en este momento esta corriendo los tests
        else:            
            return EstadoBuild.RUNNING

    def __obtener_estado(self, response):
        #Si existe algun problema de credenciales, usuario o repositorio incorrectos
        if(response == "access denied"):         
            return EstadoBuild.ACCESS_DENIED
        #Transformamos el response a JSON
        response_json = json.loads(response)
        #Cuando ocurre un error al estar mal el nombre de usuario o el repositorio
        if('error_type' in response_json):
            return EstadoBuild.CONNECTION_ERROR
        #Si no fue compilado nunca
        if(len(response_json['builds']) == 0):
            return EstadoBuild.NOT_YET_BUILT
        return self.__parsear_estado(response_json)

    def get_estado(self):
        if(not self.__configuracion_travis.esta_configurada()):
            return EstadoBuild.CONNECTION_ERROR
        try:
            response = self.__consultar_estado()
        except HttpRequests.ConnectionError:
            #Si existe error de conexion
            return EstadoBuild.CONNECTION_ERROR
        estado = self.__obtener_estado(response)
        #Ejecutamos el Garbage Collector
        gc.collect()
        return estado