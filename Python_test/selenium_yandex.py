import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config_yandex import login_yandex, password_yandex


class YandexAuth:
    url = 'https://passport.yandex.ru/auth/'

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def get_access_only_password(self):
        service = Service(f'{os.path.abspath("chromedriver")}/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(self.url)
        driver.find_element(by=By.XPATH, value='//*[@id="passp-field-login"]').send_keys(self.login)
        driver.find_element(by=By.XPATH, value='//*[@id="passp:sign-in"]').click()
        time.sleep(3)
        driver.find_element(by=By.NAME, value='passwd').send_keys(self.password)
        driver.find_element(by=By.XPATH, value='//*[@id="passp:sign-in"]').click()
        time.sleep(3)
        return driver.title, driver.current_url


def main():
    Ya = YandexAuth(login_yandex, password_yandex)
    Ya.get_access_only_password()


if __name__ == '__main__':
    main()
