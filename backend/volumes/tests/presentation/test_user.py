from fastapi.testclient import TestClient
import pytest

from pydantic import ValidationError

from tests.fixture.db import db

from app.ddd.domain.error import UserNotFoundError, UserDuplicationError, UserUpdateConflictError

from app.main import app

client = TestClient(app)

def test_get_me(db):
    """
    meの取得を行う

    TODO(nonomura): jwt関連設計後
    """
    user_id = "guest"
    response = client.get(
        f"/users/me",
    )
    assert response.status_code == 200
    print('response')
    # print(response.json()["user"]["user_id"])
    assert response.json()["user"]["userId"] == user_id

def test_operate_user(db):
    """
    ユーザ操作のテスト
    - テストユーザを作成する
    - 再度テストユーザ作成して失敗させる
    - ユーザ更新を失敗させる（無効なパラメータ）
    - ユーザを更新する
    - 再度ユーザを更新して失敗させる（楽観的ロックの確認）
    - ユーザを削除する
    - 再度ユーザを削除しようとして失敗させる
    - 存在しないテストユーザに対して取得/削除/更新をしようとして失敗させる
    """
    test_user = {
        "userId": "test",
        "userName": "test",
        "userPassword": "test",
        "userRoleCode": "99",
    }

    # テストユーザを作成する
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
    updated_at = response.json()["user"]["updatedAt"]

    # user投函をコンフリさせる
    with pytest.raises(UserDuplicationError):
        response = client.post(
            "/users",
            json=test_user,
            headers={"Content-Type": "application/json"}
        )

    # テストユーザ更新に失敗する（無効なデータ）
    patch_false_user = {
        "updatedAt": updated_at,
        "userRoleCode": "999", # 存在しない
        "userName": None, # Noneを指定する
    }
    with pytest.raises(ValidationError):
        response = client.patch(
            f"/users/{test_user['userId']}",
            json=patch_false_user,
        )

    # テストユーザ更新に成功する
    patch_user = {
        "updatedAt": updated_at,
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
    # assert response.json()["user"]["userName"] == patch_user['userName'] # 更新されているかチェック

    # テストユーザ更新に失敗する（古い日付で更新に失敗する(楽観的ロックの確認)）
    with pytest.raises(UserUpdateConflictError):
        response = client.patch(
            f"/users/{test_user['userId']}",
            json=patch_user,
        )

    # user削除する
    response = client.delete(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == 200
    
    # 削除されたテストユーザに対して各操作が失敗する
    with pytest.raises(UserNotFoundError): # 取得
        response = client.get(
            f"/users/{test_user['userId']}",
        )
    with pytest.raises(UserNotFoundError): # 更新
        response = client.patch(
            f"/users/{test_user['userId']}",
            json=patch_user,
        )
    with pytest.raises(UserNotFoundError): # 削除
        response = client.delete(
            f"/users/{test_user['userId']}",
        )
    
def test_query_user(db):
    """
    ユーザクエリのテスト
    - ユーザのクエリを行う
    """
    # userにクエリする
    response = client.post(
        "/query/users",
        json={},
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200


