from app.ddd.domain import GroupId, Group, GroupNotFoundError
import pytest

from pydantic import ValidationError

from app.ddd.infrastructure.database import get_session_context
from app.ddd.infrastructure.uow import GroupRepositoryImpl

def test_group_id_immutable():
    # DigitalBuddyIdを利用して不変性確認
    group_id = GroupId(root='10')
    with pytest.raises(ValidationError):
        group_id.root = '20'

def test_group():
    """
    - _idが等しいときに同じものとする
    - -idが等しくない場合に別のものとする
    - インスタンスが異なる場合は別物とする
    """
    group_1 = Group(
        group_responsible_user_id = 'admin',
        group_name = 'test',
    )
    group_2 = Group(
        group_responsible_user_id = 'admin',
        group_name = 'test',
    )
    is_group1_eq_group_1 = group_1 == group_1
    assert is_group1_eq_group_1 == True
    is_group1_eq_group_2 = group_1 == group_2
    assert is_group1_eq_group_2 == False
    is_not_group1_eq_group_2 = group_1 != group_2
    assert is_not_group1_eq_group_2 == True
    is_not_group1_eq_1 = group_1 != 1
    assert is_not_group1_eq_1 == True


# def test_group_update_not_found_false():
#     """
#     - 存在しないユーザをアップデートしようとする場合のエラー
#     - 現状のユースケースでは発生しない
#     - Impl経由での実行
#     """
#     group = Group(
#         group_id = 'test_update_group',
#         group_password = 'test',
#         group_name = 'test',
#         group_role_code = '00',
#     )

#     with get_session_context() as session:
#         repository = GroupRepositoryImpl(session = session)

#         with pytest.raises(GroupNotFoundError):
#             repository.update(group)