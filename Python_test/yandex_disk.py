import requests
import config


class YandexDisk:
    def __init__(self):
        self.token = config.yandex_token
        self.headers = self.__get_headers()
        self.base_url = config.yandex_disk_api_base_url

    def __get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def get_directory_info(self, directory_name):
        endpoint = f'{self.base_url}/resources'
        params = {"path": directory_name}
        try:
            response = requests.get(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            print(f'Method {self.get_directory_info.__name__} ----Status code: {response.status_code}')
            return response.json(), response.status_code
        except:
            print(f'Method {self.get_directory_info.__name__} ----Status code: {response.status_code}')
            return response.json(), response.status_code

    def create_folder(self, directory_name):
        endpoint = f'{self.base_url}/resources'
        params = {"path": directory_name}
        try:
            response = requests.put(endpoint, headers=self.headers, params=params)
            response.raise_for_status()
            print(f'Method {self.get_directory_info.__name__} ----Status code: {response.status_code}')
            return response.status_code
        except:
            print(f'Method {self.get_directory_info.__name__} ----Status code: {response.status_code}')
            return response.status_code


def main():
    yandex_loader = YandexDisk()
    yandex_loader.create_folder('test_directory')
    yandex_loader.get_directory_info('test_directory')


if __name__ == '__main__':
    main()
