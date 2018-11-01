from EvaluadorEstadoBuild import EvaluadorEstadoBuild
import time

evaluador = EvaluadorEstadoBuild()

while(True):
    evaluador.evaluar_estado()
    time.sleep(0.2)
