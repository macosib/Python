from datetime import datetime

import pydantic


class CreateAdvertisementModel(pydantic.BaseModel):
    title: str
    description: str
    author: str

    @pydantic.validator('title')
    def min_lenght_title(cls, value):
        if len(value) < 2:
            raise ValueError('header to short')
        return value


class GetAdvertisementModel(pydantic.BaseModel):
    id: int
    title: str
    description: str
    author: str
    create_date: datetime

    @pydantic.validator('create_date')
    def validated_date(cls, date: datetime):
        return date.isoformat()
