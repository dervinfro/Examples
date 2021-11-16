#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 22:30:15 2021

@author: user
"""
# =============================================================================
# This module is a test of the SMA25 using the BTCUSDT historic data .
# The data used was in 15 minute increments.
# 4SEPT - Compare against TradingView graph for method confirmation
# =============================================================================
import pandas as pd
import numpy as np
import os 

import matplotlib.pyplot as plt

pd.options.display.max_columns=None


base_path = '/Users/user/Downloads/Python_Data/raw_data/Binance_BTCUSDT/'

path_list = [os.path.join(base_path, file_path) 
             for file_path in os.listdir(base_path)]

cols = ['Open_time','Open','High','Low','Close','Volume','Close_time',
        'Quote_asset_volume','Number_of_trades',
        'Taker_buy_base_asset_volume','Taker_buy_quote_asset_volume','Ignore']

#%% Create dataframes and clean up date/time columns

# Set dataframe and concat in all the CSV files
df = pd.concat((pd.read_csv(file_path, names=cols) 
                for file_path in path_list))

# Date columns are in milliseconds...convert them
df['Close_time'] = pd.to_datetime(df['Close_time'], unit='ms')
df['Open_time'] = pd.to_datetime(df['Open_time'], unit='ms')

# Change the 'astype' for each datetime column 
# get rid of the values beyond seconds
df['Close_time'] = df['Close_time'].astype('datetime64[s]')
df['Open_time'] = df['Open_time'].astype('datetime64[m]')

# I only want to work the Close value for each 15m increment
close = df['Close']

# Change the index value of the 'close' variable
close.index = df['Close_time']

# Sort index values so that they plot properly
close = close.sort_index()

# This single line computes the SMA25
sma25 = close.rolling(window=25).mean()

# Plot Data
plt.style.use('fivethirtyeight')

plt.figure(figsize = (12,6))

plt.plot(close, label='BTCUSDT Adj Close')
plt.plot(sma25, label='SMA25')
plt.xlabel('Date')
plt.ylabel('ADJ Close')
plt.legend()
plt.show()
