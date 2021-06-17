#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 17 23:25:21 2021

@author: user
"""

import pandas as pd

pd.options.display.max_columns=None
pd.options.display.max_rows=None

df = pd.read_csv('/Users/user/Downloads/ML Analytics/ML Analytics - Course 2/Wrightsample.csv')

'''
# The commented code below exists in this example so that I have a baseline reference as to 
what the dataframes can be filtered for.
north = df[df['TREATB']=='North']
sorth = df[df['TREATB']=='South']
outer = df[df['TREATB']=='Outside']
'''

# Searching for a case insensitive string value of 'nor' in the df['TREATB']
df_contains = df[df['TREATB'].str.contains('nor', case=False)]