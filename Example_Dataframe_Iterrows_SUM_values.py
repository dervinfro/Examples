#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 13:14:44 2021

@author: user
"""

import pandas as pd

pd.options.display.max_columns=None
pd.options.display.max_rows=None
pd.options.display.width=135
#pd.options.display.float_format='{:.3f}'.format

df = pd.read_csv('/Users/user/Downloads/ML Analytics/ML Analytics - Course 3/quiz2data.csv')

# Shape
dfShape = df.shape

# Head
dfHead = df.head(15)

print("LINE",end = "NEXT")

#%% FOR Loop df.iterrows

# FOR loop using df.iterrows
# NOTE: The SUM function requires the integers to be added INSIDE a set of "()"
# ie sum((1,2)) NOT sum(1,2)....missing the double set of parans in the latter example
for index, rows in dfHead.iterrows():
    y = rows['class']
    z = rows['major_class']
    print(index)
    print(y, z, rows['class']+rows['major_class'], sum((rows['class'],rows['major_class'])))
    # print('Index: ', index, '\n', sum(rows['class'], rows['major_class']))
    
    
