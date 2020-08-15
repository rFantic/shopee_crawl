# shopee_crawl

~~~
from json_utils import *
from selenium_utils import *

driver_path = "chromedriver"
wd = get_webdriver(driver_path)
category_id = 77 # thoi trang nu
items = get_items(wd, ['vay', 'quan', 'ao', 'phu kien'], 5, category_id)
item_id_0, shop_id_0 = next(iter(items))
print(item_id_0, shop_id_0)
print(items[(item_id_0, shop_id_0)].keys())

conn = sqlite3.connect('shopee.db')
c = conn.cursor()
insert_item(c, item_id_0, shop_id_0)
conn.commit()
conn.close()
~~~
