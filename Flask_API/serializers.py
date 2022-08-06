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


class HttpError(Exception):
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message
