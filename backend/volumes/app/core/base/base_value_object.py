from abc import ABCMeta

from pydantic import BaseModel
from sqlmodel._compat import SQLModelConfig


class BaseValueObject(BaseModel, metaclass=ABCMeta):
    model_config = SQLModelConfig(
        frozen=True,
    )
