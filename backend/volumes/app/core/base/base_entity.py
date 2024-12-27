from abc import ABCMeta, abstractmethod

from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel
from sqlmodel._compat import SQLModelConfig


class BaseEntity(SQLModel, metaclass=ABCMeta):
    model_config = SQLModelConfig(
        populate_by_name=True, # 名前とエイリアスの入力の両方を許容する
        alias_generator=to_camel, # キャメルケースのエイリアスを作る
        validate_assignment=True, # 更新時にvalidationを行う設定
    )

    @abstractmethod
    def _id(self) -> str | int:
        """IDの取得方法を必ず設計する."""
        raise NotImplementedError

    # IDで比較するロジック
    def __eq__(self, other: object)->bool:
        if not isinstance(other, self.__class__):  # isinstance を使用
            return False
        return self._id() == other._id()
    def __ne__(self, other: object)->bool:
        return not self.__eq__(other)


