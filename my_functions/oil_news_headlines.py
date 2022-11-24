
from my_functions.date_functions import todays_date, last_month_year_current
from variables import oil_ticker



import yfinance as yf
import time
import pytz
from datetime import datetime
from pytz import timezone


## Variable setup
eastern = timezone('US/Eastern')
fmt = '%b %d, %Y %#I:%M%p %Z'

# 1. Function to get the latest oil headlines from yfinance
def oil_headlines():
    today, full_day, last_month = todays_date()
    oil_yf = yf.Ticker(oil_ticker)
    headline_title = f"\U0001F4F0 Oil News For {full_day} \U0001F4F0"
    headlines = dict()

    for n in range(len(oil_yf.news)):
        key = 'Article' + '_' + str(n)
        title = oil_yf.news[n]['title']
        link = oil_yf.news[n]['link']
        source = oil_yf.news[n]['publisher']

        t = time.strftime(fmt, time.localtime(oil_yf.news[n]["providerPublishTime"]))
        article_date_time = t
        try:
            image_link = oil_yf.news[n]['thumbnail']['resolutions'][0]['url']
            headlines[key] = [title, link, source, image_link, article_date_time]
        except:
            image_link = ""
            headlines[key] = [title, link, source, image_link, article_date_time]

    return headline_title, headlines
