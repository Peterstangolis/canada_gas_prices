
## from my_functions

from date_functions import date_from_website, todays_date
from variables import map_styles, flags
from next_day_gas_prices_canada import clean_next_day_gas_prices_can
from clean_statscan_hist_gas_prices_canada import clean_hist_gas_can




from datetime import date, timedelta, datetime

import branca.colormap
import pandas as pd
import ast
import pathlib
import geopandas as gpd
import folium
import branca.colormap as cm
from branca.colormap import linear


today, long_format_today, last_month = todays_date()
tomorrow_long_format = add_suffix()
date_from_gaswizard = date_from_website()

tomorrow = today + timedelta(days=1)

if date_from_gaswizard == tomorrow_long_format:
    t = tomorrow
else:
    t = today

clean_hist_gas_can()
clean_next_day_gas_prices_can()
#clean_geo_data()