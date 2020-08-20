from json_utils import *
from cache_utils import saved_data
from selenium_utils import *
from sql_utils import insert_item
import sqlite3

wd = get_webdriver()
category_id = 77 # thoi trang nu
items = get_items(wd, ['vay', 'quan', 'ao', 'phu kien'], 5, category_id)
item_id_0, shop_id_0 = next(iter(items))
print(item_id_0, shop_id_0)
print(items[(item_id_0, shop_id_0)].keys())

items_id = list(saved_data['items_dict'].keys())[:5]
print(saved_data['items_dict'][items_id[0]].keys())

conn = sqlite3.connect('shopee.db')
c = conn.cursor()
insert_item(c, item_id_0, shop_id_0)
conn.commit()
conn.close()
