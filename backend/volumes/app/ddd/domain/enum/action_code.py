from enum import Enum, unique


@unique
class ActionCode(Enum):
    GET = "0"
    # LIST = "1"
    CREATE = "2"
    PATCH = "3"
    # UPSERT = "4"
    DELETE = "5"
    QUERY = "9"
