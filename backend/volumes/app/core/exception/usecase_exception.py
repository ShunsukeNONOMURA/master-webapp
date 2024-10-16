import json


class UseCaseException(Exception):

    def __init__(self, description: str, **kwargs) -> None:
        super().__init__(description)
        self.__message = {
            "description": description,
        } | kwargs

    def __str__(self) -> str:
        return json.dumps(self.__message)

    def message(self) -> dict:
        return self.__message