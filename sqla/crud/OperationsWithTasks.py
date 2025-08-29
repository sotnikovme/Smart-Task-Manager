from sqla.config import async_session

from sqla.Models import Task

async def create_task(
        title: str,
        body: str,
        color: str,
        owner: int
):
    async with async_session() as session:
        task = Task(title=title, body=body, color=color, owner=owner)
        session.add(task)
        await session.commit()