#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 21:51:27 2021

@author: user

Slope: https://www.engineeringtoolbox.com/slope-degrees-gradient-grade-d_1562.html
Angle: https://arrayjson.com/numpy-angle/
"""

import numpy as np
import pandas as pd
import time
import seaborn as sns
import matplotlib.pyplot as plt

#%% Set Crypto Values and Date increments

# Crypto Value 1: Create 100 linear values and raise ^ 2
power_val = [x**2 for x in np.linspace(0,5,100)]

# Crypto Value 2: Create 100 linear values and raise ^ 2
power_val2 = [x**2 for x in np.linspace(1,3,100)]

# Date value ranging in 15 minute increments.
fifteen_range = list(pd.date_range(start='1/1/2021',
                                  periods = 100,
                                  freq = '15min'))

#%% Create DataFrame and columns
df = pd.DataFrame()

# Create dataframe columns from the above values and date increments
df['power_val'] = power_val
df['power_val2'] = power_val2
df['15min_range'] = fifteen_range


#%% Melt New DataFrame and plot in Seaborn

# Create df two and melt the values into the date range.
# Melting data is required to properly plot multiple data set on seaborn.
df_two = pd.melt(df, 
                 id_vars=['15min_range'], 
                 value_vars=['power_val','power_val2'])

# Graph out a line plot with the melted DataFrame
sns.lineplot(x = '15min_range', 
             y ='value', 
             hue = 'variable', 
             data = df_two)

#%% Display DataFrame and Query value crossover

# For loop and output value columns and boolean comparison.
for x in range(len(df)):
    # if df['power_val'][x] == df['power_val2'][x]:
    #     print('{},{},{}'.format('MATCH',
    #                           df['power_val'][x],
    #                           df['power_val2'][x]))
    # else:
    #     pass
    print(df['power_val'][x],
          df['power_val2'][x], 
          df['power_val'][x] < df['power_val2'][x])
    time.sleep(0.2)

#%% Build function to show slope of each line
    
# Find the X value and Y value
X = df['15min_range'].iloc[-4:]
Y = df['power_val2'].iloc[-4:]
Z = df['power_val'].iloc[-4:]

x = [1,2,3,4]
y = [1,2,3,4]

sns.scatterplot(data=df, x='15min_range', y='power_val2')

# Output a graph that shows 4 values of: time and powerval2
plt.xticks(rotation=45)
plt.scatter(df['15min_range'].iloc[-5:], df['power_val2'].iloc[-5:])

print('{} {}'.format(df['power_val2'].iloc[-4:].diff(),
                     df['power_val2'].iloc[-4:]))

#%% Solution for slope and degrees
"""
Each X increment in my graph is 15 minutes, which is equivilant to one time
series increment.
So....the X increment is always 1.

Y increment will be the difference of the Y Series (SEE: Series.diff())
Example:
    
Y = df['power_val2'].iloc[-4:]

Y
Out[84]: 
96    8.640037
97    8.759208
98    8.879196
99    9.000000
Name: power_val2, dtype: float64

Y.diff()
Out[85]: 
96         NaN
97    0.119172
98    0.119988
99    0.120804
Name: power_val2, dtype: float64

Example: np.angle(X + Yj, deg=True)

np.angle(1 + 0.119172j, deg=True)
Out[110]: 6.795973881572169

My final thought for the night....I will use .diff() to find my Y value;
assuming my .diff() default period will be 1, my X value will also be 1.

Once I have the .diff() value, I will use .angle() to output a degree.

Both the .diff() and the .angle() will be values for each row.
    
"""





