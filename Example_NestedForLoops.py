#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 24 22:12:06 2021

@author: user
"""

import pandas as pd
import timeit

startTime = timeit.default_timer()

nested_list = [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]

nested_list[0].index

flatList = []

for x in nested_list:
    for item in x:
        flatList.append(item)
    
print(flatList)

#%%
# Sample data of nested dicts within nested lists
data = [[{'col_1': 3, 'col_2': 'a'}, {'col_1': 7, 'col_2': 'z'} ],
        [{'col_1': 2, 'col_2': 'b'}],
        [{'col_1': 1, 'col_2': 'c'}],
        [{'col_1': 0, 'col_2': 'd'}]]

# Create list to append to show the output
dataFlatList = []

# Use nested FOR loops to loop through nested dicts/lists
for x in data:
    for item in x:
        dataFlatList.append(item)
        
print(dataFlatList)

# use dual brackets to display nested list/dict objects.
data[0][1]

# Show time of section execution
print('Time: ', timeit.default_timer() - startTime)

#%%
data1 = [{'col_1': 3, 'col_2': 'a'},
        {'col_1': 2, 'col_2': 'b'},
        {'col_1': 1, 'col_2': 'c'},
        {'col_1': 0, 'col_2': 'd'}]

df = pd.DataFrame(data1)


    



