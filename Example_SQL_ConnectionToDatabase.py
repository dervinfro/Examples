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
import timeit

#%% Set data1 and data2 to random variables to be used in the Dataframe
data1 = randint(10000,20000,10000)
data2 = randint(1000,5000,10000)

df = pd.DataFrame([data1,data2]).T

#%% History SQLite (Timer)

start_time = timeit.default_timer()
# conn = connect('/Users/user/Desktop/history.sqlite')
conn = connect('/Volumes/user/Desktop/history.sqlite')


cur = conn.cursor()

# Example of iterator to loop through History Table
for row in cur.execute('SELECT * FROM HISTORY'):
    print(row)
    
# cur.execute Object used with fetchmany Method
Query = cur.execute('SELECT * FROM HISTORY')
print(Query.fetchmany(size=1))
print(timeit.default_timer() - start_time)

#%% Crypto Project (Timer)
start_time = timeit.default_timer()

conn = connect('/Volumes/database/crypto_project.db')

cur = conn.cursor()

conn.close()

# Use the cur.execute Objec with the crypto_project.db
Query = cur.execute("SELECT * FROM \
            (SELECT * FROM crypto_project ORDER BY last_updated DESC LIMIT 5400)\
                ORDER BY last_updated ASC")
                
print(Query.fetchmany(size=1))

                
print(timeit.default_timer() - start_time)


