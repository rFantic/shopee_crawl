from json_utils import *
from selenium_utils import *
from sql_utils import insert_item
import sqlite3

wd = get_webdriver()
category_id = 77 # thoi trang nu
items = get_items(wd, ['vay'], 1, category_id)
item_id_0, shop_id_0 = next(iter(items))
print(item_id_0, shop_id_0)
print(items[(item_id_0, shop_id_0)].keys())

conn = sqlite3.connect('shopee.db')
c = conn.cursor()
insert_item(c, item_id_0, shop_id_0)
conn.commit()
conn.close()
