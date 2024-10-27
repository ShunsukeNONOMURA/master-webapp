from fastapi.responses import HTMLResponse

from app.ddd.presentation.endpoint.pages.router import router

"""
簡易フロントエンド
"""

html_streaming="""
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
            const response = await fetch(`http://localhost:8000/conversation`, {
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

@router.get("/pages/streamimg")
async def get_page_stream():
    return HTMLResponse(html_streaming)

@router.get("/pages/ws")
async def get_page_ws():
    return HTMLResponse(html_ws)
