import asyncio
import uvloop
from fastapi import FastAPI
from sqladmin import Admin

from app.database import init_database, engine
from app.admin import app_views

# This need to be done for create_all to work
from app.schemas import *

from app import router as app_router
from app.connections import router as connection_router

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

app = FastAPI()
app.include_router(app_router.router)
app.include_router(connection_router.router)
admin = Admin(app, engine)
for view in app_views:
    admin.add_view(view)


@app.on_event("startup")
async def on_startup():
    await init_database()
