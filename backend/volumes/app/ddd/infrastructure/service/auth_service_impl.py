import bcrypt

from app.ddd.domain.error import UserAuthError
from app.ddd.domain.service import AuthService


class AuthServiceImpl(AuthService):
    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        """hashed_passerdの確認."""
        result = bcrypt.checkpw(plain_password.encode(), hashed_password.encode())
        if result is False:
            raise UserAuthError
        return result

    def create_hashed_password(self, plain_password: str) -> str:
        """hashed_passerdの作成."""
        salt = bcrypt.gensalt(rounds=12, prefix=b"2a")
        return bcrypt.hashpw(plain_password.encode(), salt).decode()
