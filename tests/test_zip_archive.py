import os
from zipfile import ZipFile

'''Создать новые тесты, которые заархивируют имеющиеся в resources различные
типы файлов в один архив в tmp и проверят тестом в архиве каждый из файлов,
что он является тем самым, который был заархивирован, не распаковывая архив.'''

tmp_path = os.path.join(os.path.dirname(__file__), '..', 'tmp')
zip_file_path = os.path.join(tmp_path, 'new_archive.zip')
resources_path = os.path.join(os.path.dirname(__file__), '..', 'resources')
files = os.listdir(resources_path)


def test_zip_file_creation_and_reading():
    with ZipFile(zip_file_path, 'w') as archive:
        for file in files:
            archive.write(os.path.join(resources_path, file), file)
    assert os.path.exists(zip_file_path)

    with ZipFile(zip_file_path, 'r') as archive:
        file_list = archive.namelist()
        for file in file_list:
            print(file)
            assert file in files

    os.remove(zip_file_path)
