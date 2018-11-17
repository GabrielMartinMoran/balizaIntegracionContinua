class EstadoBuild:
    PASSED = "PASSED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    NOT_YET_BUILT = "NOT_YET_BUILT"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    ACCESS_DENIED = "ACCESS_DENIED"

class EstadoNoEspecificadoException(Exception):
    def __init__(self, mensaje = ""):
        self.mensaje = mensaje