# passlibがメンテされていないので使わない
# https://github.com/pyca/bcrypt/issues/684
# https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#install-passlib
import bcrypt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """hashed_passerdの確認."""
    return bcrypt.checkpw(plain_password.encode(), hashed_password.encode())

def create_hashed_password(password: str) -> str:
    """hashed_passerdの作成."""
    salt = bcrypt.gensalt(rounds=12, prefix=b"2a")
    return bcrypt.hashpw(password.encode(), salt).decode()
