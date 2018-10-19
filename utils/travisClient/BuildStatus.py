from enum import Enum

class BuildStatus(Enum):
    PASSED = 1
    FAILED = 2
    RUNNING = 3
    NOT_YET_BUILT = 4
    CONNECTION_ERROR = 5
    ACCESS_DENIED = 6