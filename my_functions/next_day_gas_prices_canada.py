

from variables import Provinces, url_gaswizard

import pandas as pd
import numpy as np
import openpyxl

# 1. Function to create a csv file of the gas prices across Canadian cities for the next day along with their lat/long

def clean_next_day_gas_prices_can():

    df_can_cities_latlng = pd.read_csv("data/canadian_cities_latlng.csv")

    ## Using the pandas read_html method to read in the table from gaswizard.ca
    table = pd.read_html(url_gaswizard)
    df = table[0]

    df = df[df['City'].str.contains("adsbygoogle") == False]
    cities = df.City.replace({":": ""}, regex=True)
    df.loc[:, "City"] = cities
    next_day_gas_df = df.copy(deep=True)
    next_day_gas_df.loc[:, "City"] = cities.values

    next_day_gas_df["Province"] = Provinces
    next_day_gas_df["Country"] = "Canada"
    next_day_gas_df["Location"] = next_day_gas_df["City"] + ", " + next_day_gas_df["Province"] + ", " + next_day_gas_df[
        "Country"]
    # print(next_day_gas_df.info())
    # print(df_can_cities_latlng.info())
    next_day_gas_df["lat_lng"] = df_can_cities_latlng["lat_lng"].values

    testing = next_day_gas_df.copy(deep=True)
    testing = testing['Regular'].str.split(' ', expand=True)
    if len(testing.columns) == 2:
        next_day_gas_df[["Regular_Price", "Symbol"]] = next_day_gas_df["Regular"].str.split(" ", expand=True)
        next_day_gas_df["Amount"] = 0
    else:
        next_day_gas_df[["Regular_Price", "Symbol", "Amount"]] = next_day_gas_df["Regular"].str.split(" ", expand=True)
        next_day_gas_df["Amount"] = pd.to_numeric(next_day_gas_df['Amount'].replace(np.nan, 0))
    next_day_gas_df["Regular_Price"] = pd.to_numeric(next_day_gas_df["Regular_Price"].replace(np.nan, 0))
    next_day_gas_df["Regular_Price"] = round((next_day_gas_df["Regular_Price"] / 100), 2)
    new = next_day_gas_df["Regular"].str.split(" ", n=1, expand=True)
    next_day_gas_df["Symbol_Amount"] = new[1]
    next_day_gas_df["Regular"] = new[0]
    # next_day_gas_df["Amount"] = pd.to_numeric(next_day_gas_df['Amount'].replace(np.nan, 0))

    ## Save the modified upcoming gas prices across Canadian cities dataframe to a xlsx filetype
    # print(next_day_gas_df.tail())
    next_day_gas_df.to_excel('data/tomorrow_gasprices_canadiancities_latlng.xlsx', sheet_name='prices', index=False)