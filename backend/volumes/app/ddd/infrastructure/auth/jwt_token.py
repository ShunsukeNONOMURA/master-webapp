import secrets
from datetime import UTC, datetime, timedelta
from typing import Any

import jwt
from fastapi import HTTPException, status
from jwt.exceptions import InvalidTokenError

# keycloak
# APP_CLIENT_ID = "dev-client"
# APP_CLIENT_SECRET = "example-secret"
APP_REDIRECT_URI = 0
KEYCLOAK_TOKEN_URL = 0

# 32バイトの秘密鍵を生成
SECRET_KEY = secrets.token_hex(32) # 開発用途の毎回作成キー

# SECRET_KEY = os.environ["SECRET_KEY"]
PUBLIC_KEY = "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAw5L4rVichlm99HrLFNlswTgNxW8fnCr3jDS9FWwNjWIYssYdPHstbamePhGgMZ5Xj/4p34dNxxqWKDafnigfcRMn36KdklN2ohMzBIQWA9kMKg3G94YO3x8f39+L09CqTZhNl1LGGL3FhO5LJG+5bUw2yJTQiCPyEupHE3oIaYY5oBxMLTE4I4G35VQ/4in9Y64vTWPO9u1T+QXMDA8boMS6/pvKJDrln0XXBG6ITr7aLUEVrEQD+3tC20DnSTD4DbjZ5g0C7u+AA+0qZ1uKothirILsUgIHUv/s3OvybFc9FvvNuVe1HVggQQuVkJJ1Bj41WXJV82Tmy6JuKdIadQIDAQAB"
public_key = "-----BEGIN PUBLIC KEY-----\n" \
                + PUBLIC_KEY \
                + "\n-----END PUBLIC KEY-----"
# ALGORITHM = "RS256" # 共通鍵方式
ALGORITHM = "HS256" # 秘密鍵方式
# ACCESS_TOKEN_EXPIRE_MINUTES = 5

options = {
    "verify_aud": False
}


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

# def create_access_token_keycloak(username: str, password: str) -> str:
#     params = {
#         'client_id': APP_CLIENT_ID,
#         'client_secret': APP_CLIENT_SECRET,
#         'grant_type': 'password',
#         'username': username,
#         'password': password,
#     }
#     import requests, json
#     from pprint import pprint
#     import ast
#     x = requests.post(KEYCLOAK_TOKEN_URL, params, verify=False).content.decode('utf-8')
#     pprint(json.loads(x))
#     token_response = ast.literal_eval(x)
#     pprint(token_response['id_token'])
#     return token_response

def get_jwt_data(
        access_token: str
    ) -> dict[str, Any]:
    print(access_token)
    try:
        # 公開鍵
        # payload: dict[str, Any] = jwt.decode(
        #     jwt=access_token,
        #     key=public_key,
        #     algorithms=[ALGORITHM],

        #     # options=options,
        #     # audience="dev-client",
        #     # issuer="http://localhost:38080/auth/realms/dev-realm"
        # )
        # 共通鍵
        payload: dict[str, Any] = jwt.decode(
            jwt=access_token,
            key=SECRET_KEY,
            algorithms=["HS256"],
            # options=options,
            # audience="dev-client",
            # issuer="http://localhost:38080/auth/realms/dev-realm"
        )
        print("payload")
        print(payload)
    except InvalidTokenError as e:
        print("error")
        print(e)
        raise credentials_exception from e
    return payload
