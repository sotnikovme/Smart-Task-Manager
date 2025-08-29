import asyncio
from sqla.Models import Base

from sqla.config.config import async_engine


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)

    await async_engine.dispose()
    print("Таблицы успешно созданы!")


if __name__ == "__main__":
    asyncio.run(create_tables())