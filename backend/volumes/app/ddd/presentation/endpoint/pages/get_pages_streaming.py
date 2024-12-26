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
                body: JSON.stringify({ conversation_id: 'dammy', conversation_content: message, user_id: 'dammy' }),
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
                console.log('v')
                console.log(chunkValue.data)
                console.log(chunkValue.split("\\r\\n"))
                //const parsedData = JSON.parse(chunkValue)

                // console.log(result + (done ? "" : "▊"));
                if (done) {
                    output.innerHTML += '<br>'
                    break;
                }

                // output.innerHTML += chunkValue + '<br>';
                output.innerHTML += chunkValue;
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

@router.get("/pages/streaming", include_in_schema=False)
async def get_page_streaming() -> HTMLResponse:
    """SSE通信用."""
    return HTMLResponse(html_streaming)
