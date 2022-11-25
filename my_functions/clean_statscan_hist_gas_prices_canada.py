
from my_functions.date_functions import last_month_year_current
import pandas as pd

def clean_hist_gas_can():

    df = pd.read_csv('data/hist_gasprices_can_1980_2022.csv')

    df_canada = df[df["CITY"] == "Canada"].reset_index(drop=True)[['REF_DATE', 'CITY', 'Type of fuel', 'VALUE']]
    df_canada.to_csv("data/hist_gas_canada.csv", index=False)

    df_cities = df[df["CITY"] != "Canada"].reset_index(drop=True)[
        ['REF_DATE', 'CITY', 'PROVINCE', 'Type of fuel', 'VALUE']]
    df_cities["REF_DATE"] = df_cities["REF_DATE"].str.strip()
    df_cities.to_excel("data/hist_gas_cities.xlsx", index=False)

    last_month_year = last_month_year_current()

    last_month_year = last_month_year_current()

    df_prov_avg_gas_prices_regular = df_cities.loc[(df_cities["REF_DATE"] == str(last_month_year)) & (df_cities["Type of fuel"] == "Regular Unleaded")].groupby(by=['PROVINCE'], dropna=False)['VALUE'].mean()

    df_prov_avg_gas_prices_regular.index = df_prov_avg_gas_prices_regular.index.map(str.strip)


    df_prov_avg_gas_prices_regular.to_csv('data/last_month_reg_gas_avg_prov.csv')