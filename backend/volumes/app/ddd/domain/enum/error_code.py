from enum import Enum, unique


@unique
class ErrorCode(Enum):
    NO_ERROR = "000"
    NOT_FOUND = "404"
    CONFLICT = "409"

    @property
    def str_value(self) -> str:
        return str(self.value)
