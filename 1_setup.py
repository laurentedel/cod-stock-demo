%load_ext autoreload
%autoreload 2
import logging
from db import Db
from get_stock_data import upsert_data, get_dataset
model=Db()
model.drop_stocks_table()
model.create_stock_table()
