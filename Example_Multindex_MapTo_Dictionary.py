#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 12:41:05 2023

@author: derekfrost
"""

# Show all columns and rows


import pandas as pd
import numpy as np

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Create the trading pairs and date range
trading_pairs = ['Pair A', 'Pair B', 'Pair C', 'Pair D']
start_date = pd.Timestamp('2023-01-01')
end_date = start_date + pd.DateOffset(days=4)
dates = pd.date_range(start=start_date, end=end_date, freq='D')

# Create the multi-index
multi_index = pd.MultiIndex.from_product([trading_pairs, dates], names=['trading pair', 'date'])

# Create the Series with random values
np.random.seed(42)
series_values = np.random.randn(len(multi_index))
series = pd.Series(series_values, index=multi_index, name='values')

# Print the multi-indexed Series
print(series)


# Create the date range
start_date1 = pd.Timestamp('2023-01-01')
end_date1 = start_date + pd.DateOffset(days=4)
dates1 = pd.date_range(start=start_date, end=end_date1, freq='D')

#%%

import pandas as pd
import numpy as np

# Set the number of rows for each trading_pair
rows_per_pair = 5

# Create a date range with day intervals
dates1 = pd.date_range(start='2023-01-01', periods=rows_per_pair, freq='D')

# Create an empty list to store the DataFrames
dfs = []

# Iterate over each trading_pair
for pair in trading_pairs:
    # Create a DataFrame with index as dates and trading_pair column
    df = pd.DataFrame(index=dates, columns=['trading pair'])
    
    # Assign the trading_pair to the DataFrame
    df['trading pair'] = pair
    
    # Add a column of random integer values
    df['Values'] = np.random.randint(100, 1000, size=len(df))
    
    # Append the DataFrame to the list
    dfs.append(df)

# Concatenate the DataFrames
df = pd.concat(dfs)

# Print the DataFrame
print(df)

# Rename index column
df.rename_axis('date', inplace=True)

# df1 = pd.merge(series.reset_index(), df.reset_index(), on='Date')
# df1 = df.merge(series.reset_index(), left_on=['Date', 'Trading_Pair'], right_on=['Date', 'Trading Pair'])
df1 = df.merge(series.reset_index(), left_index=True, right_on=['date', 'trading pair'])


# Reset the index of the Series to match the DataFrame column
series_reset = series.reset_index()

# Merge the DataFrame with the Series based on index and column values
merged_df = df.merge(series.reset_index(), left_index=True, right_on=['date', 'trading pair'])

# Print the merged DataFrame
print(merged_df)




