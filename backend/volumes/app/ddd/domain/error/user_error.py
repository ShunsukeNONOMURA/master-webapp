from enum import Enum

from fastapi import status

from app.core.base import BaseError

# status.HTTP_400_BAD_REQUEST
# status.HTTP_409_CONFLICT
from app.ddd.domain import ErrorCode


# Enumでエラー情報を定義
class ErrorEnum(Enum):
    INVALID_INPUT = (4001, status.HTTP_404_NOT_FOUND, "Invalid input provided")
    USER_NOT_FOUND = (1404, status.HTTP_404_NOT_FOUND, "User with ID {user_id} was not found.")
    SERVER_ERROR = (5000, status.HTTP_404_NOT_FOUND, "Internal server error")

class UserNotFoundError(BaseError):
    def __init__(self, user_id: str) -> None:
        message = "User with ID '{user_id}' was not found."
        super().__init__(
            error_code=ErrorCode.NOT_FOUND.str_value,
            status_code=status.HTTP_404_NOT_FOUND,
            description=message,
            # user_id=user_id,
            parameters={"user_id": user_id}  # 修正
        )

class UserDuplicationError(BaseError):
    def __init__(self, user_id: str) -> None:
        message = "User with ID '{user_id}' already exists."
        super().__init__(
            error_code=ErrorCode.CONFLICT.str_value,
            status_code=status.HTTP_409_CONFLICT,
            description=message,
            # user_id=user_id,
            parameters={
                "user_id": user_id,
                "hoge": "huga",
            }  # 修正
        )

class UserUpdateConflictError(BaseError):
    def __init__(self, user_id: str) -> None:
        message = "User with ID '{user_id}' update conlict."
        super().__init__(
            error_code=ErrorCode.CONFLICT.str_value,
            status_code=status.HTTP_409_CONFLICT,
            description=message,
            # user_id=user_id,
            parameters={"user_id": user_id}  # 修正
        )


# class UserReportDuplicationError(BaseError):
#     def __init__(self, user_report_id: str) -> None:
#         message = "User Report with ID '{user_report_id}' already exists."
#         super().__init__(
#             error_code=ErrorCode.CONFLICT.str_value,
#             status_code=status.HTTP_409_CONFLICT,
#             description=message,
#             user_report_id=user_report_id,
#         )


class UserAuthError(BaseError):
    def __init__(self) -> None:
        message = "auth error."
        super().__init__(
            error_code=ErrorCode.UNAUTHORIZED.str_value,
            status_code=status.HTTP_401_UNAUTHORIZED,
            description=message,
            # user_id=user_id,
            # parameters={"user_id": user_id}  # 修正
        )
