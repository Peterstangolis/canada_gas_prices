## Importing my functions
from my_functions.date_functions import add_suffix, todays_date, date_from_website
from my_functions.oil_news_headlines import oil_headlines
from my_functions.next_day_gas_prices_canada import clean_next_day_gas_prices_can
from my_functions.clean_statscan_hist_gas_prices_canada import clean_hist_gas_can
from my_functions.geo_data_cleaning import clean_geo_data
from my_functions.map_creation import folium_map



## Importing libraries
import datetime as dt
from datetime import timedelta
import pandas as pd
from bs4 import BeautifulSoup
import streamlit as st
import folium


last_month_date_of_avg_gas_price = clean_hist_gas_can()
clean_next_day_gas_prices_can()
clean_geo_data()

today, long_format_today, last_month = todays_date()
tomorrow_long_format, two_days_ahead_long_format = add_suffix()
date_from_gaswizard = date_from_website()

tomorrow = today + timedelta(days=1)
two_days_ahead = today + timedelta(days=2)

if date_from_gaswizard == tomorrow_long_format:
    t = tomorrow
elif date_from_gaswizard == two_days_ahead_long_format:
    t = two_days_ahead
else:
    t = today
print(t)


headline_title, headlines = oil_headlines()

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Canadian Gas Prices", page_icon=":maple_leaf:")

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{min-width: 15rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{min-width: 15rem;}}
    </style>
''',unsafe_allow_html=True)


with open('style.css') as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


## Inital Page Title of Streamlit APP
title = f"<h4 style = 'font-size:40px; color:#F2E2C4; FONT-FAMILY:liberation serif;'> UPCOMING GAS PRICES IN CITIES ACROSS <mark style = 'font-family:liberation serif; font-size:41px; color:#CC2533; background-color:transparent;'>CANADA</mark></h4>"


st.markdown(f"{title}", unsafe_allow_html=True)
st.markdown(f"<h4 style='color:#F2E2C4; font-size:25px;'> Select  the <mark style = 'color:#0076A9; background-color:transparent; font-size: 29px;'> BLUE </mark> icon to view the prices for <mark style = 'color:#B5C2C9; background-color:transparent; font-size: 28px;'> REGULAR </mark> gas in your city </h4>", unsafe_allow_html = True)
st.markdown(f"<h4 style='color:#F2E2C4; font-size:20px;'> Moving your cursor over a province will reveal the average price of REGULAR gas for {last_month_date_of_avg_gas_price} </h4>", unsafe_allow_html = True)

folium_map()

st.markdown("<hr>", unsafe_allow_html=True)

## Oil Headline News Sections ==========================================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:#F2E2C4; font-size:41px; text-align: left;'>📰 LATEST OIL NEWS</h3>", unsafe_allow_html=True)
st.markdown(f"<p style = 'color:#F2E2C4; font-size:18px; font-family: inter light; text-align: left;'> {today:%A %B %d, %Y} </p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
middle_article = int(round(len(headlines.keys())/2, 0))

col1, col2, col3 = st.columns([3,.3,3], gap='small')
headline_keys = list(headlines.keys())


with col1:
    for i in range(middle_article):
        key = headline_keys[i]
        st.markdown(f"<p style = 'font-size:18px;font-family:liberation serif;color:white;'>{headlines[key][0]}</p>",
                    unsafe_allow_html=True)
        st.markdown(f"<span style = 'color:#0076A9;font-size:12px;'> {headlines[key][2]} </span> <span style = 'color:lightgrey;font-size:13px;'> | {headlines[key][4]} </span> ", unsafe_allow_html=True)
        if len(headlines[key][3]) > 2:
            #st.image(f'{headlines[key][3]}', width=100)
            image_link = f"<a href='{headlines[key][1]}'><img src='{headlines[key][3]}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
            st.markdown(f"{image_link}", unsafe_allow_html=True)
        else:
            website_image = 'https://images.unsplash.com/photo-1523995462485-3d171b5c8fa9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80'
            image_link = f"<a href='{headlines[key][1]}'><img src= '{website_image}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
            st.markdown(f"{image_link}", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)

with col2:
    st.write(" ")

with col3:
    for i in range(middle_article, len(headline_keys)):
        key = headline_keys[i]
        st.markdown(f"<p style = 'font-size:18px;font-family:liberation serif;color:white;'> {headlines[key][0]}</p>", unsafe_allow_html=True)
        st.markdown(f"<span style = 'color:#0076A9;font-size:12px;'> {headlines[key][2]} </span> <span style = 'color:lightgrey;font-size:13px;'> | {headlines[key][4]} </span> ", unsafe_allow_html=True)
        if len(headlines[key][3]) > 2:
            #st.image(f'{headlines[key][3]}', width=140)
            image_link = f"<a href='{headlines[key][1]}'><img src='{headlines[key][3]}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
            st.markdown(f"{image_link}", unsafe_allow_html=True)
        else:
            website_image = 'https://images.unsplash.com/photo-1523995462485-3d171b5c8fa9?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=735&q=80'
            image_link = f"<a href='{headlines[key][1]}'><img src= '{website_image}' alt = 'article image' style = 'width:190px;height:120px; border: 2px solid lightgrey;border-radius:10px;'></a>"
            st.markdown(f"{image_link}", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)


with st.sidebar:
    st.markdown("<br>", unsafe_allow_html=True)
    df = pd.read_excel("data/tomorrow_gasprices_canadiancities_latlng.xlsx")
    cities = df["City"].unique().tolist()
    location_selector = st.selectbox(
        "SELECT A CANADIAN CITY FROM DROPDOWN",
        cities
    )
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(f"<mark style = 'color:#F2E2C4;background-color:clear;font-family:liberation serif;font-size:16px;'> GAS PRICES ON {t:%A %B %#d, %Y} IN: </mark>", unsafe_allow_html=True)
    st.markdown(f"<mark style= 'background-color:clear;text-align:center;font-size:20px;;color:#261C25;font-family:liberation serif;font-weight:bold; background-image: linear-gradient(to right, #70787Dcc, #CA4D57cc, #BDA523cc); text-transform:uppercase; border-radius: 6px; padding: 10px 10px;letter-spacing:.2rem;'>{location_selector}</mark>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    #position: relative; left:50px;top:10px;right:50px;

    df_temp = df[df["City"] == location_selector].reset_index()

    col5, col6, col7 = st.sidebar.columns(3, gap='small')
    with col5:
        st.markdown("<hr style ='width:95%;text-align:left;height:3px;background-color:#B5C2C9;' >", unsafe_allow_html=True)
        st.markdown("<p style='color:#B5C2C9; font-weight:bold; font-family:liberation serif;letter-spacing:.1rem;'> REGULAR</p>", unsafe_allow_html=True)
        if int(df_temp._get_value(0, 'Amount')) == 0:
            color = 'off'
        else:
            color = 'inverse'
        st.metric(label="", value=df_temp._get_value(0, 'Regular'), delta=int(df_temp._get_value(0, 'Amount')), delta_color=color)
    with col6:
        st.markdown("<hr style ='width:95%;text-align:left;height:3px;background-color:#CC2533;' >",
                    unsafe_allow_html=True)
        st.markdown("<p style='color:#CC2533; font-weight:bold; font-family:liberation serif;letter-spacing:.1rem;'> PREMIUM</p>", unsafe_allow_html=True)
        premium_list = df_temp["Premium"].str.split(" ")[0]
        premium_price = premium_list[0]
        if len(premium_list) == 2:
            amount = 0
            color = 'off'
        else:
            symbol = premium_list[1]
            amount = premium_list[2]
            color = 'inverse'
        st.metric(label="", value = float(premium_price) , delta = amount, delta_color= color)
    with col7:
        st.markdown("<hr style ='width:95%;text-align:left;height:3px;background-color:#BDA523;' >",
                    unsafe_allow_html=True)
        st.markdown("<p style='color:#BDA523; font-weight:bold; font-family:liberation serif;letter-spacing:.1rem;'> DIESEL</p>", unsafe_allow_html=True)

        diesel_list = df_temp["Diesel"].str.split(" ")[0]
        diesel_price = diesel_list[0]

        if len(diesel_list) == 2:
            amount = 0,
            color = 'off'
            st.metric(label="", value=float(diesel_price), delta=amount[0], delta_color=color)
        else:
            symbol = diesel_list[1]
            amount = diesel_list[2]
            color = 'inverse'
        #print(diesel_price, amount[0], color)
            st.metric(label="", value=float(diesel_price), delta=amount, delta_color=color)


    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr>", unsafe_allow_html=True)
    #st.markdown("<br>", unsafe_allow_html=True)

st.sidebar.markdown("<br>", unsafe_allow_html=True)

with st.sidebar.expander(label='🖱 CLICK TO REVEAL DATA SOURCES USED IN DASHBOARD', expanded=False):
    st.caption("The gas prices have been retrieved from www.gaswizard.ca. <br> \
    The historical gas prices in 🇨🇦 have been obtained from https://www150.statcan.gc.ca/t1/tbl1/en/tv.action?pid=1810000101\n\
    Updated USD to CAD rates along with CRUDE OIL prices were obtained using the yfinance package https://pypi.org/project/yfinance/")


# if __name__ == '__main__':
#     print("Program Running:")
#     clean_hist_gas_can()
#     clean_next_day_gas_prices_can()
#     clean_geo_data()
#     print("End of program")


