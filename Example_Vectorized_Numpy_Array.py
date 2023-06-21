#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 22 14:17:38 2023

@author: derekfrost
"""

import numpy as np
import pandas as pd

# Create two arrays
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])

c = np.random.randint(0,100,10) # Output: array([43, 65, 54, 24,  2, 43,  5,  4, 18, 80])
d = np.random.randint(0, 100, 10) # Output: array([70, 10,  8, 43, 18, 82, 44, 58, 16, 71])

# Vectorized addition
result = a + b
print(result)  # Output: [ 7  9 11 13 15]

# Vectorized multiplication
result = a * b
print(result)  # Output: [ 6 14 24 36 50]

# Vectorized square root
result = np.sqrt(a)
print(result)  # Output: [1.         1.41421356 1.73205081 2.         2.23606798]

# Vectorized bool comparison
bool_result = c < d
print(bool_result)
# Output: array([ True, False, False,  True,  True,  True,  True,  True, False, False])


#%%

# Create sliding windows of size 2 for array1
window1 = np.lib.stride_tricks.sliding_window_view(c, window_shape=(2,))

# Iterate through each rolling window in array1 and compare with rolling single value from array2
comparison_list_comp = [all(window1[i] < d[i]) for i in range(len(window1))]

for i, window in enumerate(window1):
    comparison = all(window < d[i])
    print("Comparison [{}]: {} - {} < {}".format(i, comparison, window, d[i])) #pylint: disable=consider-using-f-string

#%%
# Create DataFrame and add columns C and D
df = pd.DataFrame({'C':c, 'D':d})

# The comp list is missing the last value.  Append np.nan to the list.
comparison_list_comp.append(np.nan)

# Add column to DataFrame
df['compare'] = comparison_list_comp
