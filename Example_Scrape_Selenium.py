#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 23:15:30 2021

@author: user
"""


import requests
import urllib.request
import pandas as pd
import os
import html5lib
import codecs

from lxml import etree
from bs4 import BeautifulSoup
from selenium import webdriver

pd.options.display.max_columns=None
pd.options.display.max_rows=None

processed_path = '/Users/user/Downloads/Python_Data/processed_data'

# Site URL
url = 'https://coinmarketcap.com/exchanges/coinbase-exchange/'

#%% First Iteration of Scraping

# Make a GET request to fetch the raw content
page = requests.get(url)

soup = BeautifulSoup(page.text)

print(soup.find(class_='table'))

#%% Scraping using alt version
# https://towardsdatascience.com/data-science-skills-web-scraping-javascript-using-python-97a29738353f

# Other page alternate
page_alt = urllib.request.urlopen((url))

# Other soup alternate
soup_alt = BeautifulSoup(page_alt, 'html.parser')

# Find all the Table Tags
table = soup_alt.find_all('table')

# Output
print(soup_alt.find_all('table'))

# Path to bittrex .RTF that contains HTML Markdown
# I pulled this HTML file directly from the browser in dev mode.
# bittrex_table = '/Users/user/Downloads/Python_Data/raw_data/bittrex_table_allcoins_19OCT2021.rtf'
binance_table = '/Users/user/Downloads/Python_Data/raw_data/binace_table_allcoins_22OCT2021.rtf'
coinmarketcap_table = '/Users/user/Downloads/Python_Data/raw_data/market_cap_top100_23OCT2021.rtf'
coinmarketcap_table1 = '/Users/user/Downloads/Python_Data/raw_data/market_cap_101_to_200_23OCT2021.rtf'

# Open file with Codecs
file = codecs.open(coinmarketcap_table1, 'r', 'utf-8')

# Read File
content = file.read()

# Use BeautifulSoup to parse HTML file
soup = BeautifulSoup(content, 'html.parser')

# Find all the Table Tags
table = soup.find_all('table')

# Read the Table Tags string into a dataframe
df = pd.read_html(str(table))[0]

# Output DataFrame to csv
df.to_csv('/Users/user/Downloads/Python_Data/raw_data/market_cap_100_200coins_25OCT2021.csv')


#%% Selenium Scraping
# https://stackoverflow.com/questions/45259232/scraping-google-finance-beautifulsoup/45259523#45259523
# https://sites.google.com/chromium.org/driver/

browser = webdriver.Chrome(executable_path='/Users/user/Downloads/chromedriver')

browser.get(url)

html_source = browser.page_source

browser.quit()

soup = BeautifulSoup(html_source, 'lxml')

# cols for cryptobubbles.net
# cols = ['Rank','Name','Price','Market Cap','24h',' Volume','Hour','Day',
#         'Week','Month','Year','Actions']


table = soup.find_all('table')

df = pd.read_html(str(table))[0]

# For coinmarketcap -> coinbase_exchange
# Match the entire word of USD.
df_temp = df[df['Pair'].str.contains(r'\bUSD\b')]

# Drop the index
df_temp.reset_index(drop=True, inplace=True)

# Final output
df_temp[['#','Currency']].to_csv('/Users/user/Downloads/Python_Data/raw_data/coinbase_ONLY_USD_coins_13DEC2021.csv')

# Output data to CSV





# month = [x for x in df["Month"]]

# df.Month = df.Month.str.strip('%')

# make it numeric
# df['Month'] = df.Month.str.strip('%')

# save rank and name columsn to CSV
# The names will be used in other API call code.
# I want to pass a list of crypto names in the API call.

# df[['Rank','Name']].to_csv(os.path.join(processed_path,'crypto_rank_name.csv'),
#                            index=False)


























