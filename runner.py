%load_ext autoreload
%autoreload 2
from tech_ind_model import run_model
from get_stock_data import get_dataset , upsert_data
from predict import Predict
import time
import os.path
import pandas as pd
from os import path

symbols=['NLOK','AMD','QRVO','NVDA','AAPL','AMZN', 
         'GOOGL','FB','ORCL','CSCO','IBM','UBER','LYFT','COST',
         'MCD','BA','AAL','MSFT','GM','KO','QCOM','BABA','UAA',
         'HPQ','ZNGA','GM','QCOM','JBLU','XRX','ADBE']

total_earnings = pd.DataFrame()
start = time.time()

for symbol in symbols:
    symbol_start = time.time()

    #get data from the API
    data = get_dataset(symbol,'daily')

    # upsert data in COD
    upsert_data(symbol,data)

    # run model
    run_model(symbol,True)

    # Prediction over the last 120 days
    p = Predict(symbol)
    p.prediction(120)
         
    # calculate earning
    earnings = p.calculate_earnings()
    
    display(earnings)
    total_earnings = total_earnings.append(earnings, ignore_index = True)
    print ("done in " + time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - symbol_start)))
    

display(total_earnings)
print ("Total execution time: " + time.strftime("%Hh%Mm%Ss", time.gmtime(time.time() - start)))
