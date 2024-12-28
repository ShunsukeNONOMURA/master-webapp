from fastapi import status
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

    - tokenなしの場合認証できていない
    - TODO(nonomura): tokenありの場合認証できている

    TODO(nonomura): jwt関連設計後
    """
    user_id = "guest"
    response = client.get(
        f"/users/me",
    )
    assert response.status_code == status.HTTP_401_UNAUTHORIZED



    # print('response')
    # # print(response.json()["user"]["user_id"])
    # assert response.json()["user"]["userId"] == user_id

def test_operate_user(db):
    """
    ユーザ操作のテスト
    - 作成に関する操作
        - テストユーザを作成する
        - 再度テストユーザ作成してコンフリ失敗させる
        - ユーザレポートを追加する

    - 更新に関する操作
        - ユーザ更新を失敗させる（無効なパラメータ）
        - ユーザを更新する
        - 再度ユーザを更新して失敗させる（楽観的ロックの確認）

    - 削除に関する操作
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

    ### 作成のテスト ########################################################
    # テストユーザを作成する
    response = client.post(
        "/users",
        json=test_user,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == status.HTTP_200_OK 

    # user投函確認する
    response = client.get(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == status.HTTP_200_OK 
    # assert response.json()["user"]["userId"] == test_user['userId']
    updated_at = response.json()["user"]["updatedAt"]

    # user投函をコンフリさせる
    response = client.post(
        "/users",
        json=test_user,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == status.HTTP_409_CONFLICT

    # レポートを2回記述する
    response = client.post(
        f"/users/{test_user['userId']}/user-reports",
        json={
            "title": "title",
            "content": "content"
        },
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
    response = client.post(
        f"/users/{test_user['userId']}/user-reports",
        json={
            "title": "title",
            "content": "content"
        },
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200


    ### 更新のテスト ########################################################
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
    assert response.status_code == status.HTTP_200_OK 
    # assert response.json()["user"]["userId"] == test_user['userId']
    # assert response.json()["user"]["userName"] == patch_user['userName'] # 更新されているかチェック

    # テストユーザ更新に失敗する（古い日付で更新に失敗する(楽観的ロックの確認)）
    response = client.patch(
        f"/users/{test_user['userId']}",
        json=patch_user,
    )
    assert response.status_code == status.HTTP_409_CONFLICT 

    ### 削除のテスト ########################################################
    # user削除する
    response = client.delete(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == status.HTTP_200_OK 
    
    # 削除されたテストユーザに対して各操作(取得/更新/削除)が失敗する
    response = client.get(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND 
    response = client.patch(
        f"/users/{test_user['userId']}",
        json=patch_user,
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND 
    response = client.delete(
        f"/users/{test_user['userId']}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND 
    
def test_query_user(db):
    """
    ユーザクエリのテスト
    - ユーザのクエリを行う
    """
    # userにクエリする
    response = client.post(
        "/query/users",
        json={
            "filters": {
                "userId": "guest"
            }
        },
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200
