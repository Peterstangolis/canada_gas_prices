import numpy as np
import pandas as pd
import geopandas as gpd

import pathlib

# 1. clean the geodata file and add last months avg gas prices across provinces
def clean_geo_data():
    df_gas_price_last_month = pd.read_csv('data/last_month_reg_gas_avg_prov.csv', index_col=['PROVINCE'])
    f = pathlib.Path() / 'data' / 'georef-canada-province.geojson'
    assert f.exists()
    gdf = gpd.read_file(f)
    gdf['last_month_avg'] = np.NaN
    gdf["prov_name_en"] = gdf["prov_name_en"].str.strip()
    index_vals = df_gas_price_last_month.index.values
    index_vals = [x.strip() for x in index_vals]
    df_gas_price_last_month.index = df_gas_price_last_month.index.map(str.strip)

    for i, p in enumerate(gdf.prov_name_en.values):

        try:
            v = df_gas_price_last_month.loc[p][0]
            gdf.at[i, 'last_month_avg'] = v
        except:
            pass

    # save the file
    gdf.to_file('data/last_month_prov_gasprices.geojson', driver='GeoJSON')

