#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:51:55 2021

@author: user
https://school.stockcharts.com/doku.php?id=technical_indicators:moving_averages
https://stackoverflow.com/questions/37924377/does-pandas-calculate-ewm-wrong
https://newbedev.com/pandas-ema-not-matching-the-stock-s-ema
"""

import pandas as pd
import numpy as np

# Show all rows and columns
pd.options.display.max_rows=None
pd.options.display.max_columns=None

# Read CSV from two different datasets (BTC and ETH)
df_btc = pd.read_csv('/Users/user/Downloads/bitcoin_price_historical.csv')
df_eth = pd.read_csv('/Users/user/Downloads/ethereum_price_historical.csv')

# Create a new column for each dataframe.  
# This is required when I append dataframes, I'll be able to see which records
# belong to which coins
df_btc['coin'] = 'BTC'
df_eth['coin'] = 'ETH'

# Append ETH to the BTC dataframe
df = df_btc.append(df_eth)

# Create Simple Moving Average of 25
rolling = df.groupby('coin')['Close'].rolling(window=25).mean()

# Create Simple Moving Average of 25 - return an array of values
rolling_values = df.groupby('coin')['Close'].rolling(window=25).mean().values


# Create a column in the dataframe with the rolling window
df['sma25'] = df.groupby('coin')['Close'].rolling(window=25).mean().values
df['sma50'] = df.groupby('coin')['Close'].rolling(window=50).mean().values

# Create Exp Moving Average - return an array of values
ewm = df.groupby('coin')['Close'].ewm(span=20).mean().values

# Create a column in the dataframe with the exp. moving average
df['ema20'] = df.groupby('coin')['Close'].ewm(span=20).mean().values


#%% EMA Test Section

link_csv = pd.read_excel('/Users/user/Downloads/Python_Data/raw_data/cs-movavg.xls', header=1)


# The following code setups the EMA variable

# Confirm head value
link_csv['Price'].head(15)

# Set span variable for the SMA
span = 10

# Simple Moving Average
# windows is the size of the moving window, in this case 10.
# [:span] indicates to show the first 10 values of the Simple Moving Average
sma = link_csv['Price'].rolling(window=span).mean()[:span]

sma_all = link_csv['Price'].rolling(window=span).mean()


# IMPORTANT: This passes in the actual Price values to use in the EWM algo
rest = link_csv['Price'][span:]

# =============================================================================
'''
The reason why the method below works is that it takes the actual Close price
into account for the Exp. Moving Average.  The reason why my code was not working,
when I was passing in the entire SMA Series is that that code no longer contains
actual Close prices, it contains the SMA prices.  The concat method works by taking
the first 10 calculated values and putting them a Series with the size of the 
span/window.  See span value of 10.
The other portion of the concat is going to take into account the remaining Close
prices after the initial 10 span/window values.  By passing in the first calcuated 
AND the remainder of the actual Close values, this is how the .ewm function 
properly calculates the EMA.
'''
# =============================================================================
ewm_value = round(pd.concat([sma,rest]).ewm(span=span, adjust=False).mean(),2)






















