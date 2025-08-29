import asyncio

from sqlalchemy import select, update
from sqla.config import async_session, async_engine
from sqla.Models import User
from sqla.Models import Base
from sqlalchemy import MetaData


async def create_user(
        name: str,
        email: str,
        password: str
):
    async with async_session() as session:

        user = User(name=name, email=email, password=password)
        session.add(user)
        await session.commit()


"""
need revision
"""
async def update_user(
        user_id: int,
        **kwargs
):
    async with async_session() as session:
        stmt = update(User).where(User.id == user_id).values(**kwargs)
        session.add(stmt)
        session.commit(stmt)


async def find_user_by_id(
        user_id: int
):
    async with async_session() as conn:
        stmt = select(User.name, User.email, User.reg_data).where(User.id == user_id)
        res = await conn.execute(stmt)
        result = res.all()


async def main():
    pass
   # async with async_engine.begin() as conn:
   #      await conn.run_sync(Base.metadata.drop_all)
#         await conn.run_sync(Base.metadata.create_all)
#     await create_user(name="Mikle", email="mikle@ya.ru", password="21eFNj23nF")
#     await find_user_by_id(user_id=1)

if __name__ == '__main__':
    asyncio.run(main())