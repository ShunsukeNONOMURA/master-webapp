from enum import Enum, unique


@unique
class ResourceCode(Enum):
    HEALTH = "00"
    USER = "10"
    PAYMENT = "20"
