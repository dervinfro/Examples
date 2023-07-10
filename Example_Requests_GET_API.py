#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 14:27:20 2023

@author: derekfrost
"""
"""
This is an example of a cleaner way to break down the Binance URL API
SEE (crypto_binance_api.py).  
This method breaks up the URL into interval, limit and symbols.
Cleaner way to do things given that it is easily scalable in the future...
...other params, symbols, etc.


"""
import requests
import datetime


# noinspection PyGlobalUndefined
def get_klines_data(trading_pair):
    base_url = 'https://api.binance.us/api/v3/klines'
    interval = '1s'
    limit = '1'

    global data

    for symbol in trading_pair:
        params = {
            'symbol': symbol,
            'interval': interval,
            'limit': limit
        }

        response = requests.get(base_url, params=params)
        data = response.json()

        # Process the response data here
        # For example, you can print the symbol and the first kline
        print(f"Symbol: {symbol}")
        print("First Kline:")
        print(data[0])
        print()


# Example usage with an array of symbols
symbols = ['BTCUSDT', 'ETHUSDT', 'LTCUSDT']
get_klines_data(symbols)

# Output the POSIX value that comes from the .JSON data.
# Also...output the datetime conversion of that POSIX value
# noinspection PyUnboundLocalVariable
print('Print POSIX from data .JSON: {}\
 and POSIX converted: {}'.format(data[0][0], datetime.datetime.fromtimestamp(data[0][0] / 1000)))
