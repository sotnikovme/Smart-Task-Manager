from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import async_sessionmaker

from sqla.config import engine, async_engine

session = sessionmaker(
    bind=engine,
)

async_session = async_sessionmaker(
    bind=async_engine
)