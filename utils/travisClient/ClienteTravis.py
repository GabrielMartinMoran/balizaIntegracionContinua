import json
from ClienteCI import *
from BuildStatus import BuildStatus
import gc
try:
    import urequests as http_request
except:
    import requests as http_request

TRAVIS_API_URL = "https://api.travis-ci.org"
#TRAVIS_API_URL = "http://127.0.0.1:8080"

class ClienteTravis(ClienteCI):    
    

    def __init__(self, usuario_github, repositorio, token):
        self.__usuario_github = usuario_github
        self.__repositorio = repositorio
        self.__token = token
    
    def configurar(self, usuario_github, repositorio, token):
        self.__init__(usuario_github, repositorio, token)

    def __consultar_estado(self):
        #Definimos los headers para el request
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token " + self.__token
        }
        response = http_request.get(TRAVIS_API_URL + "/repo/" +
                            self.__usuario_github +"%2F"+ self.__repositorio +
                            "/builds?limit=1&sort_by=finished_at:desc", headers=headers)
        response.close()
        return response.text

    def __obtener_estado(self, response):
        #Si existe algun problema de credenciales, usuario o repositorio incorrectos
        if(response == "access denied"):         
            return BuildStatus.ACCESS_DENIED
        #Transformamos el response a JSON
        reponse_json = json.loads(response)
        #Si no fue compilado nunca
        if(len(reponse_json['builds']) == 0):
            return BuildStatus.NOT_YET_BUILT
        #Traemos el string que representa el estado del build
        estado = reponse_json['builds'][0]['state']
        #Si paso los tests
        if(estado == "passed"):
            return BuildStatus.PASSED
        #Si fallo los tests
        elif(estado == "failed"):
            return BuildStatus.FAILED
        #Si en este momento esta corriendo los tests
        else:            
            return BuildStatus.RUNNING

    def get_estado(self):
        try:
            response = self.__consultar_estado()
        except http_request.exceptions.ConnectionError:
            #Si existe error de conexion
            return BuildStatus.CONNECTION_ERROR
        estado = self.__obtener_estado(response)
        #Ejecutamos el Garbage Collector
        gc.collect()
        return estado

def main():
    token = "9cHb1xMQyaGSSSsi6xTW5Q"
    repositorio = "dyasc-2018"
    usuario = "MrKupo"
    cliente = ClienteTravis(usuario, repositorio, token)
    print(cliente.get_estado())
    #cliente.consultar_estado()

if __name__ == '__main__':
    main()