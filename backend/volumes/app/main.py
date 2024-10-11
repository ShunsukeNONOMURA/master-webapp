from fastapi import FastAPI
from gradio import mount_gradio_app
from mangum import Mangum

from .core.middleware import AuthMiddleware, LoggingMiddleware
from .ddd import *

app = FastAPI()

# # middlewareは逆順にコールされる
# app.add_middleware(AuthMiddleware)
# app.add_middleware(LoggingMiddleware)

# カスタムHTTPミドルウェア
from fastapi import FastAPI, WebSocket
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.middleware.base import RequestResponseEndpoint
class CustomMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: RequestResponseEndpoint) -> Response:
        print('customr')
        # WebSocket接続への特別な対応が必要な場合
        if "websocket" in request.url.path:
            # WebSocketのミドルウェアに関連する処理をここで行います
            print("WebSocket connection processing")
        # その他のHTTPリクエストに対する処理
        response = await call_next(request)
        return response
# app.add_middleware(CustomMiddleware)

# ws, http両方
class ASGIMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        print('asgi')
        print(scope["type"])
        response = await self.app(scope, receive, send)
        print(response)
# app.add_middleware(ASGIMiddleware)


from fastapi import APIRouter, FastAPI, Request, Response
from fastapi.routing import APIRoute
from typing import Callable
import time
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

main_router = APIRouter(route_class=TimedRoute)
main_router.include_router(health_view.router)
main_router.include_router(user_view.router)
main_router.include_router(conversation_view.router)

app.include_router(main_router)

# gradio
import gradio as gr
import requests as r

# API_HOST = "http://localhost:8000/api/v1"
API_HOST = "http://localhost:8000"

def predict(text: str, request: gr.Request):
    url = f"{API_HOST}/users/{text}"
    try:
        data = r.get(url).json()
    except Exception:
        data = {
            "msg": "false"
        }
    if data is None:
        data = {
            "msg": "none"
        }
    # print(data)
    return data
def greet(message: str):
    url = f"{API_HOST}/conversation"
    data = r.post(
        url,
        json={"message":message},
        headers={"Content-Type": "application/json"}
    ).json()
    return data["message"]

# import random
# def random_response(message, history):
#     return random.choice(["Yes", "No"])
def slow_echo(message: str, history: list):
    url = f"{API_HOST}/streaming"
    response = r.post(
        url,
        json={"message":message},
        headers={"Content-Type": "application/json"},
        stream=True
    )
    data = ""
    for chunk in response.iter_content():
        data += chunk.decode("utf-8")
        # data += chunk
        yield data
        # try:
        #     j = json.loads(chunk.decode()[6:])
        #     content = j['choices'][0]['delta'].get('content')
        #     if content:
        #         response_text += content
        #         yield content
        # except:
        #     pass
    # for i in range(len(message)):
    #     time.sleep(0.3)
    #     yield "You typed: " + message[: i+1]

def fetch_stream(message: str):
    url = f"{API_HOST}/streaming"
    response = r.post(
        url,
        json={"message":message},
        headers={"Content-Type": "application/json"},
        stream=True
    )
    data = ""
    for chunk in response.iter_content():
        data += chunk.decode("utf-8")
        if len(data.splitlines()) > 10:  # 例えば、10行取得したら終了
            break
    return data

blocks = gr.Interface(fn=greet, inputs="textbox", outputs="textbox")

# with gr.Blocks() as blocks:
#     # with gr.Row():
#     #     # gr.Button("ダッシュボード", link="/dashboard")
#     #     # url = f"{API_HOST}/users/admin"
#     #     # url = "http://127.0.0.1/users/admin"
#     #     # data = r.get(url).json()
#     #     # print(data)
#     gr.Interface(predict, "text", "json")
#     gr.Interface(greet, "text", "text")
#     gr.ChatInterface(slow_echo, examples=["streaming"])
#     gr.Interface(fn=fetch_stream, inputs=["text"], outputs="text")

#     # Gradioのインターフェイスを作成
#     def interact_with_server(message):
#         url = "ws://localhost:8000/ws"
#         ws = websocket.WebSocket()
#         ws.connect(url)
#         ws.send(message)
#         response = ws.recv()
#         ws.close()
#         return f"Response from server: {response}"

#     # async def stream_from_server(url, port):
#     #     uri = "ws://localhost:8000/ws"
#     #     ws = websocket.WebSocket()
#     #     ws.connect(uri)
#     #     async with ws as websocket:
#     #         await websocket.send(message)
#     #         while True:
#     #             message = await websocket.recv()
#     #             yield message

#     # Gradioインターフェイスの定義
#     ws_url_input = gr.Textbox(lines=1, label="WebSocket Server URL")
#     message_input = gr.Textbox(lines=2, label="Message to Send")
#     result_output = gr.Textbox(label="Server Response")

#     interface = gr.Interface(
#         fn=interact_with_server,
#         inputs=[message_input],
#         outputs=result_output,
#         title="WebSocket Client"
#     )

app = mount_gradio_app(app, blocks, path="/top")

# Mangum
handler = Mangum(app)

# invoke debug 用
# def handler_debug(event, context):
#     print(event)
#     print(context)
#     # if event.get("resource") != '/{proxy+}':
#     #     # proxy+ 由来ではない場合何もしない
#     #     return

#     # default
#     asgi_handler = Mangum(app)
#     response = asgi_handler(event, context) # Call the instance with the event arguments

#     return response
# handler = handler_debug

# export openapi
HTML_TEMPLATE = """<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <title>My Project - ReDoc</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="shortcut icon" href="https://fastapi.tiangolo.com/img/favicon.png">
    <style>
        body {
            margin: 0;
            padding: 0;
        }
    </style>
    <style data-styled="" data-styled-version="4.4.1"></style>
</head>
<body>
    <div id="redoc-container"></div>
    <script src="https://cdn.jsdelivr.net/npm/redoc/bundles/redoc.standalone.js"> </script>
    <script>
        var spec = %s;
        Redoc.init(spec, {}, document.getElementById("redoc-container"));
    </script>
</body>
</html>
"""
path_output_html = '/root/docs/backend/api.html'
with open(path_output_html, "w") as fd:
    print(HTML_TEMPLATE % json.dumps(app.openapi()), file=fd)
path_output_openapi_json = '/root/docs/backend/openapi.json'
with open(path_output_openapi_json, "w") as f:
    api_spec = app.openapi()
    f.write(json.dumps(api_spec))
