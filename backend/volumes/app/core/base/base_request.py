
from abc import ABCMeta

from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel
from sqlmodel._compat import SQLModelConfig


class BaseRequest(SQLModel, metaclass=ABCMeta):
    """
    リクエストスキーマのベース.

    camelCaseの入力をsnake_caseに変換する
    """

    model_config = SQLModelConfig(
        populate_by_name=True,
        alias_generator=to_camel,
    )
