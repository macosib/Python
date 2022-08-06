import json

from aiohttp import web


class HttpError(web.HTTPError):
    def __init__(self, *args, error='', **kwargs):
        kwargs['text'] = json.dumps({'error': error})
        super().__init__(*args, **kwargs, content_type='application/json')

class BadRequest(HttpError):
    status_code = 400

class NotFound(HttpError):
    status_code = 404