import pydantic
from flask import Flask, jsonify, request
from flask.views import MethodView
from sqlalchemy.exc import NoResultFound

from models import Session, AdvertisementModel
from serializers import CreateAdvertisementModel, HttpError

app = Flask(__name__)


class AdvertisementView(MethodView):

    def get(self, id_adv: int):
        try:
            with Session() as session:
                adv = session.query(AdvertisementModel).filter(AdvertisementModel.id == id_adv).one()
                return jsonify({
                    'id': adv.id,
                    'author': adv.author,
                    'descrition': adv.description,
                    'create_date': adv.create_date,
                    'title': adv.title,
                })
        except NoResultFound as er:
            raise HttpError(400, er.args)

    def post(self):
        json_data = dict(request.json)
        print(json_data)
        try:
            json_data_validate = CreateAdvertisementModel(**json_data).dict()
        except pydantic.ValidationError as er:
            raise HttpError(400, er.errors())

        with Session() as session:
            advertisement = AdvertisementModel(**json_data_validate)
            session.add(advertisement)
            session.commit()
            return jsonify({
                'id': advertisement.id,
                'author': advertisement.author,
                'descrition': advertisement.description,
            })

    def delete(self, id_adv: int):
        try:
            with Session() as session:
                adv = session.query(AdvertisementModel).filter(AdvertisementModel.id == id_adv).one()
                session.delete(adv)
                session.commit()
                return jsonify({
                    'deleted': 'sucsessful',
                    'id': adv.id,
                    'title': adv.title, })
        except NoResultFound as er:
            raise HttpError(400, er.args)


@app.errorhandler(HttpError)
def http_error_hander(error):
    responce = jsonify({
        'error': error.error_message,
    })
    responce.status_code = error.status_code
    return responce


app.add_url_rule('/advertisement/<int:id_adv>/', view_func=AdvertisementView.as_view('advertisement_delete'),
                 methods=['DELETE', 'GET'])
app.add_url_rule('/advertisement', view_func=AdvertisementView.as_view('advertisement_create'), methods=['POST'])

if __name__ == '__main__':
    app.run(debug=True)
