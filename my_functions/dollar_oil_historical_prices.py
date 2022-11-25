
from my_functions.date_functions import todays_date
from variables import days, years, periods

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

    means = dict()

    for period in periods[2:]:
        y = int(period[period.find("_")+1:period.find(" ")+3])
        data = get_yahoo_data(ticker, period)
        data = data.reset_index()
        data["month_year"] = data["Date"].apply(lambda x: x.strftime("%b-%y"))
        year_of_data = y - 1
        mean = data[data["month_year"] == (last_month - pd.offsets.DateOffset(years = year_of_data)).strftime("%b-%y")]["Close"].mean()
        key = "period_" + str(year_of_data) + "y"
        means[key] = round(mean, 3)

    for i, period in enumerate(periods[0:2]):
        if days[i] == 1 and today.weekday() == 6:
            data = get_yahoo_data(ticker, '3d')
            close = data["Close"][-1]
            open = data["Open"][-1]
            key = "period_" + "1d"
            means[key] = round(close, 3)
            yest_close_date = date.index[0].strftime("%b %d, %Y")
        elif days[i] == 1 and today.weekday() in [0,1,2,3,4,5] :
            data = get_yahoo_data(ticker, period)
            close = data["Close"][-1]
            open = data['Open'][-1]
            key = "period_" + period
            means[key] = round(close,3)
            yest_close_date = data.index[0].strftime("%b %d, %Y")
        else:
            data = get_yahoo_data(ticker, period)
            data = data.reset_index()
            data["month_year"] = data["Date"].apply(lambda x: x.strftime("%b-%y"))
            mean = data[data["month_year"] == (last_month.strftime("%b-%y"))]["Close"].mean()
            key = "period_" + period
            means[key] = round(mean,3)

    return open, yest_close_date, means

def hist_gas_can():
    df_can_hist = pd.read_csv(filepath_or_buffer='data/hist_gas_canada.csv',
                              na_values="..")

    hist_gas_price_can = dict()

    for y in years:
        value = df_can_hist[
            df_can_hist["REF_DATE"] == (last_month - pd.offsets.DateOffset(years=y)).strftime("%b-%y")].reset_index(
            drop=True)._get_value(0, 'VALUE')
        date = df_can_hist[
            df_can_hist["REF_DATE"] == (last_month - pd.offsets.DateOffset(years=y)).strftime("%b-%y")].reset_index(
            drop=True)._get_value(0, 'REF_DATE')
        date = (last_month - pd.offsets.DateOffset(years=y)).strftime("%b-%Y")
        hist_gas_price_can[date] = value

    return hist_gas_price_can

def current_can_mean_gas():
    df_can_gas_prices = pd.read_excel('data/tomorrow_gasprices_canadiancities_latlng.xlsx')
    current_can_mean = round(df_can_gas_prices["Regular"].mean(), 2)
    return current_can_mean




