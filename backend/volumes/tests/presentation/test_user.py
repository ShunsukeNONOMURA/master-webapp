from fastapi.testclient import TestClient
import pytest

from tests.fixture.db import db

from app.ddd.domain.error import UserNotFoundError, UserDuplicationError

from app.main import app

client = TestClient(app)

# def test_query_user():
#     q = "hoge"
#     response = client.get(
#         "/query/users",
#         params={"q": q},
#     )
#     assert response.status_code == 200
#     # assert response.json() == {'q': q }

def test_get_me(db):
    user_id = "guest"
    response = client.get(
        f"/users/me",
    )
    assert response.status_code == 200
    print('response')
    # print(response.json()["user"]["user_id"])
    assert response.json()["user"]["userId"] == user_id

def test_operate_user(db):
    test_user = {
        "userId": "test",
        "userName": "test",
        "userPassword": "test",
        "userRoleCode": "99",
    }

    # user取得する
    with pytest.raises(UserNotFoundError):
        response = client.get(
            f"/users/{test_user['userId']}",
        )
        # assert response.status_code == 200
        # assert response.json()["user"]["userId"] == user_id

    # user投函する
    response = client.post(
        "/users",
        json=test_user,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200

    # user投函確認する
    response = client.get(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == 200
    # assert response.json()["user"]["userId"] == test_user['userId']

    # user投函をコンフリさせる
    with pytest.raises(UserDuplicationError):
        response = client.post(
            "/users",
            json=test_user,
            headers={"Content-Type": "application/json"}
        )

    # user更新に成功する
    # ValidationError
    patch_user = {
        "userRoleCode": "00", # 存在する
        # "userName": None, # Noneを指定する
        "userName": "new_name",
    }
    response = client.patch(
        f"/users/{test_user['userId']}",
        json=patch_user,
    )
    assert response.status_code == 200
    # assert response.json()["user"]["userId"] == test_user['userId']
    # assert response.json()["userName"] == patch_user['userName'] # 更新されているかチェック

    # user削除する
    response = client.delete(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == 200
    # assert response.json()["user"]["userId"] == test_user['userId']

    # 再度user削除確認する（見つからず404エラーになる）
    with pytest.raises(UserNotFoundError):
        response = client.delete(
            f"/users/{test_user['userId']}",
        )

    # 再度user更新する（見つからず404エラーになる）
    with pytest.raises(UserNotFoundError):
        response = client.patch(
            f"/users/{test_user['userId']}",
            json=patch_user,
        )

    # userにクエリする
    response = client.post(
        "/query/users",
        json={},
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200


