#!/usr/bin/env python

import os
import sys
from datetime import datetime
from urllib.parse import urljoin

from bs4 import BeautifulSoup
import requests
import pandas as pd

main_url = "https://coinmarketcap.com"
coin_list_path = "/all/views/all/"
data_path = "historical-data/?start=20130428&end=%s" % (datetime.now().strftime("%Y%m%d"))

page = requests.get(urljoin(main_url, coin_list_path))

soup = BeautifulSoup(page.text, "lxml")

coins = soup.tbody.findAll("tr")

print("Found", len(coins), "coins")

def get_coin(coin_url):
    coin_page = requests.get(coin_url)

    # Convert the data into a data frame and
    # make sure dates are parsed and
    # column names are clean
    df = pd.read_html(coin_page.text, parse_dates=[0], na_values='-')[0]
    column_names = ["".join(column.lower().split()) for column in df.columns]
    df.columns = column_names

    return df

count = 0

for coin in coins:
    columns = coin.findAll("td")
    name = columns[1]["data-sort"]
    symbol = columns[2].text
    url = columns[1].a["href"]

    count += 1
    print(count, symbol, name)

    filename = os.path.join("data", symbol + ".pickle")

    if os.path.exists(filename):
        continue

    try:
        coindata = urljoin(main_url, url + data_path)
        data = get_coin(coindata)

        data.to_pickle(filename)
    except Exception as e:
        print(e, file=sys.stderr)
