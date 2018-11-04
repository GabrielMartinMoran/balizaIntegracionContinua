import socket
import gc
from _thread import start_new_thread

class ServidorHTTP():

    def __init__(self, host, puerto, clientes_maximos = 5, imprimir_log = False):
        self.__configurar(host, puerto, clientes_maximos, imprimir_log)
        self.__ruteos = {}
    
    def __configurar(self, host, puerto, clientes_maximos, imprimir_log):
        self.__host = host
        self.__puerto = puerto
        self.__clientes_maximos = clientes_maximos
        self.__imprimir_log = imprimir_log

    def iniciar(self, threaded = True):
        self.__servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.__servidor.bind((self.__host, self.__puerto))
        self.__servidor.listen(self.__clientes_maximos)
        if(self.__imprimir_log):
            print('Iniciado servidor en host:', self.__host, "puerto:", self.__puerto)
        if(threaded):
            start_new_thread(self.__escuchar_clientes,())
        else:
            self.__escuchar_clientes()

    def __es_request(self, string):
        if(string[:3]=='GET'):
            return True
        return False

    def detener(self):
        self.__servidor.shutdown(1)
        self.__servidor.close()

    def __mapear_parametros(self, parametros):
        mapa = {}
        for x in parametros:
            param = x.split('=')
            mapa[param[0]] = param[1]
        return mapa

    def __dividir_url(self, url):
        data = url.replace('?',' ')
        data = data.replace('&',' ')
        return data.split(' ')

    def __atender_request(self, request_str):
        data = request_str[4:].split(' ')[0]
        request_data = self.__dividir_url(data)
        url = request_data[0]
        parametros = self.__mapear_parametros(request_data[1:])
        if(self.__imprimir_log):
            print("REQUEST TO:",url)
        return self.__rutear(url,parametros)

    def __atender_cliente(self, conexion):
        cl_file = conexion.makefile('rwb', 0)
        data = b''
        while True:
            line = cl_file.readline()
            if not line or line == b'\r\n':
                break
            data += line
        
        decoded_data = data.decode('utf-8')
        response = None
        if(self.__es_request(decoded_data)):
            response = self.__atender_request(decoded_data)
        conexion.sendall(response.encode())
        response = None
        conexion.close()
        gc.collect()

    def __escuchar_clientes(self):
        while True:
            conexion, addr = self.__servidor.accept()
            if(self.__imprimir_log):
                print('Cliente conectado desde:', addr)
            start_new_thread(self.__atender_cliente,(conexion,))

    """
    La funcion debe permitir recibir un parametro ya que se utilizara de la manera funcion(parametros_url)
    """
    def agregar_ruteo(self, url, funcion):
        self.__ruteos[url] = funcion

    def __generar_response(self, data, error = False):
        codigo = None
        if(not error):
            codigo = "200 OK"
        else:
            codigo = "404 Not Found"
        return "HTTP/1.1 " + codigo + "\r\nContent-Type: text/html\r\n\r\n" + data


    def __rutear(self, url, parametros):
        if(url in self.__ruteos):
            return self.__generar_response(self.__ruteos[url](parametros))
        else:
            return self.__generar_response("URL NO ENCONTRADA", error = True)







