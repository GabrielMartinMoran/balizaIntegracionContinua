from ClienteTravis import *
import time
import gc

def main():
    token = "9cHb1xMQyaGSSSsi6xTW5Q"
    repositorio = "dyasc-2018"
    usuario = "MrKupo"
    cliente = ClienteTravis(usuario, repositorio, token)
    estado_anterior = None
    cantidad_requests = 0
    while(True):
        estado_actual = cliente.get_estado()
        cantidad_requests += 1
        print("REQUEST N°:",cantidad_requests)
        if(estado_actual != estado_anterior):
            estado_anterior = estado_actual
            print("\n------ CAMBIO DE ESTADO A:",estado_actual,"------\n")
        else:
            print("PERMANECE EN ESTADO:",estado_actual)
        gc.collect()
        time.sleep(1)

if __name__ == '__main__':
    main()