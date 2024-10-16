import json


class DomainException(Exception):

    def __init__(self, status_code: int, description: str, **kwargs) -> None:
        super().__init__(description)
        self.__status_code: int = status_code
        self.__message: dict = {
            "description": description,
        } | kwargs
        self.__detail: dict = {
            "status_code": self.__status_code,
        } | self.__message

    def __str__(self) -> str:
        return json.dumps(self.__detail)

    def status_code(self) -> int:
        return self.__status_code

    def message(self) -> dict:
        return self.__message