"""
from enum import Enum

class EstadoBuild(Enum):
    PASSED = 1
    FAILED = 2
    RUNNING = 3
    NOT_YET_BUILT = 4
    CONNECTION_ERROR = 5
    ACCESS_DENIED = 6
"""

class EstadoBuild:
    PASSED = "PASSED"
    FAILED = "FAILED"
    RUNNING = "RUNNING"
    NOT_YET_BUILT = "NOT_YET_BUILT"
    CONNECTION_ERROR = "CONNECTION_ERROR"
    ACCESS_DENIED = "ACCESS_DENIED"