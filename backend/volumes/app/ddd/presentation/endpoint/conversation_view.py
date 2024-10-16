import asyncio
import json
import time
import uuid
from typing import Callable

from fastapi import (
    APIRouter,
    Request,
    Response,
    WebSocket,
    WebSocketDisconnect,
)
from fastapi.responses import HTMLResponse
from fastapi.routing import APIRoute
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse


class TimedRoute(APIRoute):
    def get_route_handler(self) -> Callable:
        original_route_handler = super().get_route_handler()

        async def custom_route_handler(request: Request) -> Response:
            before = time.time()
            response: Response = await original_route_handler(request)
            duration = time.time() - before
            response.headers["X-Response-Time"] = str(duration)
            print(f"route duration: {duration}")
            print(f"route response: {response}")
            print(f"route response headers: {response.headers}")
            return response

        return custom_route_handler

router = APIRouter(route_class=TimedRoute)



class RequestConversation(BaseModel):
    message: str

@router.post("/conversation", tags=["conversation"])
def conversation(request: RequestConversation):
    print(request.message)
    return {"message": request.message + "!"}

## Server-Sent Events ######################################################3
class StreamRequest(BaseModel):
    message: str

async def send_token(query: str):
    message_id = str(uuid.uuid4())
    message = ""
    for chank in query:
        message += chank
        json_data = {
            "message_id": message_id,
            "message": message,
        }
        # response_text = json.dumps(json_data)
        # yield f"data:{response_text}\n\n"
        yield {"data": json_data}
        await asyncio.sleep(0.5)
    yield {"data": "[DONE]"}

# async def send_token_openai(query: str):
#     response = openai.ChatCompletion.create(
#         model="gpt-3.5-turbo-0613",
#         messages=[
#             {'role': 'user', 'content': query}
#         ],
#         stream=True
#     )
#     for chunk in response:
#         chunk_message = chunk['choices'][0]['delta'].get('content', '')
#         yield chunk_message

@router.post("/streaming")
async def streaming_endpoint(request: StreamRequest) -> EventSourceResponse:
    return EventSourceResponse(
        send_token(request.message),
    )

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


"""
以下、簡易フロントエンド
"""

html="""
<html>
  <head>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        const output = document.getElementById("output");
        const input = document.getElementById("input");
        const button = document.getElementById("send_button");

        // Send message to WebSocket server
        button.addEventListener("click", async () => {
            const message = input.value;
            input.value = '';
            const response = await fetch(`http://localhost:8000/streaming`, {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: message }),
            });
            const data = response.body;
            const reader = data.getReader();
            const decoder = new TextDecoder();

            let done = false;
            while (true) {
                const { value, done: doneReading } = await reader.read();
                done = doneReading;
                // JSON.parse(value);
                const chunkValue = decoder.decode(value);

                // result += chunkValue;
                output.innerHTML += chunkValue;
                // console.log(result + (done ? "" : "▊"));
                if (done) {
                    output.innerHTML += '<br>'
                    break;
                }
            }
        });
      });
    </script>
  </head>
  <body>
    <h1>Streaming Chatbot</h1>
    <input
      id="input"
      type="text"
      placeholder="Enter message"
      style="width: 500px; height: 100px"
    />
    <button id="send_button">send_button</button>
    <div id="output"></div>
  </body>
</html>
"""


# ws
html_ws="""
<html>
  <head>
    <script>
      document.addEventListener("DOMContentLoaded", () => {
        const output = document.getElementById("output");
        const input = document.getElementById("input");
        const button = document.getElementById("send_button");

        let socket;

        // Send message to WebSocket server
        button.addEventListener("click", () => {
          if (!socket || socket.readyState !== WebSocket.OPEN) {
            socket = new WebSocket("ws://localhost:8000/ws");

            socket.addEventListener("open", (event) => {
              output.innerHTML += "<p>Connected to WebSocket server.</p>";
              button.textContent = "Send";
            });

            socket.addEventListener("message", (event) => {
              const data = JSON.parse(event.data);
              console.log(data)
              output.innerHTML += JSON.stringify(data)
              //output.innerHTML += event.data;
            });

            socket.addEventListener("close", (event) => {
              output.innerHTML += "<p>Disconnected from WebSocket server.</p>";
              button.textContent = "Connect";
            });
          } else {
            const message = input.value;
            if (message) {
              // console.log(message)
              socket.send(message);
              input.value = "";
            }
          }
        });

        // Close WebSocket connection on window close
        window.addEventListener("beforeunload", () => {
          socket.close();
          console.log('close')
        });
      });
    </script>
  </head>
  <body>
    <h1>WS Chatbot</h1>
    <input
      id="input"
      type="text"
      placeholder="Enter message"
      style="width: 500px; height: 100px"
    />
    <button id="send_button">Connect</button>
    <div id="output"></div>
  </body>
</html>
"""

@router.get("/page/stream")
async def get_page_stream():
    return HTMLResponse(html)

@router.get("/page/ws")
async def get_page_ws():
    return HTMLResponse(html_ws)
