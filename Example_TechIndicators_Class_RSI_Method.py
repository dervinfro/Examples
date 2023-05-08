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

# Generate random integers between 10 and 1000
rand_ints = np.random.randint(low=10, high=1001, size=100)

# Create a DataFrame with one column containing the random integers
df = pd.DataFrame(rand_ints, columns=["values"])

# Reset the index
df.reset_index(drop=True, inplace=True)

# Define a list of category names
category_names = ["fruit", "animal", "color", "city"]

# Add a new column containing randomly chosen categories
df["Names"] = np.random.choice(category_names, size=len(df))

# Sort on Name and ensure that the index is ignored and not sorted.
df.sort_values('Names', ignore_index=True, inplace=True)

# Define the TechIndicators class
class TechIndicators:
    def __init__(self, df):
        self.df = df
    
    """
    When we define instance methods (RSI is the method in this example)  in a class, 
    we don't need to include the self parameter in the method's arguments, 
    since Python automatically passes the instance as the first argument.
    """ 
    def RSI(self, close_price: pd.Series, periods: int):
        
        # Calculate the price difference between the current and previous day
        delta = close_price.diff()
        
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
    
    # To view the output of repr: repr(tech_indicators)
    def __repr__(self):
        return "{}".format(self.df)

    # To view the output of str: str(tech_indicators)
    def __str__(self):
        return "{}".format(self.df)

# Create a Class instance of the TechIndicators class
tech_indicators = TechIndicators(df)

# Group the DataFrame by the "Names" column and apply the RSI method to the "values" column for each group
rsi_df = df.groupby("Names")["values"].apply(lambda x: tech_indicators.RSI(x, periods=3))

# Pass the values of the rsi_df series into a 'RSI' column in the df.
df['RSI'] = rsi_df.values

# Display the resulting DataFrame
print(df)
