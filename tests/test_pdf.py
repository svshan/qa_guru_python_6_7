from pypdf import PdfReader
import os

# TODO оформить в тест, добавить ассерты и использовать универсальный путь

resources_path = os.path.join(os.path.dirname(__file__), '..', 'resources')
pdf_file_path = os.path.join(resources_path, 'docs-pytest-org-en-latest.pdf')


def test_pdf_file():
    reader = PdfReader(pdf_file_path)
    number_of_pages = len(reader.pages)
    page = reader.pages[0]
    text = page.extract_text()
    print(page)
    print(number_of_pages)
    print(text)

    assert 'Jul 14, 2022' in text
    assert len(reader.pages) == 412
