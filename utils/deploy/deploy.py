import subprocess

DEPLOY_SCRIPTS = [
    ("./../travisClient/boot.py","boot.py"),
    ("./../travisClient/main.py","main.py"),
    ("./../travisClient/ConfiguracionBaliza.py","ConfiguracionBaliza.py"),
    ("./../travisClient/Configuracion.py","Configuracion.py"),
    ("./../travisClient/ConfiguracionTravis.py","ConfiguracionTravis.py"),
    ("./../travisClient/ConfiguracionRed.py","ConfiguracionRed.py"),
    ("./../travisClient/ConfiguracionGPIO.py","ConfiguracionGPIO.py"),
    ("./../travisClient/HttpRequests.py","HttpRequests.py"),
    ("./../travisClient/EstadoBuild.py","EstadoBuild.py"),
    ("./../travisClient/ClienteCI.py","ClienteCI.py"),
    ("./../travisClient/ClienteTravis.py","ClienteTravis.py"),
    ("./../travisClient/LoopPrincipal.py","LoopPrincipal.py"),
    ("./../travisClient/EvaluadorEstadoBuild.py","EvaluadorEstadoBuild.py"),
    ("webrepl_cfg.py","webrepl_cfg.py") #PARA CONFIGURAR WEBREPL
]

for x in DEPLOY_SCRIPTS:
    print("DEPLOYING FROM",x[0],"TO",x[1])
    bashCommand = "python3 webrepl_cli.py -p Passw0rd "+x[0]+" 192.168.4.1:8266:"+x[1]
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    print(output)
    print("---------------------------------------------------------------------------\n")