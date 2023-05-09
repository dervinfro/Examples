#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 30 22:47:18 2021

@author: user

https://livecodestream.dev/post/how-to-use-generator-and-yield-in-python/
"""

import pandas as pd
import os

os.getcwd = os.getcwd()

os.listdir(path='.')

# Read in the path of the .CSV that I'll be using.
df = pd.read_csv('/Users/user/Desktop/CSV/gpslog7JUN.csv', header=None)

# Shape
dfShape = df.shape

# Head
dfHead = df.head(n=15)

# %% FOR df.iterrows
# FOR loop using df.iterrows
for index, rows in dfHead.iterrows():
    print('Index: ', index, '\n', rows[8], rows[9])


# %%
# Function that opens and returns yield for file_name
def csv_reader(file_name):
    for myrow in open(file_name, 'r'):
        yield myrow


# CSV Reader that reads in file and return Generator
csvGenerator = csv_reader('/Users/user/Desktop/CSV/gpslog7JUN.csv')

# Variable rowCount set to 0
rowCount = 0

# FOR loop for Generator, that returns the number of lines in file
for row in csvGenerator:
    rowCount += 1

# Output the rowCount
print('Row count is: {}'.format(rowCount))
