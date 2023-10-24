import asyncio
from sse_starlette.sse import EventSourceResponse

from src.connection.broker import broker  # Import your broker

connected_clients = set()

async def notif_upload():
    return EventSourceResponse(event_generator())

async def event_generator():
    while True:
        try:
            message = await broker.consume_data()
            if message:
                yield {"event": "notification", "data": message}
        except asyncio.CancelledError:
            print("disconnect")
            break
