from ClienteCI import *
from BuildStatus import BuildStatus
import gc
try:
    import urequests as http_request
except:
    import requests as http_request

class ClienteTravis(ClienteCI):

    global TRAVIS_API_URL
    #TRAVIS_API_URL = "https://api.travis-ci.org"
    TRAVIS_API_URL = "http://127.0.0.1:8080"

    def __init__(self, usuario_github, repositorio, token):
        self.__usuario_github = usuario_github
        self.__repositorio = repositorio
        self.__token = token
    
    def configurar(self, usuario_github, repositorio, token):
        self.__init__(usuario_github, repositorio, token)
    
    def __obtener_estado(self):
        #Definimos los headers para el request
        headers = {
            "Travis-API-Version": "3",
            "Authorization": "token " + self.__token
        }
        response = None
        estado = None
        try:
            response = http_request.get(TRAVIS_API_URL + "/repo/"+ self.__usuario_github +"%2F"+ self.__repositorio + "/builds?limit=1&sort_by=finished_at:desc", headers=headers)
        except http_request.exceptions.ConnectionError:
            #Si existe error de conexion
            return BuildStatus.CONNECTION_ERROR
        #Si existe algun problema de credenciales, usuario o repositorio incorrectos
        if(response.text == "access denied"):
            response.close()
            return BuildStatus.ACCESS_DENIED
        #Si no fue compilado nunca
        if(len(response.json()['builds']) == 0):
            response.close()
            return BuildStatus.NOT_YET_BUILT
        build_status = response.json()['builds'][0]['state']
        #Si paso los tests
        if(build_status == "passed"):
            estado = BuildStatus.PASSED
        #Si fallo los tests
        elif(build_status == "failed"):
            estado = BuildStatus.FAILED
        else:
            #Si en este momento esta corriendo los tests
            estado = BuildStatus.RUNNING
        return estado

    def get_estado(self):
        estado = self.__obtener_estado()
        #Ejecutamos el Garbage Collector
        gc.collect()
        return estado

def main():
    token = "9cHb1xMQyaGSSSsi6xTW5Q"
    repositorio = "dyasc-2018"
    usuario = "MrKupo"
    cliente = ClienteTravis(usuario, repositorio, token)
    print(cliente.get_estado())

if __name__ == '__main__':
    main()