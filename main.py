## Importing my functions
from my_functions.date_functions import add_suffix, todays_date, date_from_website
from my_functions.oil_news_headlines import oil_headlines



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

headline_title, headlines = oil_headlines()

# SETTING PAGE CONFIG TO WIDE MODE AND ADDING A TITLE AND FAVICON
st.set_page_config(layout="wide", page_title="Canadian Gas Prices", page_icon=":maple_leaf:")


## Inital Page Title of Streamlit APP
title = f"<h4 style = 'font-size:55px; color:#F2E2C4; FONT-FAMILY:liberation serif;'> TOMORROW'S GAS PRICES IN CITIES ACROSS <mark style = 'font-family:liberation serif; font-size:55px; color:#CC2533; background-color: transparent;'>CANADA</mark></h4>"



## Oil Headline News Sections ==========================================================================================
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(f"<h3 style='color:#F2E2C4; font-size:45px; text-align: left;'>📰 LATEST OIL NEWS</h3>", unsafe_allow_html=True)
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Program Running:")


