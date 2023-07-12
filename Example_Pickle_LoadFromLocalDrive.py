#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 16:04:20 2023

@author: derekfrost
"""

import pickle

# Load the dataframe from a file on a local drive
file_path = '/Users/derekfrost/Desktop/dataframe.pickle'  # Replace with the actual file path
with open(file_path, 'rb') as file:
    df = pickle.load(file)

# Display the loaded dataframe
print(df)
