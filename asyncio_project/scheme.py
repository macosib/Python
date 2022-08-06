from typing import List

import pydantic
from pydantic import validator


class PersonBase(pydantic.BaseModel):
    birth_year: str
    eye_color: str
    films: List[str] = None
    gender: str
    hair_color: str
    height: str
    homeworld: str
    mass: str
    name: str
    skin_color: str
    species: List[str] = None
    starships: List[str] = None
    vehicles: List[str] = None

    @validator('species', 'starships', 'vehicles', 'films')
    def validator_species(cls, value):
        if value:
            return ','.join(value)
        else:
            return ''


class HttpError(Exception):
    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message
