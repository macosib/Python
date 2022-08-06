import asyncio
import aiohttp
import asyncpg

from more_itertools import chunked
from pydantic import ValidationError
from config import PG_DSN, BASE_URI
from scheme import PersonBase
from typing import Tuple

async def get_character(character_id: int, session) -> object:
    async with await session.get(f'{BASE_URI}{character_id}') as response:
        json_data = await response.json()
        if response.status == 200:
            return json_data
        else:
            pass

async def validated_person_list(person_list: Tuple):
    valid_person_list = []
    for person in person_list:
        if person:
            try:
                valid_person_list.append(tuple(PersonBase(**person).dict().values()))
            except ValidationError as err:
                print(err.errors())

    return valid_person_list


async def insert_users(pool: asyncpg.Pool, person_list):
    query = 'INSERT INTO people (birth_year, eye_color, films, ' \
            'gender,hair_color, height,' \
            'homeworld, mass, name, ' \
            'skin_color, species, starships, vehicles' \
            ') VALUES($1,$2,$3,$4,$5,$6,$7,$8,$9,$10,$11,$12,$13)'
    try:
        async with pool.acquire() as connection:
            async with connection.transaction():
                await connection.executemany(query, person_list)
    except TypeError as err:
        print(err.args)


async def main():
    async with aiohttp.ClientSession() as session:
        tasks = []
        pool = await asyncpg.create_pool(PG_DSN, min_size=20, max_size=20)
        for characters_chunk in chunked((get_character(i, session) for i in range(1, 90)), 10):
            result = await asyncio.gather(*characters_chunk)
            valid_result = await validated_person_list(result)
            tasks.append(asyncio.create_task(insert_users(pool, valid_result)))
        await asyncio.gather(*tasks)
        await pool.close()


if __name__ == '__main__':
    asyncio.run(main())
