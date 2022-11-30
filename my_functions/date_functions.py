
## A python file that contains a number of functions to return various dates required throughout the project

from variables import url_gaswizard, url_statscan

from datetime import date, timedelta, datetime

import pandas as pd
import requests
from bs4 import BeautifulSoup
import datetime as dt



# 1. the following functions returns todays_date, a formatted version of todays date, and last_months date
def todays_date():
    return datetime.today().date(), datetime.today().date().strftime("%A %B %#d, %Y"), (
                datetime.today().date() - pd.offsets.DateOffset(months=1)).date()


# 2. The function adds a suffix (i.e. 'th') to the end of tomorrows date
def add_suffix():
    today, full_day, last_month = todays_date()

    tomorrow = today + timedelta(days=1)
    two_days_ahead = today + timedelta(days=2)
    day = tomorrow.day
    two_days = two_days_ahead.day
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]

    if 4 <= two_days <= 20 or 24 <= two_days <= 30:
        suffix_2 = "th"
    else:
        suffix_2 = ["st", "nd", "rd"][day % 10 - 1]

    tomorrow_long_format = tomorrow.strftime(f"%A %#d{suffix} of %B %Y")
    two_days_ahead_long_format = two_days_ahead.strftime(f"%A %#d{suffix_2} of %B %Y")
    return tomorrow_long_format, two_days_ahead_long_format

# 3. This fuinction returns the date from 1 month ago (vs today) in 'mon-yy' format
def last_month_year_current():
    today, full_day, last_month = todays_date()
    return last_month.strftime("%b-%y")


# 4. This function gets the date gaswizard.ca has been updated
def date_from_website():
    source = requests.get(url_gaswizard).text
    soup = BeautifulSoup(source, 'html.parser')
    t = soup.find('div', class_ = 'price-date').text
    website_date = t[t.find('for ')+4:]

    website_date_list = website_date.split(" ")
    week_day, day_num, month_name, long_year = website_date_list[0], ''.join(filter(str.isdigit, website_date_list[1])), \
                                               website_date_list[3], website_date_list[4]
    website_date_formatted_a = month_name + " " + day_num + ", " + long_year
    website_date_formatted = dt.datetime.strptime(website_date_formatted_a, "%B %d, %Y")

    return website_date


# 5. Returns the date statscan site has been updated
def stats_can_updated_date():
    source = requests.get(url_statscan).text
    soup = BeautifulSoup(source, 'html.parser')
    # text = soup.find('div', class_= 'col-md-8 mrgn-btm-0 mrgn-lft-0 divLeft').text
    para = soup.find('div', class_='col-md-8 mrgn-btm-0 mrgn-lft-0 divLeft')
    for p in para:
        if len(p.text) > 1:
            text = p.text.strip()
            stats_can_updated = (text[text.find('date:') + 5:text.find('date') + 37]).strip()
            return stats_can_updated