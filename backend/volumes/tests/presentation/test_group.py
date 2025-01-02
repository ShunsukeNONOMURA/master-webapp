from fastapi import status
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_op_group():
    """
    Group操作のTest
    - 作成に関する操作
        - TestGroupを作成する
        # - 再度TestGroup作成してコンフリ失敗させる(同じ名前のグループを許容しない)
        # - Groupにメンバーを追加する

    # - 更新に関する操作
    #     - Group更新を失敗させる（無効なパラメータ）
    #     - Groupを更新する
    #     - 再度Groupを更新して失敗させる（楽観的ロックの確認）

    - 削除に関する操作
        - Groupを削除する
        - 再度Groupを削除しようとして失敗させる
        - 存在しないTestGroupに対して操作失敗させる
    """
    test_group_init = {
        "groupName": "test",
    }

    ### 作成のTest ########################################################
    # TestGroupを作成する
    response = client.post(
        "/groups",
        json=test_group_init,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == status.HTTP_200_OK 
    test_group = response.json()["group"]

    # group投函確認する
    response = client.get(
        f"/groups/{test_group['groupId']}",
    )
    assert response.status_code == status.HTTP_200_OK 
    assert response.json()["group"]["groupId"] == test_group['groupId']

    # # group投函をコンフリさせる
    # response = client.post(
    #     "/groups",
    #     json=test_group,
    #     headers={"Content-Type": "application/json"}
    # )
    # assert response.status_code == status.HTTP_409_CONFLICT

    # # レポートを2回記述する
    # response = client.post(
    #     f"/groups/{test_group['groupId']}/group-reports",
    #     json={
    #         "title": "title",
    #         "content": "content"
    #     },
    #     headers={"Content-Type": "application/json"}
    # )
    # assert response.status_code == 200
    # response = client.post(
    #     f"/groups/{test_group['groupId']}/group-reports",
    #     json={
    #         "title": "title",
    #         "content": "content"
    #     },
    #     headers={"Content-Type": "application/json"}
    # )
    # assert response.status_code == 200


    ### 更新のTest ########################################################
    # # TestGroup更新に失敗する（無効なデータ）
    # patch_false_group = {
    #     "updatedAt": updated_at,
    #     "groupRoleCode": "999", # 存在しない
    #     "groupName": None, # Noneを指定する
    # }
    # with pytest.raises(ValidationError):
    #     response = client.patch(
    #         f"/groups/{test_group['groupId']}",
    #         json=patch_false_group,
    #     )

    # # TestGroup更新に成功する
    # patch_group = {
    #     "updatedAt": updated_at,
    #     "groupRoleCode": "00", # 存在する
    #     # "groupName": None, # Noneを指定する
    #     "groupName": "new_name",
    # }
    # response = client.patch(
    #     f"/groups/{test_group['groupId']}",
    #     json=patch_group,
    # )
    # assert response.status_code == status.HTTP_200_OK 
    # # assert response.json()["group"]["groupId"] == test_group['groupId']
    # # assert response.json()["group"]["groupName"] == patch_group['groupName'] # 更新されているかチェック

    # # TestGroup更新に失敗する（古い日付で更新に失敗する(楽観的ロックの確認)）
    # response = client.patch(
    #     f"/groups/{test_group['groupId']}",
    #     json=patch_group,
    # )
    # assert response.status_code == status.HTTP_409_CONFLICT 

    ### 削除のTest ########################################################
    # group削除する
    response = client.delete(
        f"/groups/{test_group['groupId']}",
    )
    assert response.status_code == status.HTTP_200_OK 
    
    # 削除されたTestGroupに対して各操作(取得/更新/削除)が失敗する
    response = client.get(
        f"/groups/{test_group['groupId']}",
    )
    # assert response.status_code == status.HTTP_404_NOT_FOUND
    # response = client.patch(
    #     f"/groups/{test_group['groupId']}",
    #     json=patch_group,
    # )
    # assert response.status_code == status.HTTP_404_NOT_FOUND 
    response = client.delete(
        f"/groups/{test_group['groupId']}",
    )
    assert response.status_code == status.HTTP_404_NOT_FOUND 