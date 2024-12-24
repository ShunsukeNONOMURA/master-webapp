from app.ddd.domain.model import UserId
import pytest

from pydantic import ValidationError

def test_user_id_immutable():
    # DigitalBuddyIdを利用して不変性確認
    user_id = UserId(root='10')
    with pytest.raises(ValidationError):
        user_id.root = '20'
