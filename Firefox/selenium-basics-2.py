import os
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


def load_driver():
    # Download Chromedriver if path not exists
    if os.path.exists('driver.path'):
        with open('driver.path', 'r', encoding='utf-8') as file:
            path = file.read()
            file.close()
    else:
        path = GeckoDriverManager().install()
        with open('driver.path', 'w', encoding='utf-8') as file:
            file.write(path)
            file.close()
    return path


driver_path = load_driver()
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('http://example.com')