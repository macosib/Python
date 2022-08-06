import pydantic
from aiohttp import web
from db import init_orm

from db import AdvertisementModel
from handlers import NotFound, BadRequest
from serializer import CreateAdvertisementModel, GetAdvertisementModel


class AdvertisementView(web.View):

    async def get(self):
        adv_id = self.request.match_info['id']
        advertisement = await AdvertisementModel.get(int(adv_id))
        if advertisement is None:
            raise NotFound(error='user not found')
        return web.json_response(GetAdvertisementModel(**advertisement.to_dict()).dict())

    async def post(self):
        json_data = await self.request.json()
        try:
            json_data_validate = CreateAdvertisementModel(**json_data).dict()
        except pydantic.ValidationError as er:
            raise BadRequest(error=er.errors())
        advertisement = await AdvertisementModel.create(**json_data_validate)
        return web.json_response({
            'id': advertisement.id,
            'author': advertisement.author,
            'description': advertisement.description,
        })

    async def delete(self):
        adv_id = self.request.match_info['id']
        advertisement = await AdvertisementModel.get(int(adv_id))
        try:
            await advertisement.delete()
            print(advertisement)
            return web.json_response(GetAdvertisementModel(**advertisement.to_dict()).dict())
        except AttributeError as er:
            raise BadRequest(error=er.args)



app = web.Application()
app.router.add_view("/advertisement/{id:\d+}/", AdvertisementView)
app.router.add_view("/advertisement/", AdvertisementView)
app.cleanup_ctx.append(init_orm)

if __name__ == '__main__':
    web.run_app(app)
