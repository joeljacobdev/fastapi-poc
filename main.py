from fastapi import FastAPI
import asyncio
import uvloop

from app.database import init_database
# This need to be done for create_all to work
from app.schemas import *

from app import router as app_router

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = FastAPI()
app.include_router(app_router.router)

@app.on_event("startup")
async def on_startup():
    await init_database()

