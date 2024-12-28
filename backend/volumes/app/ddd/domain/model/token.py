from app.core.base import BaseValueObject


class Token(BaseValueObject):
    access_token: str
    token_type: str
