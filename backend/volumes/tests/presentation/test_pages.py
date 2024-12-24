from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_get_pages_streming():
    response = client.get("/pages/streaming")
    assert response.status_code == 200
