from fastapi import Request
from sse_starlette.sse import EventSourceResponse
from typing import Callable
from src.connection.broker import broker  # Import your broker

connected_clients = set()

async def notif_upload(request: Request, filter_func: Callable, user_id: str):
    while True:
        if await request.is_disconnected():
            break
        message = await broker.consume_data()
        if message:
            if filter_func(user_id, message):
                yield {"event": "notification", "data": message}


# async def event_generator():
#     while True:
#         if await request.is_disconnected():
#             break
#         message = await broker.consume_data()
#         if message:
#             yield {"event": "notification", "data": message}
