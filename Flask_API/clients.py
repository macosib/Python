import requests

HOST = "http://127.0.0.1:5000"


def get_data():
    response = requests.get(f'{HOST}/advertisement/10')
    print(response.json())


def post_data():
    data = {
        'title': 'Продам авто',
        'description': 'Не битая, не крашенная',
        'author': 'Иван Петрович',
    }
    response = requests.post(f'{HOST}/advertisement', json=data)
    print(response.json())


def delete_data():
    response = requests.delete(f'{HOST}/advertisement/9/')
    print(response.json())


# for i in range(25):
#     post_data()
get_data()
# delete_data()
