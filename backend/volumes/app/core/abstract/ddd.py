import json
from abc import ABCMeta, abstractmethod

from pydantic import ConfigDict
from pydantic.alias_generators import to_camel
from sqlmodel import SQLModel


class DDDModel(SQLModel, metaclass=ABCMeta):
    def to_dict(self):
        """
        dict形式に変換する
        """
        return json.loads(self.json())

class ValueObject(DDDModel, metaclass=ABCMeta):
    # class Config:
    #     allow_mutation = False
    model_config = ConfigDict(frozen=True)

class Entity(DDDModel, metaclass=ABCMeta):
    @abstractmethod
    def _id(self):
        """
        IDの取得方法を必ず設計する
        """
        raise NotImplementedError

    # IDで比較するロジック
    def __eq__(self, other: DDDModel)->bool:
        if other is None or type(self) != type(other):
            return False # isinstance(other, Entity)を除去
        return self._id() == other._id()
    def __ne__(self, other: DDDModel)->bool:
        return not self.__eq__(other)

class BaseUsecase(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        """
        Usecaseを実行する抽象メソッド
        """
        raise NotImplementedError

# Request, Response間でケース変換するとき
class BaseRequest(SQLModel):
    """
    リクエストスキーマのベース
    camelCaseの入力をsnake_caseに変換する
    """
    model_config = ConfigDict(
        alias_generator=to_camel
    )
class BaseResponse(SQLModel):
    """
    レスポンススキーマのベース
    snake_caseの入力をcamelCaseに変換する
    """
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel
    )
