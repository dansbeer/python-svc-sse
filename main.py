from fastapi import FastAPI

import event
from src.config.global_config import app_setting
from src.controller.sse import router as sse_router
from src.controller.produce import router as produce_router

app = FastAPI()

# Add Event shutdown
app.add_event_handler("shutdown", event.shutdown)

# Register Controller
app.include_router(sse_router)
app.include_router(produce_router)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    import uvicorn
    app_port = app_setting.APP_PORT
    uvicorn.run("main:app", host="0.0.0.0", port=int(app_port), reload=True, workers=3)
