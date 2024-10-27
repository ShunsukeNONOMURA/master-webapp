import asyncio
import json

from fastapi import (
    APIRouter,
    WebSocket,
    WebSocketDisconnect,
)

router = APIRouter()

async def send_token(query: str):
    message_id = "dammy"
    message = ""
    yield {
        "event": "delta",
        "data": "start",
    }
    for chank in query:
        message += chank
        json_data = {
            "message_id": message_id,
            "message": chank,
            # "message": message,
        }
        # response_text = json.dumps(json_data)
        # yield f"data:{response_text}\n\n"
        yield {
            "event": "delta",
            "data": json_data,
        }
        await asyncio.sleep(0.5)
    yield {
        "data": "[DONE]"
    }

# ws ######################################################3
class ConnectionManager:
    def __init__(self) -> None:
        self.active_connections: list[WebSocket] = [] # websocket登録状態

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    username = "dammy"
    try:
        while True:
            data = await websocket.receive_text()
            # message_id = str(uuid.uuid4())
            async for message_token in send_token(data):
                # json_data = {
                #     "message_id": message_id,
                #     "message_token": message_token,
                # }
                response_text = json.dumps(message_token)
                # await manager.send_personal_message(response_text, websocket)
                await manager.broadcast(response_text) # 全体通知
            # await websocket.close()
            manager.disconnect(websocket)
            await websocket.close()
            break
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{username} left the chat") # 全体通知
