import os.path
import requests

# TODO оформить в тест, добавить ассерты, сохранять и читать из tmp, использовать универсальный путь

url = 'https://selenium.dev/images/selenium_logo_square_green.png'

tmp_path = os.path.join(os.path.dirname(__file__), '..', 'tmp')
downloaded_file_path = os.path.join(tmp_path, 'selenium_logo.png')


def test_download_file_with_api():
    response = requests.get(url)
    with open(downloaded_file_path, 'wb') as file:
        file.write(response.content)

    size = os.path.getsize(downloaded_file_path)
    print(size)

    assert size == 30803
    assert response.status_code == 200
    assert os.path.exists(downloaded_file_path)

    os.remove(downloaded_file_path)
