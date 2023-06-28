#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 00:46:06 2023

@author: derekfrost
"""
"""
******************************************************
This code was assisted using ChatGPT on May6 @ 1:00 AM
******************************************************
"""


import pandas as pd
import numpy as np

# Show all columns and rows
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Create a list of four random nouns
nouns = np.random.choice(['apple', 'book', 'car', 'dog'], size=100)

# Create a list of 100 random prices between 100 and 1000
prices = np.random.randint(low=100, high=1000, size=100)

# Create a pandas DataFrame with two columns: "name" and "price"
df = pd.DataFrame({'name': nouns, 'price': prices})

# Sort on Name and ensure that the index is ignored and not sorted.
df.sort_values('name', ignore_index=True, inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

#%%
# Define the TechIndicators class
class TechIndicators:
    def __init__(self, df):
        self.df = df
    
    """
    When we define instance methods (RSI is the method in this example)  in a class, 
    we don't need to include the self parameter in the method's arguments, 
    since Python automatically passes the instance as the first argument.
    """ 
    def RSI(self, price: pd.Series, periods: int):
        
        # Calculate the price difference between the current and previous day
        delta = price.diff()
        
        # Calculate the gain and loss on each day, where gain is positive price changes and loss is negative price changes
        gain = delta.where(delta > 0, 0)
        loss = -delta.where(delta < 0, 0)
        
        # Calculate the average gain and loss over a rolling window of 'periods' days
        avg_gain = gain.rolling(window=periods).mean()
        avg_loss = loss.rolling(window=periods).mean()
        
        # Calculate the relative strength (RS) as the ratio of the average gain to the average loss
        rs = avg_gain / avg_loss
        
        # Calculate the relative strength index (RSI) as 100 minus 100 divided by 1 plus the RS
        rsi = 100 - (100 / (1 + rs))
        
        # Return the RSI values as a pandas series
        return rsi
    
    def BollingerBands(self, price: pd.Series, window: int):
        # Set the 'price' column of the dataframe to the values passed in as an argument
        self.price = price
        
        # Calculate the rolling mean and standard deviation of the price over a window of 'window' days
        rolling_mean = self.price.rolling(window=window).mean()
        rolling_std = self.price.rolling(window=window).std()
        
        # Calculate the upper, average and lower Bollinger Bands as the rolling mean plus or minus the rolling standard deviation
        upper_band = rolling_mean + 2 * rolling_std
        avg_band = rolling_mean
        lower_band = rolling_mean - 2 * rolling_std
        
        # Return the upper, average and lower Bollinger Bands as a pandas DataFrame
        """
        The magic sauce for the line of code below is to use the pd.concat.
        Without pd.concat, the results were not being saved as a DataFrame with 
        three seperate BB columns.  An interesting note here is that pd.concat created
        a MultiIndex of "name" and "index.value".  I need to look into this.
        """
        return pd.concat([upper_band, lower_band, avg_band], axis=1, \
                         keys=['bb_upper','bb_lower','bb_sma'])

    
    # To view the output of repr: repr(tech_indicators)
    def __repr__(self):
        return "{}".format(self.df)

    # To view the output of str: str(tech_indicators)
    def __str__(self):
        return "{}".format(self.df)

#%%
# Create a Class instance of the TechIndicators class
ti = TechIndicators(df)

# Group the DataFrame by the "Names" column and apply the RSI method to the "values" column for each group
rsi_df = df.groupby("name")["price"].apply(lambda x: ti.RSI(x, periods=3))

# Pass the values of the rsi_df series into a 'RSI' column in the df.
df['RSI'] = rsi_df.values

# Group the DataFrame by name and apply the BollingerBand() method to each group
grouped_df = df.groupby('name').apply(lambda x: ti.BollingerBands(x['price'], 5))

# this line takes the values from the grouped_df and saves them to the df with the column keys
df[['bb_upper','bb_lower','bb_sma']] = grouped_df.values


# Display the resulting DataFrame
print(df.head())
