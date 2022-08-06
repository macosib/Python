from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, DateTime, String, func
from sqlalchemy.orm import sessionmaker

PG_DSN = 'postgresql://flask_db:flask_db@127.0.0.1:5430/flask_db'

BaseModel = declarative_base()
engine = create_engine(PG_DSN)

Session = sessionmaker(bind=engine)


class AdvertisementModel(BaseModel):
    __tablename__ = 'advertisement'

    id = Column(Integer, primary_key=True)
    title = Column(String, index=True, nullable=False)
    description = Column(String, nullable=False)
    create_date = Column(DateTime, server_default=func.now())
    author = Column(String, nullable=False)

    def __repr__(self):
        return f'{self.id}-{self.header}-{self.description}-{self.create_date}-{self.author}'


BaseModel.metadata.create_all(engine)
