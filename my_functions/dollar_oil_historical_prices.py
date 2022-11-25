
from variables import periods
from date_functions import todays_date
from variables import days, years

import yfinance as yf
from numpy import mean
import pandas as pd




## Dates
today, full_day, last_month = todays_date()


## Retriee relevant data from yfinance
def get_yahoo_data(ticker, time_period, interval='1d'):
    data = yf.Ticker(ticker=ticker)
    data = data.history(period=time_period, interval=interval)
    return data

## returns a dictionary of historical oil / exchange rate data
def retrieve_historical_pricing(ticker):

    cad_usd_means
