import asyncio
import random
from sqlalchemy import text
from fastapi import APIRouter, Depends
from app.database import get_db_session


router = APIRouter(prefix="/connections")


@router.get("/fetch")
async def fetch_data(session=Depends(get_db_session)):
    result = await session.execute(
        text(f"SELECT id from app__colleges where id = {random.randint(1, 10)}")
    )
    result.scalar()
    # await asyncio.sleep(3)
    result = await session.execute(
        text(f"SELECT id from app__course where id = {random.randint(1, 200)}")
    )
    return result.scalar()
