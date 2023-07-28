import csv
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

resources_path = os.path.join(os.path.dirname(__file__), '..', 'resources')
csv_file_path = os.path.join(resources_path, 'eggs.csv')


def test_csv_file():
    with open(csv_file_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])
    assert os.path.exists(csv_file_path)
    assert os.path.getsize(csv_file_path) > 0

    with open(csv_file_path) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
            assert len(row) == 3

    os.remove(csv_file_path)
