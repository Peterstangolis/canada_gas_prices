
## from my_functions

from my_functions.date_functions import date_from_website, todays_date, add_suffix
from variables import map_styles, flags
from my_functions.next_day_gas_prices_canada import clean_next_day_gas_prices_can
from my_functions.clean_statscan_hist_gas_prices_canada import clean_hist_gas_can




from datetime import date, timedelta, datetime

import branca.colormap
import pandas as pd
import ast
import pathlib
import geopandas as gpd
import folium
import branca.colormap as cm
from branca.colormap import linear
import geopandas as gdp


today, long_format_today, last_month = todays_date()
tomorrow_long_format = add_suffix()
date_from_gaswizard = date_from_website()

tomorrow = today + timedelta(days=1)

if date_from_gaswizard == tomorrow_long_format:
    t = tomorrow
else:
    t = today

# clean_hist_gas_can()
# clean_next_day_gas_prices_can()
# clean_geo_data()

## import the required data
df_gas_price_last_month = pd.read_csv('data/last_month_reg_gas_avg_prov.csv',
                                       names = ['province', 'last_month_avg'],
                                       header=None,
                                       skiprows=1,
                                       index_col='province')


df_gas_prices_upcoming = pd.read_excel('data/tomorrow_gasprices_canadiancities_latlng.xlsx')
df_gas_prices_upcoming.lat_lng = df_gas_prices_upcoming.lat_lng.apply(ast.literal_eval)

f = pathlib.Path() / 'data' / 'last_month_prov_gasprices.geojson'
assert f.exists()
gdf = gdp.read_file(f)

min_gas = df_gas_price_last_month.last_month_avg.min()
max_gas = df_gas_price_last_month.last_month_avg.max()


colorscale = cm.LinearColormap(colors=["#F7FD66", "#FFB700", '#990000'] ,

                               vmin=min_gas, vmax=max_gas)
colorscale.caption = f"Average Provincial Gas Price for {last_month:%b-%Y}"

## change avg_gas_prices to string
#gdf["last_month_avg"] = gdf["last_month_avg"].astype(str)



def folium_map():
    from streamlit_folium import folium_static

    ## Create Map
    m = folium.Map(location=[56.1304, -106.3468],
                   tiles=map_styles['NatGeoWorldMap'][0],
                   attr=map_styles['NatGeoWorldMap'][1],
                   width='100%',
                   height='100%',
                   zoom_start=3, max_zoom=16, min_zoom=2,
                   )

    choropleth = folium.Choropleth(
        geo_data=gdf,
        data=df_gas_price_last_month,
        columns=(df_gas_price_last_month.index, 'last_month_avg'),
        nan_fill_color= 'grey',
        nan_fill_opacity=0.7,
        key_on='properties.prov_name_en',
        line_color='green',
        line_weight=2,
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        # legend_name=f'Last Month Avg Gas Prices {last_month_avg}',
        highlight=True
    )

    choropleth.geojson.add_to(m)
    choropleth.geojson.add_child(
        folium.features.GeoJsonTooltip(['prov_name_en', 'last_month_avg'], labels=False))

    colorscale.add_to(m)

    for i, latlng in enumerate(df_gas_prices_upcoming['lat_lng']):
        if df_gas_prices_upcoming.iloc[i,0]  == 'GTA':
            pass
        else:
            prov = df_gas_prices_upcoming.iloc[i, 4]
            flags_src = flags[prov]
            if 'Amount' in df_gas_prices_upcoming.columns:
                popup_text = folium.Popup(
                    html=f"""<center><img src= {flags_src} alt='Province Flag' width = '60', height = '30'><h4 style = 'font-family:montserrat;'><strong> {df_gas_prices_upcoming.iloc[i, 0].upper()}</strong></center></h4><center><h5 style = 'font-family:montserrat;'><strong> {t.strftime("%b %d, %y")}</strong></center></h5><h4 style = 'font-family:montserrat;'><center><strong><p style = 'color:{"#52382A" if df_gas_prices_upcoming.iloc[i, 10] == 0 else "#912D48" if df_gas_prices_upcoming.iloc[i, 10] > 0 else "#164c45"};'>{df_gas_prices_upcoming.iloc[i, 11]}</p>  ${df_gas_prices_upcoming.iloc[i, 8]}/L</strong></center></h4>""",
                    max_width=160, min_width=130)
            else:
                popup_text = folium.Popup(
                    html=f"""<center><img src = {flags_src} alt = 'Province Flag' width = '60', height = '30'> """,
                    max_width=160, min_width = 130
                )
            folium.Marker(location=[latlng[0], latlng[1]],
                          popup=popup_text,
                          tooltip=f"<strong>{df_gas_prices_upcoming.iloc[i, 0].upper()}</strong>",
                          icon=folium.Icon(color='darkblue', icon='car', prefix='fa')).add_to(m)

            html_to_insert = "<style>.leaflet-popup-content-wrapper, .leaflet-popup.tip {background-color:#c1ccbe !important;}</style>"
            m.get_root().header.add_child(folium.Element(html_to_insert))



    ## Save the map
    m.save('data/gas_prices.html')
    # st_map = st_folium(m, width = 1000, height = 700)
    folium_static(m, width=1300, height=750)