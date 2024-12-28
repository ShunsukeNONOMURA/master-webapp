import os
from datetime import timedelta

from app.ddd.domain.factory import TokenFactory
from app.ddd.domain.model import Token, User
from app.ddd.infrastructure.auth import create_access_token


class TokenFactoryImpl(TokenFactory):
    def __init__(self, expires_minites: int = 1) -> None:
        self.expires_minites = expires_minites
    def create(self, user: User) -> Token:
        return Token(
            access_token = create_access_token(
                expires_delta=timedelta(self.expires_minites),
                data={"sub": user.user_id},
            ),
            token_type =os.environ["TOKEN_TYPE"]
        )
