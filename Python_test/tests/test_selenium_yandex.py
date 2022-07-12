import unittest

import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config_yandex import login_yandex, password_yandex


class TestYandexAuth(unittest.TestCase):
    url = 'https://passport.yandex.ru/auth/'
    login = login_yandex
    password = password_yandex

    def setUp(self):
        print('Запускаем драйвер')
        self.service = Service(f'{os.path.abspath("chromedriver")}/chromedriver')
        self.driver = webdriver.Chrome(service=self.service)

    def test_get_access_only_password(self):
        self.driver.get(self.url)
        self.driver.find_element(by=By.XPATH, value='//*[@id="passp-field-login"]').send_keys(self.login)
        self.driver.find_element(by=By.XPATH, value='//*[@id="passp:sign-in"]').click()
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value='passwd').send_keys(self.password)
        self.driver.find_element(by=By.XPATH, value='//*[@id="passp:sign-in"]').click()
        time.sleep(2)
        self.assertEqual(self.driver.title, 'Яндекс ID')

    def tearDown(self):
        print('Закрываем драйвер')
        self.driver.close()
