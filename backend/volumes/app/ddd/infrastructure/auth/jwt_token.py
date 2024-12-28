import os
from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError

SECRET_KEY = os.environ["SECRET_KEY"]
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 5

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)

def create_access_token(data: dict[str, Any], expires_delta: timedelta) -> str:
    to_encode = data.copy()
    expire = datetime.now(UTC) + expires_delta
    # if expires_delta:
    #     expire = datetime.now(UTC) + expires_delta
    # else:
    #     expire = datetime.now(UTC) + timedelta(minutes=15) # default 15 min
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_jwt_data(access_token: str) -> dict[str, Any]:
    try:
        payload: dict[str, Any] = jwt.decode(access_token, SECRET_KEY, algorithms=[ALGORITHM])
    except InvalidTokenError:
        raise credentials_exception from None
    return payload