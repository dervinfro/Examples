#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created on Wed May 10 22:58:53 2023
# @author: derekfrost

import pandas as pd
import numpy as np
from crypto_class_tech_indicators import TechIndicators

# Show all columns and rows
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', None)

# Create a list of four random nouns
nouns = np.random.choice(['apple', 'book', 'car', 'dog'], size=100)

# Create a list of 100 random prices between 100 and 1000
prices = np.random.randint(low=100, high=1000, size=100)

# Create a list of 100 random prices between 100 and 1000
bb_upper_price = np.random.randint(low=100, high=1000, size=100)

# Create a pandas DataFrame with two columns: "name" and "price"
df = pd.DataFrame({'name': nouns, 'price': prices, 'upper_bb':bb_upper_price})

# Sort on Name and ensure that the index is ignored and not sorted.
df.sort_values('name', ignore_index=True, inplace=True)

# Reset the index
df.reset_index(drop=True, inplace=True)

# This will take the current price and "shift" it down one value to the next cell
# ..and this will be appended into the "prev_price" column
df['prev_price'] = df.groupby('name')['price'].shift(1)
"""
Test if all elements in the array meet the True/False condition
...for this condition to test True, all elements need to return as True.
...we can accomplish this using .all()
...pass in the above code with a condition (ie: < or >, etc)
ie: 
df['price'].iloc[df.shape[0]-2:].values
RETURN: array([614, 637])

all(df['price'].iloc[df.shape[0]-2:].values < 625)
RETURN: False
    
https://stackoverflow.com/questions/31099561/test-if-all-elements-of-a-python-list-are-false
"""

######################################################################
 #### List Comprehension in conjunction with Exception Handling  ####
######################################################################

# https://www.geeksforgeeks.org/how-to-handle-a-python-exception-in-a-list-comprehension/

# This function will accept one input var.  In this case it will accept the df.index
# The test return is df['price'] and +1
# If there is a KeyError, it will return the df['price'] and not error on out the missing key

# helper function
def two_compare(a):
	try:
		return df['price'][a], df['price'][a] + 1
	except KeyError:
		return df['price'][a], None
    
# List comprehension 
two_compare_output = [two_compare(x) for x in range(len(df))]

######################################################################
 ## Compare the Values of SMA to the two relative values of Price ##
######################################################################

# Build an SMA based on each of the groups...use .groupby function
# Price groupedby Name and Transformed using the Mean
# A much cleaner way to populate the SMA based on each group.
df['sma'] = df['price'].groupby(df['name']).transform('mean')


# Re-arrange the layout of the columns
df = df[['name', 'price','prev_price', 'sma', 'upper_bb']]

# Create a new column called 'upper_bb'
# Use the SMA and the Map Function using Lambda, to generate random values
# Have those random values be a product of SMA...to create an Upper BB that is 
# above the SMA
# This is NOT a True Upper BB value.  It was only used as an example in my test DataFrame
df['upper_bb'] = df['sma'].map(lambda x: x * np.random.uniform(1.1, 1.7))

# This creates a column called Compare
# Using numpy logical_and...I've compared the price/prev_price if it's less than SMA.
df['compare'] = np.logical_and(df['price'] < df['sma'], df['prev_price'] < df['sma'])

# Only show the rows with a True value in df['compare']
# To find False: df.loc[~df['compare'].values]
df.loc[df['compare'].values]

# New Test Ground for Class
ti = TechIndicators(df)

# Output the Class Method to a Series that shows the < Condition.
df['compare'] = ti.twogreens_ti(df['price'], df['sma'], df)


