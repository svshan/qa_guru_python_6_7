import time
import os
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


tmp_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'tmp')
file_path = os.path.join(tmp_path, 'pytest-main.zip')


def test_download_file_through_ui():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": tmp_path,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.config.driver = driver
    browser.config.driver_options = webdriver.ChromeOptions()
    browser.config.driver_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
    # browser.config.driver_options = options

    browser.open("https://github.com/pytest-dev/pytest")
    browser.element(".d-none .Button-label").click()
    browser.element('[data-open-app="link"]').click()
    time.sleep(5)

    assert os.path.exists(file_path)
    assert os.path.getsize(file_path) > 0

    os.remove(file_path)
