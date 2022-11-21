import asyncio
from sqlalchemy.orm import declarative_base, sessionmaker, scoped_session
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession

Base = declarative_base()

POSTGRES_DSN = "postgresql+asyncpg://joel:joeljacob@0.0.0.0:5432/fastapi-sqlalchemy"
engine = create_async_engine(POSTGRES_DSN, echo=True, future=True)
async_session = scoped_session(
    sessionmaker(
            bind=engine, class_=AsyncSession, expire_on_commit=False, future=True
        )
)


async def get_db_session() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        except Exception as e:
            raise
        finally:
            # TODO - only do this if there is any write made
            await session.commit()


async def init_database():
    # TODO if anything needs to be created

    async with engine.begin() as conn:
        # TODO - only to be used for local dev, till migrations are etup
        # await conn.run_sync(Base.metadata.drop_all)
        # await conn.run_sync(Base.metadata.create_all)
        pass
