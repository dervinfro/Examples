#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul  9 06:23:26 2023

@author: derekfrost
"""

import pandas as pd
import numpy as np

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

# Define a function to filter the condition for each rolling window
def filter_condition(group):
    return group[(group['Candle'] == 'Green') & (group['Close'] > group['bbupper'])]

# Define the last hour that will be used for filtering the DataFrame 
last_hour = start_time - pd.Timedelta(hours=1)

# Set the filter
filtered_df = filter_condition(df)

# Filtering out the DataFrame that only shows the condition within the last hour
filtered_df[filtered_df['timeseries'] > last_hour]

# Get the latest row for each trading_pair
latest_rows = filtered_df.groupby('trading_pair').tail(1)


