import subprocess

DEPLOY_SCRIPTS = [
    ("./../../src/boot.py","boot.py"),
    ("./../../src/main.py","main.py"),
    ("./../../src/ConfiguracionBaliza.py","ConfiguracionBaliza.py"),
    ("./../../src/Configuracion.py","Configuracion.py"),
    ("./../../src/ConfiguracionTravis.py","ConfiguracionTravis.py"),
    ("./../../src/ConfiguracionRed.py","ConfiguracionRed.py"),
    ("./../../src/ConfiguracionLedRGB.py","ConfiguracionLedRGB.py"),
    ("./../../src/HttpRequests.py","HttpRequests.py"),
    ("./../../src/EstadoBuild.py","EstadoBuild.py"),
    ("./../../src/ClienteCI.py","ClienteCI.py"),
    ("./../../src/ClienteTravis.py","ClienteTravis.py"),
    ("./../../src/LoopPrincipal.py","LoopPrincipal.py"),
    ("./../../src/EvaluadorEstadoBuild.py","EvaluadorEstadoBuild.py"),
    ("./../../src/ControladorLed.py","ControladorLed.py"),
    ("./../../src/ControladorLedRGB.py","ControladorLedRGB.py"),
    ("./../../src/ManejadorLedRGB.py","ManejadorLedRGB.py"),
    ("./../../src/ColoresLed.py","ColoresLed.py"),
    ("./../../src/ControladorBuzzer.py","ControladorBuzzer.py"),
    ("./../../src/ManejadorBuzzer.py","ManejadorBuzzer.py"),
    ("./../../src/ConfiguracionBuzzer.py","ConfiguracionBuzzer.py"),
    ("webrepl_cfg.py","webrepl_cfg.py") #PARA CONFIGURAR WEBREPL
]

for x in DEPLOY_SCRIPTS:
    print("TRANSFIRIENDO ARCHIVO",DEPLOY_SCRIPTS.index(x)+1,"DE",len(DEPLOY_SCRIPTS))
    print("Desde:",x[0],"a:",x[1])
    bashCommand = "python webrepl_cli.py -p Passw0rd "+x[0]+" 192.168.4.1:8266:"+x[1]
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    lines = output.splitlines()
    print(lines[len(lines)-1])
    print("\n--------------------------------------------------------------------\n")
print("LA TRANSFERENCIA DE ARCHIVOS HA FINALIZADO CON EXITO!\n")