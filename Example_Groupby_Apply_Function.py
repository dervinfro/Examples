#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 22:53:15 2022

@author: derekfrost
"""

# https://stackoverflow.com/questions/68518403/pandas-how-to-return-multiple-columns-with-a-custom-apply-function-on-a-groupby

import pandas as pd

# Show all columns and rows
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

#%% Create DataFrame

df = pd.DataFrame(data_000)

headers = df.iloc[0]
df = df.iloc[1:]
df.columns = headers


#%% Set Index

# Set the index to the last_updated date/time field
df.index = df.last_updated

#%% Test Function

# Create a test function that can be passed into the groupby lambda

def test_func(price, window):
    sma = price.rolling(window).mean()  # <- Simple Moving Average
    stdev = price.rolling(window).std()  # <- Standard Deviation
    return pd.concat([sma, stdev], axis=1, keys=['sma','stdev'])


#%% Groupby line of code

# This line of code creates a groupby on name, which creates a multi index function
# It then applies a lambda to a Function.
# Function takes in the df.close Series and the window (14)
# Output is two columns (SMA and STDEV) with a multi index.
df.groupby('name').apply(lambda x: test_func(x.close, 14))

