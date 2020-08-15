from json_utils import *
from selenium_utils import *

wd = get_webdriver()
items = get_items(wd, ['vay'], 1)
print(items[0].keys())