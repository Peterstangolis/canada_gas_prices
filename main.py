## Importing my functions
from my_functions.date_functions import add_suffix, todays_date, date_from_website


## Importing libraries
import datetime as dt
from datetime import timedelta
import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st
import folium


today, long_format_today, last_month = todays_date()
tomorrow_long_format = add_suffix()
date_from_gaswizard = date_from_website()

tomorrow = today + timedelta(days=1)

if date_from_gaswizard == tomorrow_long_format:
    t = tomorrow
else:
    t = today

print(date_from_gaswizard)
print(tomorrow_long_format)
print(t)

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Canadian Gas Prices", page_icon=":maple_leaf:")


def test_func():
    print(dt.datetime.today().date())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_func()
    print(add_suffix())

