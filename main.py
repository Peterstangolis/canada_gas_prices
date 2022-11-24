## Importing my functions
from my_functions.date_functions import add_suffix


## Importing libraries
import datetime
import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st
import folium



# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Canadian Gas Prices", page_icon=":maple_leaf:")


def test_func():
    print(datetime.datetime.today().date())




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test_func()
    add_suffix()

