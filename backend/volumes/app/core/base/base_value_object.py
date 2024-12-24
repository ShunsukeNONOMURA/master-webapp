from abc import ABCMeta

from pydantic import BaseModel


class BaseValueObject(BaseModel, frozen=True, metaclass=ABCMeta):
    pass

# TODO(nonomura): pydanticとSQLModelの使い分け整理後
# class BaseValueObject(SQLModel, frozen=True, metaclass=ABCMeta):
#     pass
