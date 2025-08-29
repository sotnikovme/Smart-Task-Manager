from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine

# DB_URL = f"sqlite:///{db_file_path}"
DB_URL = "postgresql+pg8000://user:example@localhost:5432/blog"
DB_URL_ASYNC = "postgresql+asyncpg://user:example@localhost:5432/blog"
# DB_ECHO = False
DB_ECHO = True

engine = create_engine(
    url=DB_URL,
    echo=DB_ECHO,
)

async_engine = create_async_engine(
    url=DB_URL_ASYNC,
    echo=DB_ECHO,
)