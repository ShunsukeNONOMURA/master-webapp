from enum import Enum

from fastapi import status

from app.core.base import BaseError

# status.HTTP_400_BAD_REQUEST
# status.HTTP_409_CONFLICT
from app.ddd.domain import ErrorCode


# Enumでエラー情報を定義
class ErrorEnum(Enum):
    INVALID_INPUT = (4001, status.HTTP_404_NOT_FOUND, "Invalid input provided")
    USER_NOT_FOUND = (1404, status.HTTP_404_NOT_FOUND, "Group with ID {group_id} was not found.")
    SERVER_ERROR = (5000, status.HTTP_404_NOT_FOUND, "Internal server error")

class GroupNotFoundError(BaseError):
    def __init__(self, group_id: str) -> None:
        message = "Group with ID '{group_id}' was not found."
        super().__init__(
            error_code=ErrorCode.NOT_FOUND.str_value,
            status_code=status.HTTP_404_NOT_FOUND,
            description=message,
            # group_id=group_id,
            parameters={"group_id": group_id}  # 修正
        )

class GroupDuplicationError(BaseError):
    def __init__(self, group_id: str) -> None:
        message = "Group with ID '{group_id}' already exists."
        super().__init__(
            error_code=ErrorCode.CONFLICT.str_value,
            status_code=status.HTTP_409_CONFLICT,
            description=message,
            # group_id=group_id,
            parameters={
                "group_id": group_id,
                "hoge": "huga",
            }  # 修正
        )

class GroupUpdateConflictError(BaseError):
    def __init__(self, group_id: str) -> None:
        message = "Group with ID '{group_id}' update conlict."
        super().__init__(
            error_code=ErrorCode.CONFLICT.str_value,
            status_code=status.HTTP_409_CONFLICT,
            description=message,
            # group_id=group_id,
            parameters={"group_id": group_id}  # 修正
        )


# class GroupReportDuplicationError(BaseError):
#     def __init__(self, group_report_id: str) -> None:
#         message = "Group Report with ID '{group_report_id}' already exists."
#         super().__init__(
#             error_code=ErrorCode.CONFLICT.str_value,
#             status_code=status.HTTP_409_CONFLICT,
#             description=message,
#             group_report_id=group_report_id,
#         )


class GroupAuthError(BaseError):
    def __init__(self) -> None:
        message = "auth error."
        super().__init__(
            error_code=ErrorCode.UNAUTHORIZED.str_value,
            status_code=status.HTTP_401_UNAUTHORIZED,
            description=message,
            # group_id=group_id,
            # parameters={"group_id": group_id}  # 修正
        )
