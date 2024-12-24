class UserNotFoundError(Exception):
    pass
    # TODO(nonomura): ErrorCode, HTTPStatus, Message設計
    # def __init__(self) -> None:
    #     super().__init__(
    #         error_code="999",
    #         status_code=status.HTTP_404_NOT_FOUND,
    #         description="Digital Buddy is not found",
    #     )

class UserDuplicationError(Exception):
    pass
