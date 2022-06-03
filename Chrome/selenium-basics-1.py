from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Download Chromedriver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://example.com')
