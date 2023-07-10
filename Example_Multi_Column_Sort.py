#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 23:10:55 2023

@author: derekfrost
See this for full workup: 
/Users/derekfrost/Projects/examples/Examples/Example_NumpyTile_DataFrameFilterCondition.py
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Set seed for reproducibility
np.random.seed(42)

# Generate random integers for bbupper, Close, and Open
bbupper_values = np.random.randint(50, 100, size=90)
close_values = np.random.randint(50, 100, size=90)
open_values = np.random.randint(50, 100, size=90)

# Create the dataframe
df = pd.DataFrame({
    'bbupper': bbupper_values,
    'Close': close_values,
    'Open': open_values
})

# Create the 'Candle' column based on the condition of 'Close' being greater than 'Open'
df['Candle'] = np.where(df['Close'] > df['Open'], 'Green', 'Red')

num_intervals = 30

# Add the 'trading_pair' column with three different categories: BTC, ADA, and SOL
categories = ['BTC', 'ADA', 'SOL']
np.random.shuffle(categories)
df['trading_pair'] = np.tile(categories, len(df) // len(categories))

# Sort the trading_pair before inserting the timeseries
# Failure to do this will result in mismatched trading_pair & timeseries data
df.sort_values('trading_pair', inplace=True)

# Refactor the 'timeseries' column for each category in 'trading_pair'
# Set the start time
start_time = pd.Timestamp.now().floor('5min')
# Set the timeseries using date_range.  NOTE: the -5min interval.
timeseries = pd.date_range(start=start_time, periods=num_intervals, freq='-5min', inclusive='left')
# Reverse the timeseries so that when it's applied to .tile, the most recent time 
# ...will be the categories most recent record.
timeseries = timeseries[::-1]
# Use numpy tile to iterate timeseries for each of the trading_pair categories
df['timeseries'] = np.tile(timeseries, 3)

# Multip Column sort
sorted_df = df.sort_values(by=['trading_pair', 'timeseries'], key=lambda x: x.map({col: i for i, col in enumerate(categories)}))