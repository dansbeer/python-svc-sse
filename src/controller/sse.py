from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse
from src.connection.broker import broker

router = APIRouter()

@router.get("/notif-upload")
async def notif_upload_endpoint(request: Request):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                print("disconnected")
                break
            message = await broker.consume_data()
            if message:
                yield {"event": "notification", "data": message}
    return EventSourceResponse(event_generator())
