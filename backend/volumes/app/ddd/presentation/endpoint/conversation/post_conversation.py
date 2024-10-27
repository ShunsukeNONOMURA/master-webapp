import asyncio

from sse_starlette.sse import EventSourceResponse

from app.ddd.presentation.endpoint.conversation.router import router
from app.ddd.presentation.schema.conversation import (
    PostConversationRequest,
    PostConversationResponse,
)

## Stream形式：Server-Sent Events ######################################################3
# class StreamRequest(BaseModel):
#     message: str

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

@router.post(
    path="/conversation",
    response_model=PostConversationResponse,
)
async def post_conversation(
    request: PostConversationRequest
) -> EventSourceResponse:
    return EventSourceResponse(
        send_token(request.message)
    )
