from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager


socks_proxy_ip = '127.0.0.1'
socks_proxy_port = 9150

# SOCKS5 SETUP:-
profile = webdriver.FirefoxProfile()
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', socks_proxy_ip)
profile.set_preference('network.proxy.socks_port', int(socks_proxy_port))

driver_path = GeckoDriverManager().install()
driver = webdriver.Firefox(executable_path=driver_path, firefox_profile=profile)
driver.get('https://api.ipify.org/')
