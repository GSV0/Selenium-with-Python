from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--proxy-server=socks5://{}'.format('127.0.0.1:9150'))

driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
driver.get('https://api.ipify.org/')
