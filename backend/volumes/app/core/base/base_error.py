from typing import Any, TypedDict, Unpack

from app.ddd.infrastructure.util import recursive_to_camel


class ErrorParams(TypedDict, total=False):
    user_id: str

class BaseError(Exception):
    def __init__(self, error_code: str, status_code: int, description: str, **kwargs: Unpack[ErrorParams]) -> None:
        """
        BaseError.

        継承して利用するアプリエラークラス

        Args:
            error_code: ERROR CODE
            status_code: HTTP STATUS CODE
            description: エラーメッセージ
            kwargs: その他パラメータ（エラーメッセージに追加する文言など）

        """
        super().__init__(description)
        self.__error_code: str = error_code # application error code
        self.__status_code: int = status_code # http status code
        self.__message: dict[str, Any] = {
            "description": description.format(**kwargs),
        } | kwargs
        self.__detail: dict[str, Any] = {
            "error_code": self.__error_code,
            "status_code": self.__status_code,
        } | self.__message

    # def __str__(self) -> str:
    #     return json.dumps(self.__detail)

    # def error_code(self) -> str:
    #     return self.__error_code

    def status_code(self) -> int:
        return self.__status_code

    def detail(self) -> dict[str, Any]:
        return self.__detail

    def camel_detail(self) -> dict[str, Any]:
        return recursive_to_camel(self.detail())

    def response(self) -> dict[str, Any]:
        """エラーレスポンスの内容を生成."""
        return {
            # "model": DynamicModel,
            # "description":  self.__message["description"], # Discriptionを指定する場合
            "content": {
                "application/json": {
                    "example": {
                        "detail": [
                            self.camel_detail(),
                        ]
                    }
                }
            },
        }

