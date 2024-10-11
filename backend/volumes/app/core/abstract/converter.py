from pydantic import BaseModel, ConfigDict, Field, RootModel, SecretStr
from abc import ABCMeta, abstractmethod

from pydantic.alias_generators import to_camel

# Request, Response間でケース変換するとき
class BaseRequest(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel
    )
class BaseResponse(BaseModel):
    model_config = ConfigDict(
        populate_by_name=True,
        alias_generator=to_camel
    )
class BaseSchema(BaseModel):
    model_config = ConfigDict(
        alias_generator=to_camel,
        populate_by_name=True,
        from_attributes=True,
    )