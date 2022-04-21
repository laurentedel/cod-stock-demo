# cod-stock-demo

This project is about using COD (_Cloudera Operational Database_) and CML (_Cloudera Machine Learning_) for predicting stock prices, based on their historical data.

We're assuming that you have a COD and CML instances up and running. You will also need a Alpha Vantage API token, you can claim for a free token here: https://www.alphavantage.co/support/#api-key

As we'll use Python to access COD from CML, go in the Python tab of your COD instance and copy the Phoenix Python URL endpoint

![image](https://user-images.githubusercontent.com/7782997/164310529-1e94c958-bd08-4a88-a4dd-32615b5d93d0.png)

Now, in CML, the new project being imported with this repository, we'll have to setup some environment variables.
For that, go in Project Settings / Advanced and put the following variables:

```
API_KEY=<YOUR_ALPHA_VANTAGE_API_TOKEN>
WORKLOAD_USER=<USERNAME>
WORKLOAD_PASSWORD=<PASSWORD>
OPDB_ENDPOINT=<PHOENIX_PYTHON_URL_ENDPOINT>
MAX_TEXT_LENGTH=1000000 # for libs installation
TF_CPP_MIN_LOG_LEVEL=3 # for avoiding unnecessary Tensorflow logging
```

![image](https://user-images.githubusercontent.com/7782997/164311271-65cd0f1a-9545-4329-9bb6-653651dfe482.png)

Open a new session (4GB RAM minimum to install keras/tensorflow packages), and install all the required libraries (you might open a terminal window)

```
pip3 install -r requirements.txt
```

There are 2 steps to follow: 
1. Run the `1_setup.py` script to connect to COD and create the table we'll need
2. Run the `2_runner.py` script 

The `runner.py` will do the following:
* Get daily stocks from Alpha Vantage
* Store data in COD
* Run the model and create the model file
* Run the prediction over the last 120 days
* Compute the predicted earnings if we buy/sell the stocks at the exact rates

![image](https://user-images.githubusercontent.com/7782997/164312863-8e9c058c-afa3-43ca-8727-dd22928e765e.png)

So for each of the 30 stocks here, you will get the latest data, stored in COD, plotting the real and the predicted stock prices, and calculate earnings: 
* revenue
* performance
* predicted price
* the recommendation between don't buy, keep or sell
* a signal high/low depending on the strength of the recommendation

![image](https://user-images.githubusercontent.com/7782997/164313976-fcf49325-d879-4ca1-8186-619efa9e29bc.png)

At the very end, you'll have a dataframe with a recap of all the predictions

![image](https://user-images.githubusercontent.com/7782997/164314095-788008e2-5391-40af-9b60-9c6bd3c1b6eb.png)

