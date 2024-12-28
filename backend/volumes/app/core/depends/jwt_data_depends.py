from typing import Annotated, Any

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

from app.ddd.infrastructure.auth import get_jwt_data

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
def jwt_data_depends(token: Annotated[str, Depends(oauth2_scheme)]) -> dict[str, Any]:
    return get_jwt_data(token)
