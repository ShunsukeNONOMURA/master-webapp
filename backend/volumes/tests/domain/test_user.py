from app.ddd.domain import UserId, User, UserReport, UserNotFoundError
import pytest

from pydantic import ValidationError

from app.ddd.infrastructure.database import get_session_context
from app.ddd.infrastructure.uow import UserRepositoryImpl

def test_user_id_immutable():
    # DigitalBuddyIdを利用して不変性確認
    user_id = UserId(root='10')
    with pytest.raises(ValidationError):
        user_id.root = '20'

def test_user():
    """
    - _idが等しいときに同じものとする
    - -idが等しくない場合に別のものとする
    - インスタンスが異なる場合は別物とする
    """
    user_1 = User(
        user_id = 'test',
        user_password = 'test',
        user_name = 'test',
        user_role_code = '00',
    )
    user_2 = User(
        user_id = 'test',
        user_password = 'test',
        user_name = 'test',
        user_role_code = '00',
    )
    user_3 = User(
        user_id = 'test_other',
        user_password = 'test',
        user_name = 'test',
        user_role_code = '00',
    )
    is_user1_eq_user_2 = user_1 == user_2
    assert is_user1_eq_user_2 == True
    is_user1_eq_user_3 = user_1 == user_3
    assert is_user1_eq_user_3 == False
    is_not_user1_eq_user_3 = user_1 != user_3
    assert is_not_user1_eq_user_3 == True
    is_not_user1_eq_1 = user_1 != 1
    assert is_not_user1_eq_1 == True


def test_user_report():
    user_report = UserReport(
        user_report_id = "dammy",
        title = "dammy",
        content = "dammy",
        created_user_id = "dammy",
    )
    is_user_report_eq_user_report =  user_report == user_report
    assert is_user_report_eq_user_report == True


def test_user_update_not_found_false():
    """
    - 存在しないユーザをアップデートしようとする場合のエラー
    - 現状のユースケースでは発生しない
    - Impl経由での実行
    """
    user = User(
        user_id = 'test_update_user',
        user_password = 'test',
        user_name = 'test',
        user_role_code = '00',
    )

    with get_session_context() as session:
        repository = UserRepositoryImpl(session = session)

        with pytest.raises(UserNotFoundError):
            repository.update(user)