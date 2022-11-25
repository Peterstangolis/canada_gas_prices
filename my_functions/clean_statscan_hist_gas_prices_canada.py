
# import pandas as pd

def clean_hist_gas_can():

    df = pd.read_csv('data/hist_gasprices_can_1980_2022.csv')

    df_canada = df[df["CITY"] == "Canada"].reset_index(drop=True)[['REF_DATE', 'CITY', 'Type of fuel', 'VALUE']]
    df_canada.to_csv("data/hist_gas_canada.csv", index=False)

    df_cities = df[df["CITY"] != "Canada"].reset_index(drop=True)[
        ['REF_DATE', 'CITY', 'PROVINCE', 'Type of fuel', 'VALUE']]
    df_cities.to_csv("data/hist_gas_cities.csv", index=False)