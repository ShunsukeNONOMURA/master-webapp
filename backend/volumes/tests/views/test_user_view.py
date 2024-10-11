from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_user():
    user_id = "admin"
    response = client.get(
        f"/users/{user_id}",
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == user_id

def test_query_user():
    q = "hoge"
    response = client.get(
        "/query/users",
        params={"q": q},
    )
    assert response.status_code == 200
    # assert response.json() == {'q': q }

def test_user():
    user = {
        "user_id": "test",
        "user_name": "test",
        "user_password": "test",
        "user_role_code": "99",
    }
    user = {
        "userId": "test",
        "userName": "test",
        "userPassword": "test",
        "userRoleCode": "99",
    }
    response = client.post(
        "/users",
        # params={"user": user},
        json=user,
        headers={"Content-Type": "application/json"}
    )
    assert response.status_code == 200

    user_id = user["userId"]
    response = client.get(
        f"/users/{user_id}",
    )
    assert response.status_code == 200
    assert response.json()["user_id"] == user_id

    response = client.delete(
        f"/users/{user_id}",
    )
    assert response.status_code == 200
    # assert response.json()["user_id"] == user_ide

    response = client.get(
        f"/users/{user_id}",
    )
    assert response.status_code == 200
    # assert response.json()["user_id"] == None

