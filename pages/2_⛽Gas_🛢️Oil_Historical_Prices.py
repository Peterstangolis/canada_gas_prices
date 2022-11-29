
from my_functions.date_functions import todays_date, date_from_website

from variables import oil_ticker, cad_usd_ticker, periods
from my_functions.dollar_oil_historical_prices import retrieve_historical_pricing, hist_gas_can, current_can_mean_gas
from my_functions.plotly_plot import interactive_plot

from my_functions.clean_statscan_hist_gas_prices_canada import clean_hist_gas_can


import pandas as pd
import streamlit as st

## initial variable setup
yest_open_oil, yest_close_date_oil, oil_hist_prices = retrieve_historical_pricing(oil_ticker)
yest_open_usd_cad, yest_close_date_cad_usd, cad_usd_hist_rates = retrieve_historical_pricing(cad_usd_ticker)

## dictionary of gas prices from 1, 5, 10, 15 years
can_hist_gas_prices = hist_gas_can()

## Getting the current mean Regular Gas price based on tomorrows gas prices across Canada
current_can_mean_gas_price = round((current_can_mean_gas()/100),2)

## Getting the last Close prices for the exchange of USD to CAD
yest_USD_CAD_close = f"{cad_usd_hist_rates['period_1d']}"

yest_close_oil_price_CAD = round(oil_hist_prices['period_1d'] * cad_usd_hist_rates['period_1d'],2)
yest_open_oil_price_CAD = round(yest_open_oil * cad_usd_hist_rates['period_1d'], 2)
d = round(yest_close_oil_price_CAD - yest_open_oil_price_CAD,1 )

yest_close_oil_price_CAD = round(oil_hist_prices['period_1d'] * cad_usd_hist_rates['period_1d'],2)
yest_open_oil_price_CAD = round(yest_open_oil * cad_usd_hist_rates['period_1d'], 2)
d = round(yest_close_oil_price_CAD - yest_open_oil_price_CAD,1 )

## Getting historical USD to CAD exchange rates, returns the last full months mean rate
one_year_USD_CAD_close = round(cad_usd_hist_rates["period_1y"] * oil_hist_prices["period_1y"], 2)
five_year_USD_CAD_close = round(cad_usd_hist_rates['period_5y'] * oil_hist_prices['period_5y'],2)
ten_year_USD_CAD_close = round(cad_usd_hist_rates['period_10y'] * oil_hist_prices['period_10y'],2)

today_1, full_day, present_last_month = todays_date()

one_year_ago = present_last_month - pd.offsets.DateOffset(years=1)
five_years_ago = present_last_month - pd.offsets.DateOffset(years=5)
ten_years_ago = present_last_month - pd.offsets.DateOffset(years=10)

#date_from_gaswizard_formatted
date_from_gaswizard  = date_from_website()
print(f"Date from gaswizard.ca {date_from_gaswizard}")


## Streamlit APP Setup
st.set_page_config(layout="wide", page_title="Canadian Gas Prices", page_icon=":maple_leaf:")

## Setting Session States
if 'fuel_type' not in st.session_state:
    st.session_state.fuel_type = 'Regular'

if 'city_prov' not in st.session_state:
    st.session_state.city_prov = 'COUNTRY'

title = f"<h4 style = 'font-size:50px; color:#F2E2C4; FONT-FAMILY:liberation serif;'> A Glimpse of <mark style = 'font-family:liberation serif; font-size:55px; color:#2C998B; background-color: transparent;'>OIL</mark> & <mark style = 'font-family:liberation serif; font-size:55px; color:#BDA523; background-color: transparent;'>GAS</mark> Prices in \
        <mark style = 'font-family:liberation serif; font-size:55px; color:#CC2533; background-color: transparent;'>$CAD</mark>  </h4>"


st.markdown(f"{title}", unsafe_allow_html = True)
st.markdown("<br>", unsafe_allow_html=True)
st.caption(
        f"The USD crude oil price was converted to CAD utilizing the exchange rate at close for time period represented",
        unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)

col5, col6, col7, col8 = st.columns(4)
st.markdown("<br>", unsafe_allow_html=True)

st.caption(f"")

st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

with col1:
    #st.subheader(f"{yest_close_date_cad_usd}")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#2C998B;' >", unsafe_allow_html=True)
    st.metric(label = "OIL", value = f"${yest_close_oil_price_CAD}", delta = f"{d:.2f}", delta_color='inverse')
    st.caption(f"{yest_close_date_oil}")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#164C45;' >", unsafe_allow_html=True)
    st.caption(
        f"{yest_close_date_cad_usd}: <mark style = 'color:#9FC131;'>${yest_USD_CAD_close}</mark>",
        unsafe_allow_html=True)

with col2:
    # st.subheader("1 YEAR")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#2C998B;' >", unsafe_allow_html=True)
    st.metric(label="OIL", value=f"${one_year_USD_CAD_close}", delta=None)
    st.caption(f"1 YEAR")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#164C45;' >", unsafe_allow_html=True)

    st.caption(
        f"{one_year_ago:%b-%Y}: <mark style = 'color:#9FC131;'>${cad_usd_hist_rates['period_1y']}</mark>",
        unsafe_allow_html=True)

with col3:
    #st.subheader("5 YEAR")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#2C998B;' >", unsafe_allow_html=True)

    st.metric(label = "OIL", value = f"${five_year_USD_CAD_close}", delta = None)
    st.caption(f"5 YEAR")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#164C45;' >", unsafe_allow_html=True)

    st.caption(
        f"{five_years_ago:%b-%Y}: <mark style = 'color:#9FC131;'>${cad_usd_hist_rates['period_5y']}</mark>",
        unsafe_allow_html=True)

with col4:
    #st.subheader("10 YEAR")
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#2C998B;' >", unsafe_allow_html=True)
    st.metric(label = "OIL", value = f"${ten_year_USD_CAD_close}", delta = None)
    st.caption(f"10 YEAR")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#164C45;' >", unsafe_allow_html=True)

    st.caption(
        f"{ten_years_ago:%b-%Y}: <mark style = 'color:#9FC131;'>${cad_usd_hist_rates['period_10y']}</mark>",
        unsafe_allow_html=True)

## ===================   FIRST 4 COLUMNS  ======================================= ##

with col5:
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)
    st.metric(label = "GAS", value = f"${current_can_mean_gas_price}/L", delta = None)
    st.caption(f"{yest_close_date_oil}")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)

with col6:
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)
    st.metric(label="GAS", value=f"${round(can_hist_gas_prices['Oct-2021'] / 100, 2)}/L", delta=None,
              delta_color='inverse')
    st.caption(f"Oct-2021")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)

with col7:
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)
    st.metric(label = "GAS", value = f"${round(can_hist_gas_prices['Oct-2017']/100,2)}/L", delta = None)
    st.caption(f"Oct-2017")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)

with col8:
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)
    st.metric(label = "GAS", value = f"${round(can_hist_gas_prices['Oct-2012']/100,2)}/L", delta = None, delta_color='inverse')
    st.caption(f"Oct-2012")
    st.markdown("<hr style ='width:40%;text-align:left;height:4px;background-color:#BDA523;' >", unsafe_allow_html=True)

## ========================================    NEXT 4 COLUMNS   =================================================== ##



### SIDEBAR START

with st.sidebar:
    st.markdown("<br>",unsafe_allow_html=True)
    with st.expander(label="ADDITIONAL CHART OPTIONS", expanded=False):
        st.markdown("<br>", unsafe_allow_html=True)
        ## Fuel type radiobutton
        st.markdown("<br>", unsafe_allow_html=True)
        ## City, Province, Country radiobutton
        st.radio(
            "SELECT LOCATION TYPE",
            ['COUNTRY', 'PROVINCE', 'CITY'],
            key = 'city_prov',
            horizontal=True
        )

        if st.session_state.city_prov in ['PROVINCE', 'CITY']:
            df_city_prov = pd.read_csv('data/hist_gas_cities.csv')
            choices = df_city_prov[st.session_state.city_prov].unique()
            d = False
        else:
            if st.session_state.city_prov == 'COUNTRY':
                df_can = pd.read_csv('data/hist_gas_canada.csv')
                d = True
                choices = df_can["CITY"].unique()
                st.session_state.fuel_type = 'Regular'


        st.markdown("<br>", unsafe_allow_html=True)
        option = st.selectbox(
            "SELECT TO VIEW HISTORICAL PRICES FOR",
            (choices),
            disabled = d
        )
        if option.strip().upper() == 'ONTARIO PART':
            st.markdown(f"Ontario part represents <mark style='color:#D9981E;'>OTTAWA-GATINEAU</mark> region.",
                        unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        st.radio(
            'SELECT FUEL TYPE',
            ['Regular', 'Premium', 'Diesel'],
            key='fuel_type',
            horizontal=True,
            disabled=d
        )

## PLOTLY PLOT
interactive_plot(st.session_state.fuel_type, st.session_state.city_prov, option)




st.markdown("<br>", unsafe_allow_html=True)
col9, col10, col11, col12 = st.columns([0.5,3,3,1])
with col9:
    st.write(" ")
with col10:
    with st.expander(label='🖱️ CLICK TO VIEW MORE INFO ABOUT CRUDE OIL PRICING', expanded=False):
        st.markdown("[PLACEHOLDER]")
with col11:
    with st.expander(label=" CLICK TO VIEW INFO ABOUT GAS PRICING PRICING", expanded=False):
        st.markdown("[PLACEHOLDER]")
with col12:
    st.write(" ")