
import pandas as pd
import geopandas as gpd

import pathlib

# 1. clean the geodata file and add last months avg gas prices across provinces
def clean_geo_data():
    df_gas_price_last_month = pd.read_csv('data/last_month_reg_gas_avg_prov.csv', index_col=['PROVINCE'])
    print(df_gas_price_last_month.head())
    f = pathlib.Path() / 'data' / 'georef-canada-province.geojson'
    assert f.exists()
    gdf = gpd.read_file(f)
    gdf['last_month_avg'] = None

    for i, p in enumerate(gdf.prov_name_en.values):
        try:
            v = df_gas_price_last_month.loc[p][0]
            gdf.at[i, 'last_month_avg'] = v
        except:
            pass

    # save the file
    gdf.to_file('data/last_month_prov_gasprices.geojson', driver='GeoJSON')

