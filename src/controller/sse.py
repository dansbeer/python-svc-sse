from collections import defaultdict

from fastapi import APIRouter, Request
from sse_starlette.sse import EventSourceResponse

from src.connection.broker import broker

router = APIRouter()

clients = defaultdict(list)
@router.get("/notif-upload")
async def notif_upload_endpoint(request: Request, id: str):
    async def event_generator():
        while True:
            if await request.is_disconnected():
                break
            message = await broker.consume_data()
            if message:
                if id in clients and len(clients[id]) > 0:
                    yield {"event": "notification", "data": message}
    # Tambahkan koneksi klien ke "clients" saat klien terhubung
    clients[id].append(event_generator())
    print(clients)

    # Menggunakan EventSourceResponse untuk mengirim data ke klien
    return EventSourceResponse(event_generator())
