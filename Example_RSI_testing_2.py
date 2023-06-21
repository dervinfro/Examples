#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 21:34:49 2023

@author: derekfrost
"""

import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

class RSI:
    def __init__(self, dataframe):
        self.df = dataframe
    
    def calculate_rsi(self, close_price, period):
        # Calculate price difference and gain/loss
        price_diff = close_price.diff()
        gain = price_diff.clip(lower=0)
        loss = -1 * price_diff.clip(upper=0)
        
        # Calculate average gain and loss over the specified period
        avg_gain = gain.rolling(window = period, min_periods = period).mean()
        avg_loss = loss.rolling(window = period, min_periods = period).mean()
        
        # Calculate initial RS and RSI
        rs = avg_gain / avg_loss
        rsi = 100 - (100 / (1 + rs))
        
        return rsi

# Generate example dataframe (as in the previous code)
start_date = pd.Timestamp('2023-01-01')
end_date = start_date + pd.DateOffset(days=99)
dates = pd.date_range(start=start_date, end=end_date, freq='D')
np.random.seed(42)
close_prices = np.random.randint(1, 100, size=100).astype('f')
data = {'Date': dates, 'Close Price': close_prices}
df = pd.DataFrame(data)

# Create an instance of the RSI class with the dataframe
rsi_calculator = RSI(df)

# Call the calculate_rsi method with example values
close_price = df['Close Price']
period = 14  # Example period
rsi_value = rsi_calculator.calculate_rsi(close_price, period)

# Print the calculated RSI value
print("RSI:", rsi_value)
