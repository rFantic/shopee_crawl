from json_utils import *
from selenium_utils import *

wd = get_webdriver()
category_id = 77 # thoi trang nu
items = get_items(wd, ['vay'], 1, category_id)
print(items[0].keys())