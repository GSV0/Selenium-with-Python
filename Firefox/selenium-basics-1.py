from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

# Download GeckoDriver
driver_path = GeckoDriverManager().install()
driver = webdriver.Firefox(executable_path=driver_path)
driver.get('http://example.com')
