#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:03:09 2023

@author: derekfrost
"""

import pandas as pd
import pickle

# Create a sample dataframe
data = {'Name': ['John', 'Jane', 'Alice'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Save the dataframe to a file on a local drive using pickle
file_path = '/Users/derekfrost/Desktop/dataframe.pickle'  # Replace with your desired file path
with open(file_path, 'wb') as file:
    pickle.dump(df, file)
