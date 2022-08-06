import asyncio
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

from config import PG_DSN_ALC

Base = declarative_base()

engine = create_async_engine(PG_DSN_ALC, echo=True)
Session = sessionmaker(bind=engine)


class PeopleModel(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    birth_year = Column(String, nullable=False)
    eye_color = Column(String, nullable=False)
    films = Column(String, nullable=False)
    gender = Column(String, nullable=True)
    hair_color = Column(String, nullable=True)
    height = Column(String, nullable=False)
    homeworld = Column(String, nullable=True)
    mass = Column(String, nullable=False)
    name = Column(String, nullable=False)
    skin_color = Column(String, nullable=True)
    species = Column(String, nullable=True)
    starships = Column(String, nullable=True)
    vehicles = Column(String, nullable=True)

    def __repr__(self):
        return f'id: {self.id}, name: {self.name}'


async def get_async_session(
        drop: bool = False, create: bool = False
):
    async with engine.begin() as conn:
        if drop:
            await conn.run_sync(Base.metadata.drop_all)
        if create:
            await conn.run_sync(Base.metadata.create_all)
    async_session_maker = sessionmaker(
        engine, expire_on_commit=False, class_=AsyncSession
    )
    return async_session_maker


async def main():
    await get_async_session(True, True)


if __name__ == '__main__':
    asyncio.run(main())
