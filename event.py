from src.connection.broker import broker

async def shutdown():
    print("closing database connection")
    await broker.close_connection()
