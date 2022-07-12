from selenium_yandex import YandexAuth
from config_yandex import *


def test_get_access_only_password():
    ya_auth = YandexAuth(login_yandex, password_yandex)
    assert ya_auth.get_access_only_password()[0] == 'Яндекс ID'
