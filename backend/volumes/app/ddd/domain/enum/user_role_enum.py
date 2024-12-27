from enum import Enum, unique


@unique
class UserRoleEnum(str, Enum):
    ADMIN = "00"
    GENERAL = "10"
    GUEST = "99"
