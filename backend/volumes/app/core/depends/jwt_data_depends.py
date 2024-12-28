from datetime import timedelta
from typing import Annotated, Any

from fastapi import Depends, Request

# from fastapi.security import OAuth2PassewordBearer # 余計なものが多いので一旦使わない
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from fastapi.security.utils import get_authorization_scheme_param

from app.ddd.infrastructure.auth import create_access_token, get_jwt_data


class DummyHTTPBearer(HTTPBearer):
    async def __call__(
        self, request: Request
    ) -> HTTPAuthorizationCredentials | None:
        """
        開発用認証.

        認証がないときはguestのインスタントトークン認証を使う
        """
        authorization = request.headers.get("Authorization")
        scheme, credentials = get_authorization_scheme_param(authorization)
        if not (authorization and scheme and credentials):
            access_token_expires = timedelta(minutes=1)
            access_token = create_access_token(
                data={"sub": "guest"},
                expires_delta=access_token_expires
            )
            return HTTPAuthorizationCredentials(scheme="bearer", credentials=access_token)
        return HTTPAuthorizationCredentials(scheme=scheme, credentials=credentials)

# schema = OAuth2PasswordBearer(tokenUrl="token") # 余計なものが多いので一旦使わない
# schema = HTTPBearer() # 本番用
schema = DummyHTTPBearer() # 開発用

def jwt_data_depends(token: Annotated[HTTPAuthorizationCredentials, Depends(schema)]) -> dict[str, Any]:
    return get_jwt_data(token.credentials) # HTTPBearer -> HTTPAuthorizationCredentials(schema, params:str)
