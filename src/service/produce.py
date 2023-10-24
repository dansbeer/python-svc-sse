import traceback

from fastapi.encoders import jsonable_encoder
from src.model.produce import MessageProduce
from src.connection.broker import broker

async def produce_service(produce_schema: MessageProduce):
    try:
        param = jsonable_encoder(produce_schema)
        await broker.publish_message(param)
    except Exception as e:
        traceback.print_exc(e)
        raise Exception("Failed to publish message")
