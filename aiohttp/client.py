import aiohttp
import asyncio

from config import HOST


async def get_data():
    async with aiohttp.ClientSession() as session:
        async with session.get(f'{HOST}/advertisement/3/') as response:
            print(await response.text())


async def post_data():
    data = {
        'title': 'Продам авто',
        'description': 'Не битая, не крашенная',
        'author': 'Иван Петрович',
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(f'{HOST}/advertisement/', json=data) as response:
            print(await response.text())


async def delete_data():
    async with aiohttp.ClientSession() as session:
        async with session.delete(f'{HOST}/advertisement/4555/') as response:
            print(await response.text())


if __name__ == '__main__':
    asyncio.run(get_data())
    asyncio.run(post_data())
    asyncio.run(delete_data())
