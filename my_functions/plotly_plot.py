
from my_functions.dollar_oil_historical_prices import get_yahoo_data
from variables import oil_ticker, cad_usd_ticker


import pandas as pd
import streamlit as st

import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.express as px

import itertools
import datetime


## Plotly template setup
custom_template = {
    "layout": go.Layout(
        font={
            "family": "Nunito",
            "size": 14,
            "color": "#707070",
        },
        title={
            "font": {
                "family": "liberation serif",
                "size": 29,
                "color": "#F2E2C4",
            },
            "pad":{}
        },
        plot_bgcolor="#B3A791",
        paper_bgcolor="#B3A791",
        colorway=px.colors.qualitative.G10,
    )
}


def interactive_plot(fuel, location_type, location):

    ## retrieve the correct dataset
    if location_type == 'COUNTRY':
        df = pd.read_csv("data/hist_gas_canada.csv")
        if fuel == "Regular":
            df = df[df["Type of fuel"] == "Regular Unleaded"]
        elif fuel == "Premium":
            df = df[df["Type of fuel"] == "Premium Unleaded"]
        else:
            df = df[df["Type of fuel"] == "Diesel Fuel"]

    else:
        df = pd.read_csv("data/hist_gas_cities.csv")
        if fuel == "Regular":
            df = df[df["Type of fuel"] == "Regular Unleaded"]
        elif fuel == "Premium":
            df = df[df["Type of fuel"] == "Premium Unleaded"]
        else:
            df = df[df["Type of fuel"] == "Diesel Fuel"]
        if location_type == 'CITY':
            df = df[df["CITY"] == location]
        else:
            df = df[df["PROVINCE"] == location]

    df = df.reset_index(drop=True)
    if int((df["REF_DATE"][0].split("-")[1])) <= 22:
        year = "20" + str((df["REF_DATE"][0].split("-")[1]))
        y_diff = datetime.datetime.today().year - int(year)
    else:
        year = "19" + str((df["REF_DATE"][0].split("-")[1]))
        y_diff = datetime.datetime.today().year - int(year)

    ## Yahoo Data
    data = get_yahoo_data(oil_ticker, time_period=f"{y_diff}y", interval='1mo')
    data["mon_year"] = data.index.strftime("%b-%y")
    data["year"] = data.index.strftime("%Y")

    data_CAD_USD = get_yahoo_data(cad_usd_ticker, time_period=f"{y_diff}y", interval="1mo")
    data_CAD_USD["mon_year"] = data_CAD_USD.index.strftime("%b-%y")
    data_CAD_USD.reset_index(inplace=True)

    merged_df = pd.merge(df, data, left_on="REF_DATE", right_on="mon_year", how="left")
    merged_df.dropna(inplace=True)
    print("------")

    merged_df2 = pd.merge(merged_df, data_CAD_USD, left_on="REF_DATE", right_on="mon_year", how="left")
    merged_df2["oil_close_CAD"] = merged_df2["Close_x"] * merged_df2["Close_y"]
    merged_df2.dropna(inplace=True)
    merged_df2.reset_index(drop=True, inplace=True)

    ## Fuel Type text colors:
    r = '#70787D'
    p = '#CC2533'
    d = '#BDA523'

    c = r if fuel == "Regular" else p if fuel == 'Premium' else d

    fig2 = make_subplots(specs=[[{'secondary_y': True}]])

    # Add traces
    fig2.add_trace(
        go.Scatter(x=merged_df2['Date'], y=merged_df2["oil_close_CAD"].round(2),
                   name='Oil Price', line_color='#2C998B', yaxis='y1'),
        secondary_y=False,
    )

    fig2.add_trace(
        go.Scatter(x=merged_df2['Date'], y = (merged_df2['VALUE']/100).round(1),
                   name=f'{fuel} Gas Price', line_color=f'{c}', yaxis='y2'),
        secondary_y=True,
    )
    # Figure Title
    fig2.update_layout(
        title_text=f"Monthly <span style='color:#2C998B'> Oil </span> vs <span style='color:{c}'>{fuel}</span> Gas Prices in<span style='color:#CC2533'> $CAD</span> <br><span style = 'font-size:16px;' >{merged_df2.iloc[0]['REF_DATE']}  to {merged_df2.iloc[len(merged_df2) - 1]['REF_DATE']} in</span> <span style = 'text-transform:uppercase;color:#D9981E;font-size:18px;'>{location}</span>",
        template=custom_template
        # 'simple_white'
    )

    fig2.update_layout(
        yaxis1=dict(
            titlefont=dict(
                color='#2C998B'),
            tickfont=dict(
                color='#2C998B'
            )
        ),
        yaxis2=dict(
            titlefont=dict(
                color=f'{c}'
            ),
            tickfont=dict(
                color=f'{c}'
            )
        ),
        xaxis=dict(
            tickfont=dict(
                color='#F2E2C4'
            )
        )
    )
    fig2.update_xaxes(ticks="inside", tickwidth=1.5, tickcolor='#F2E2C4', ticklen=5, showline=True, linewidth=1,
                      linecolor='#F2E2C4')

    fig2.update_layout(yaxis_tickprefix='$')
    fig2.update_layout(yaxis2_tickprefix='$')

    fig2.update_xaxes(title_text="",
                      ticks="inside", tickwidth=1.5, tickcolor='#F2E2C4', ticklen=5, showline=True, linewidth=1,
                      linecolor='#F2E2C4')
    fig2.update_yaxes(title_text="Price of Crude Oil WTI",
                      ticks='inside', tickwidth=1.5, tickcolor='#2C998B', ticklen=7, showline=True, linewidth=1,
                      linecolor='#2C998B',
                      showgrid=True,
                      nticks = 6,
                      # gridwidth=0.3, gridcolor='grey',
                      range=[0, 170],
                      secondary_y=False)
    fig2.update_yaxes(title_text="Price of Gas /L",
                      ticks='inside', tickwidth=1.5, tickcolor=f'{c}', ticklen=7, showline=True, linewidth=1,
                      showgrid=False,
                      tick0=.50,
                      tickformat='.2f',
                      secondary_y=True)

    fig2.update_layout(legend=dict(
        orientation="h",
        entrywidth=100,
        yanchor="bottom",
        y=.85,
        xanchor="center",
        x=.5,
        bgcolor = "#232533"
    ))

    st.plotly_chart(fig2)