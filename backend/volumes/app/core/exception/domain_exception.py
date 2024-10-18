import json



class DomainException(Exception):

    def __init__(self, error_code: str, status_code: int, description: str, **kwargs) -> None:
        super().__init__(description)
        self.__error_code: str = error_code
        self.__status_code: int = status_code
        self.__message: dict = {
            "description": description,
        } | kwargs
        self.__detail: dict = {
            "status_code": self.__status_code,
        } | self.__message

    def __str__(self) -> str:
        return json.dumps(self.__detail)
    
    def error_code(self) -> str:
        return self.__error_code

    def status_code(self) -> int:
        return self.__status_code

    def message(self) -> dict:
        return self.__message
