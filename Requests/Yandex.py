import requests
import os


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }
        params = {"path": file_path, "overwrite": "true", 'fields': 'href'}
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        response_link = requests.get(upload_url, headers=headers, params=params, timeout=5)
        link_upload = response_link.json().get('href', '')
        response = requests.put(link_upload, data=open(os.path.join(os.getcwd(), file_name), 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success")


if __name__ == '__main__':
    file_name = 'test_file.txt'
    path_to_file = 'Test/test_file.txt'
    token = '...'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)
