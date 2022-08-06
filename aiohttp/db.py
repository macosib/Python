from config import DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME
from sqlalchemy import (Column, Integer, String, DateTime, func)
from gino import Gino


def construct_pg_dsn():
    return f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


db = Gino()


class AdvertisementModel(db.Model):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    create_date = Column(DateTime, server_default=func.now())
    author = Column(String, nullable=False)

    _idx1 = db.Index('app_advertisement_id', 'id', unique=True)


async def init_orm(app):
    await db.set_bind(construct_pg_dsn())
    await db.gino.create_all()
    yield
    await db.pop_bind().close()
