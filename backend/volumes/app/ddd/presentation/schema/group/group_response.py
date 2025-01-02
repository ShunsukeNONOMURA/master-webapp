

from app.core.base import BaseResponse
from app.ddd.domain.model import Group


class GetGroupResponse(BaseResponse):
    group: Group

class CreateGroupResponse(BaseResponse):
    group: Group

# class PatchGroupResponse(BaseResponse):
#     group_id: str

class DeleteGroupResponse(BaseResponse):
    group_id: str

class QueryGroupResponse(BaseResponse):
    groups: list[Group]
