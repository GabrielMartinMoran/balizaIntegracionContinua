html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8" />
        <title>Configuracion - Baliza de Integración Contínua</title>
    </head>
    <body class="mx-1">
        <h1>
            Configuracion de la Baliza de Integración Contínua
        </h1>
        <form class="mx-2">
            <br/>
            <h3>Configuración de Red</h3>
            <div class="row spacer col-lg-12 flex-wrap">
                <div class="row col-md-4">
                    <label for="textSSID" class="col-md-4 control-label">SSID de Red</label>
                    <div>
                        <input type="text" id="textSSID" name="textSSID"/>
                    </div>
                </div>
                <div class="row col-md-4">
                    <label for="textPassword" class="col-md-4 control-label">Clave de Red</label>
                    <div>
                        <input type="password" id="textPassword" name="textPassword"/>
                    </div>
                </div>
            </div>
            <br/>
            <h3>Configuración de Travis</h3>
            <div class="row spacer col-lg-12 flex-wrap">
                <div class="row col-md-4">
                    <label for="textUsername" class="col-md-4 control-label">Nombre de Usuario (Git)</label>
                    <div>
                        <input type="text" id="textUsername" name="textUsername"/>
                    </div>
                </div>
                <div class="row col-md-4">
                    <label for="textRepository" class="col-md-4 control-label">Nombre del Repositorio</label>
                    <div>
                        <input type="text" id="textRepository" name="textRepository"/>
                    </div>
                </div>
                
                <div class="row col-md-4">
                    <label for="textToken" class="col-md-4 control-label">Token de Travis</label>
                    <div>
                        <input type="text" id="textToken" name="textToken"/>
                    </div>
                </div>
            </div>
            <br/>
            <div class="row">
                <div class="col-md-2 col-xs-2 center-block"> 
                    <button type="submit" class="btn btn-primary">Enviar</button>
                </div>
            </div>
        </form>
    </body>
</html>
"""

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

s = socket.socket()
s.bind(addr)
s.listen(1)

print('listening on', addr)

def is_request(string):
    if(string[:3]=='GET'):
        return True
    return False

def make_response(request_str):
    url = request_str[4:].split(' ')[0]
    print("REQUEST TO:",url)
    if(url=="/"):
        return html
    elif(url=="/test"):
        return "ON TEST MODE!"
    else:
        return url

while True:
    cl, addr = s.accept()
    print('client connected from', addr)
    cl_file = cl.makefile('rwb', 0)
    response = None
    while True:
        line = cl_file.readline()
        decoded_line = line.decode('utf-8')
        if(is_request(decoded_line)):
            response = make_response(decoded_line)
        if not line or line == b'\r\n':
            break
    cl.send(response.encode())
    cl.close()