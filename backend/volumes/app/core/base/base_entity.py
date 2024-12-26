from abc import ABCMeta

from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel
from sqlmodel._compat import SQLModelConfig


class BaseEntity(SQLModel, metaclass=ABCMeta):
    model_config = SQLModelConfig(
        populate_by_name=True, # 名前とエイリアスの入力の両方を許容する
        alias_generator=to_camel, # キャメルケースのエイリアスを作る
        validate_assignment=True, # 更新時にvalidationを行う設定
    )


