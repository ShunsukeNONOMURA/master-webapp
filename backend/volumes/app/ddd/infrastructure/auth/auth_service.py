from passlib.context import CryptContext


class AuthService:
    def __init__(self) -> None:
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def verify_password(self, plain_password: str, hashed_password: str) -> bool:
        return bool(self.pwd_context.verify(plain_password, hashed_password))

    def get_password_hash(self, password: str) -> str:
        return str(self.pwd_context.hash(password))

# def authenticate_user(fake_db, username: str, password: str):
#     user = get_user(fake_db, username)
#     if not user:
#         return False
#     if not verify_password(password, user.hashed_password):
#         return False
#     return user
