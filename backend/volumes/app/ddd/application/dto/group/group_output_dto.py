

from app.core.base import BaseOutputDTO
from app.ddd.domain import Group


class GetGroupOutputDTO(BaseOutputDTO):
    group: Group

class CreateGroupOutputDTO(BaseOutputDTO):
    group: Group

class PatchGroupOutputDTO(BaseOutputDTO):
    group: Group

class DeleteGroupOutputDTO(BaseOutputDTO):
    group_id: str

class QueryGroupOutputDTO(BaseOutputDTO):
    groups: list[Group]
