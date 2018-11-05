import ImportadorMultiplataforma
http_requests = ImportadorMultiplataforma.importar("requests")

#Excepcion a lanzar cuando ocurre un error de conexion
class ConnectionError(Exception):
    pass

def request(tipo, url, headers={}):
    try:
        response = http_requests.request(tipo, url, headers=headers)
    except Exception:
        raise ConnectionError()
    #print("RESPONSE")
    #print(help(response))
    #if(response != None):
    #    response.close()
    return response

def post(url, headers={}):
    return request('POST', url, headers)

def get(url, headers={}):
    return request('GET', url, headers)