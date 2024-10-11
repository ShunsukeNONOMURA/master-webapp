import json
from abc import ABCMeta, abstractmethod

from pydantic import BaseModel, ConfigDict


class DDDModel(BaseModel, metaclass=ABCMeta):
    def to_json(self):
        return json.loads(self.json())

class ValueObject(DDDModel, metaclass=ABCMeta):
    # class Config:
    #     allow_mutation = False
    model_config = ConfigDict(frozen=True)

class Entity(DDDModel, metaclass=ABCMeta):
    @abstractmethod
    def _id(self): # IDの取得方法を必ず設計する
        raise NotImplementedError

    # IDで比較するロジック
    def __eq__(self, other: DDDModel)->bool:
        if other is None or type(self) != type(other):
            return False # isinstance(other, Entity)を除去
        return self._id() == other._id()
    def __ne__(self, other: DDDModel)->bool:
        return not self.__eq__(other)
