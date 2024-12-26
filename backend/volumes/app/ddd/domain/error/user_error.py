from enum import Enum

from fastapi import status

from app.core.base import BaseError


# Enumでエラー情報を定義
class ErrorInfo(Enum):
    INVALID_INPUT = (4001, "Invalid input provided")
    USER_NOT_FOUND = (1404, "User with ID {user_id} was not found.")
    SERVER_ERROR = (5000, "Internal server error")

class UserNotFoundError(BaseError):
    def __init__(self, user_id: str) -> None:
        message = f"User with ID {user_id} was not found."
        super().__init__(
            error_code="999",
            status_code=status.HTTP_404_NOT_FOUND,
            description=message
        )

class UserDuplicationError(Exception):
    pass


class UserUpdateConflictError(Exception):
    pass
