from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def get_webdriver():
	driver_path = ChromeDriverManager().install()
	chrome_options = webdriver.ChromeOptions()
	chrome_options.add_argument('--headless')
	chrome_options.add_argument('window-size=1366x768')
	chrome_options.add_argument('--no-sandbox')
	chrome_options.add_argument('--disable-dev-shm-usage')
	wd = webdriver.Chrome(driver_path,options=chrome_options)
	return wd