import os
import time
import sys

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config_yandex import login_yandex, password_yandex


class YandexAuthSecond:
    url = 'https://passport.yandex.ru/auth/'

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def __get_code(self):
        code = input('Введите код с смс: ')
        return code

    def get_access(self):
        service = Service(f'{os.path.abspath("chromedriver")}/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get(self.url)
        driver.find_element(by=By.XPATH, value='//*[@id="passp-field-login"]').send_keys(self.login)
        driver.find_element(by=By.XPATH, value='//*[@id="passp:sign-in"]').click()
        time.sleep(3)
        driver.find_element(by=By.NAME, value='passwd').send_keys(self.password)
        driver.find_element(by=By.XPATH, value='//*[@id="passp:sign-in"]').click()
        time.sleep(10)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="root"]/div/div[2]/div[2]/div/div/div[2]/'
                                  'div[3]/div/div/div/div[1]/form/div[2]/button').click()
        accept_code = YandexAuthSecond.__get_code(self)
        time.sleep(10)
        driver.find_element(by=By.ID, value='passp-field-phoneCode').send_keys(accept_code)
        driver.find_element(by=By.XPATH,
                            value='//*[@id="root"]/div/div[2]/div[2]/'
                                  'div/div/div[2]/div[2]/form/div[2]/button  ').click()
        time.sleep(3)
        return driver.title, driver.current_url

def main():
    Ya = YandexAuthSecond(login_yandex, password_yandex)
    Ya.get_access()


if __name__ == '__main__':
    main()


