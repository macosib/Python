from yandex_disk import YandexDisk

class TestYandex:

    yandex_object = YandexDisk()

    def test_create_folder(self):
        assert YandexDisk.create_folder(TestYandex.yandex_object, 'Test_dir') == 201


    def test_get_directory_info(self):
        assert YandexDisk.get_directory_info(TestYandex.yandex_object, 'Test_dir')[1] == 200
