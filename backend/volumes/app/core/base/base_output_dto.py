from abc import ABCMeta

from sqlmodel import SQLModel


class BaseOutputDTO(SQLModel, metaclass=ABCMeta):
    """UseCaseのBaseOutputDTOベース."""

# class BaseStreamOutputDTO(SQLModel, metaclass=ABCMeta):
#     """UseCaseのBaseStreamOutputDTOベース."""

#     event: str
#     data: dict[str, Any] | str

#     model_config = SQLModelConfig(
#         populate_by_name=True,
#         alias_generator=to_camel,
#     )

#     def to_sse(self) -> str:
#         """
#         eventとdataをSSEデータ形式に変換する関数。.

#         Returns:
#             str: SSEフォーマットの文字列。.

#         """
#         try:
#             # JSONデータを文字列に変換
#             json_string = json.dumps(self.data, ensure_ascii=False)
#         except (TypeError, ValueError) as e:
#             msg = "Invalid JSON data"
#             raise ValueError(msg) from e
#         else:
#             # SSEフォーマットに変換
#             return f"event: {self.event}\ndata: {json_string}\n\n"

