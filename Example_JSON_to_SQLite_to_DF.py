#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 27 00:59:24 2021

@author: user
"""

# Use crypto JSON data with a scheduler

import sqlite3
import pandas as pd
import sched
import time

from requests import Session
from IPython.display import clear_output


#%% Crypto API Setup

# Setup the Crypto API calls
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start':'1',
    'limit':'100',
    'convert':'USD'
    }

headers = {
    'Accept':'application/json',
    'Accept-Encoding':'deflate, gzip',
    'X-CMC_PRO_API_KEY':'0b685b4c-fe2d-4bbd-8f0a-40c30cdb4087'
    }

session = Session()
session.headers.update(headers)

#%% SQL Connection

# Create sqlite3 connection - This does not need to be in the While Loop
conn = sqlite3.connect('/Users/user/Downloads/Python_Data/raw_data/database/crypto_project.db')

#%% Crypto Function and Schedule

# Set the scheduler
scheduler = sched.scheduler(time.time, time.sleep)

print('Start Time: {}'.format(time.ctime()))

# create crypto calls function
def save_to_database(url, parameters):
    print('Time: {}'.format(time.ctime()))
    
    # Crypto session get - pass in URL and parameters
    response = session.get(url, params=parameters)
    
    # Retreive data using the .json method
    j = response.json()
    
    # Import JSON data into DataFrame
    df = pd.json_normalize(j['data'])
    
    # There is a dtype that SQLite does not like.
    # To fix that, change all dtypes to 'str'
    df = df.applymap(str)
    
    # Import DataFrame to SQLite3 Database
    df.to_sql('crypto_project', conn, if_exists='append', index=False)
    
    

# Infinite Loop that will forever iterate over the schedule.
def infinite_loop():
    while True:
        
        # Query the database
        df_query = pd.read_sql('SELECT * FROM crypto_project', conn)
         
        # Query shape
        print(df_query.shape)
        
        
        # Run every 30 seconds, with a priority of 1 (ignore this for now),
        # ..pass in the crypto_calls function and the arguments
        scheduler.enter(30, 1, save_to_database, argument=(url, parameters))
        
        # Run the scheduler
        scheduler.run()


infinite_loop()


    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    