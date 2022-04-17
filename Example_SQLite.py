#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
https://towardsdatascience.com/python-pandas-and-sqlite-a0e2c052456f

Created on Sun Nov 14 00:38:45 2021

@author: user

SQLite: Call in data from JSON -> output to dataframe
"""

import sqlite3
import pandas as pd
import requests

#%% Call the API and choose second list element
countries_api_request = requests.get('http://api.worldbank.org/countries?format=json&per_page=100')
countries = countries_api_request.json()[1]

# Create the dataframe and pipe in JSON data
df = pd.json_normalize(countries)

# Create SQLite connection
conn = sqlite3.connect('/Users/user/Downloads/Python_Data/raw_data/database/worldbank_countries.db')

# Pandas to_sql and pass in dataframe to connection
df.to_sql('worldbank_countries',conn, if_exists='append')

# Example query
df_query = pd.read_sql('SELECT * FROM worldbank_countries', conn)
