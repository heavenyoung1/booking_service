from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from models.base import Base

from typing import AsyncGenerator

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/testpostgreserver"

# Настройка асинхронного движка
engine = create_async_engine(DATABASE_URL)

# Создание асинхронных сессий для работы с БД
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

# Создание таблиц в БД, если не существуют
async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

# Получение объекта SQLAlchemyUserDatabase для управления пользователями
# async def get_user_db(session: AsyncSession = Depends(get_async_session)):
#     yield SQLAlchemyUserDatabase(session, User)