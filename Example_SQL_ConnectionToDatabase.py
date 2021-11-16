#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 21:38:49 2021

@author: user

NOTE: https://docs.python.org/3/library/sqlite3.html
"""

import pandas as pd
from sqlite3 import connect
from numpy.random import randint

#%% Set data1 and data2 to random variables to be used in the Dataframe
data1 = randint(100,200,10)
data2 = randint(10,50,10)

df = pd.DataFrame([data1,data2]).T

#%% 
conn = connect('/Users/user/Desktop/history.sqlite')

cur = conn.cursor()

# Example of iterator to loop through History Table
for row in cur.execute('SELECT * FROM HISTORY'):
    print(row)
    
# cur.execute Object used with fetchmany Method
Query = cur.execute('SELECT * FROM HISTORY')
print(Query.fetchmany(size=10))
