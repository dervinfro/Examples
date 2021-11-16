#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 16:47:14 2021

@author: user

https://towardsdatascience.com/understand-map-function-to-manipulate-pandas-series-8ac340d514f7
"""

import numpy as np
import pandas as pd

# Create Series with a list of integers
pd_series = pd.Series([1,3,5,7,9])

# Map function using Lambda to perform square
series_map = pd_series.map(lambda x: x ** 2)

# Make a function that inputs a number 
# ..and passes product of input number and random integer
def we_random(anumber):
    ran_value = np.random.randint(1,100,1)
    return anumber * ran_value

# Map function using defined function
series_map_random = pd_series.map(we_random)

# Create dataframe merging (merge) all of the series.map outputs
df = pd.concat([pd_series, series_map, series_map_random],  axis=1)

# Columns renamed for the sake of renaming...nothing to do with Series.map
df = df.rename(columns={0:'a', 1:'b', 2:'c'})
    
# Append Series map to DataFrame
df['d'] = pd_series.map(lambda x: x ** 3)
