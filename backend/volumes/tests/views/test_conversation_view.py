from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

def test_websocket():
    with client.websocket_connect("/ws") as websocket:
        websocket.send_text("hoge")

        # data = websocket.receive_json()
        # assert data == {"msg": "Hello WebSocket"}
