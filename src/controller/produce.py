import traceback

from fastapi import APIRouter, Body
from src.service.produce import produce_service
from src.model.produce import MessageProduce

router = APIRouter()

@router.post("/produce")
async def produce_endpoint(param: MessageProduce = Body(...)):
    result = await produce_service(param)
    return result
