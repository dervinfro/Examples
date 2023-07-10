#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:43:39 2023

@author: derekfrost
"""

import requests
import datetime as dt
import numpy as np
import time
import asyncio
import aiohttp
import nest_asyncio
import pandas as pd

#%%
resp = requests.get('https://api.binance.us/api/v3/klines?interval=5m&limit=1&symbol=BTCUSD')

print(resp.json())

print(dt.datetime.utcfromtimestamp(1687148100000 / 1000))
print(dt.datetime.utcfromtimestamp(1687148399999 / 1000))

#%% trading_pair_array cell
trading_pair_array1 = np.array(['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'LTCUSDT', 'BNBUSDT', 'ADAUSDT',
       'BATUSDT', 'ETCUSDT', 'XLMUSDT', 'ZRXUSDT', 'DOGEUSDT', 'ATOMUSDT',
       'NEOUSDT', 'VETUSDT', 'QTUMUSDT', 'ONTUSDT', 'KNCUSDT', 'VTHOUSDT',
       'COMPUSDT', 'MKRUSDT', 'ONEUSDT', 'BANDUSDT', 'STORJUSDT',
       'UNIUSDT', 'SOLUSDT', 'EGLDUSDT', 'PAXGUSDT', 'OXTUSDT', 'ZENUSDT',
       'FILUSDT', 'AAVEUSDT', 'GRTUSDT', 'SHIBUSDT', 'CRVUSDT', 'AXSUSDT',
       'AVAXUSDT', 'CTSIUSDT', 'DOTUSDT', 'YFIUSDT', '1INCHUSDT',
       'FTMUSDT', 'USDCUSDT', 'MATICUSDT', 'MANAUSDT', 'ALGOUSDT',
       'LINKUSDT', 'EOSUSDT', 'ZECUSDT', 'ENJUSDT', 'NEARUSDT', 'OMGUSDT',
       'SUSHIUSDT', 'LRCUSDT', 'LPTUSDT', 'NMRUSDT', 'SLPUSDT', 'ANTUSDT',
       'CHZUSDT', 'OGNUSDT', 'GALAUSDT', 'TLMUSDT', 'SNXUSDT',
       'AUDIOUSDT', 'ENSUSDT', 'REQUSDT', 'APEUSDT', 'FLUXUSDT',
       'COTIUSDT', 'VOXELUSDT', 'RLCUSDT', 'BICOUSDT', 'API3USDT',
       'BNTUSDT', 'IMXUSDT', 'FLOWUSDT', 'GTCUSDT', 'THETAUSDT',
       'TFUELUSDT', 'OCEANUSDT', 'LAZIOUSDT', 'SANTOSUSDT', 'ALPINEUSDT',
       'PORTOUSDT', 'RENUSDT', 'CELRUSDT', 'SKLUSDT', 'VITEUSDT',
       'WAXPUSDT', 'LTOUSDT', 'FETUSDT', 'BONDUSDT', 'LOKAUSDT',
       'ICPUSDT', 'TUSDT', 'OPUSDT', 'ROSEUSDT', 'CELOUSDT', 'KDAUSDT',
       'KSMUSDT', 'ACHUSDT', 'DARUSDT', 'RNDRUSDT', 'SYSUSDT', 'RADUSDT',
       'ILVUSDT', 'LDOUSDT', 'RAREUSDT', 'LSKUSDT', 'DGBUSDT', 'REEFUSDT',
       'ALICEUSDT', 'FORTHUSDT', 'ASTRUSDT', 'BTRSTUSDT', 'GALUSDT',
       'SANDUSDT', 'BALUSDT', 'GLMUSDT', 'CLVUSDT', 'TUSDUSDT', 'QNTUSDT',
       'STGUSDT', 'AXLUSDT', 'KAVAUSDT', 'APTUSDT', 'MASKUSDT',
       'BOSONUSDT', 'PONDUSDT', 'MXCUSDT', 'JAMUSDT', 'TRACUSDT',
       'PROMUSDT', 'DIAUSDT', 'LOOMUSDT', 'STMXUSDT', 'BTCUSD', 'ETHUSD',
       'BCHUSD', 'LTCUSD', 'USDTUSD', 'BNBUSD', 'ADAUSD', 'BATUSD',
       'ETCUSD', 'XLMUSD', 'ZRXUSD', 'LINKUSD', 'RVNUSD', 'DASHUSD',
       'ZECUSD', 'ALGOUSD', 'IOTAUSD', 'WAVESUSD', 'ATOMUSD', 'NEOUSD',
       'QTUMUSD', 'ICXUSD', 'ENJUSD', 'ONTUSD', 'ZILUSD', 'VETUSD',
       'XTZUSD', 'HBARUSD', 'OMGUSD', 'MATICUSD', 'EOSUSD', 'DOGEUSD',
       'KNCUSD', 'VTHOUSD', 'USDCUSD', 'COMPUSD', 'MANAUSD', 'MKRUSD',
       'DAIUSD', 'ONEUSD', 'BANDUSD', 'STORJUSD', 'UNIUSD', 'SOLUSD',
       'EGLDUSD', 'PAXGUSD', 'OXTUSD', 'ZENUSD', 'FILUSD', 'AAVEUSD',
       'GRTUSD', 'SUSHIUSD', 'ANKRUSD', 'CRVUSD', 'AXSUSD', 'AVAXUSD',
       'CTSIUSD', 'DOTUSD', 'YFIUSD', '1INCHUSD', 'FTMUSD', 'NEARUSD',
       'LRCUSD', 'LPTUSD', 'NMRUSD', 'SLPUSD', 'ANTUSD', 'XNOUSD',
       'CHZUSD', 'OGNUSD', 'GALAUSD', 'TLMUSD', 'SNXUSD', 'AUDIOUSD',
       'REQUSD', 'APEUSD', 'FLUXUSD', 'COTIUSD', 'VOXELUSD', 'RLCUSD',
       'BICOUSD', 'API3USD', 'ENSUSD', 'BNTUSD', 'IMXUSD', 'FLOWUSD',
       'GTCUSD', 'THETAUSD', 'TFUELUSD', 'OCEANUSD', 'LAZIOUSD',
       'SANTOSUSD', 'ALPINEUSD', 'PORTOUSD', 'RENUSD', 'CELRUSD',
       'SKLUSD', 'VITEUSD', 'WAXPUSD', 'LTOUSD', 'FETUSD', 'BONDUSD',
       'LOKAUSD', 'ICPUSD', 'TUSD', 'OPUSD', 'ROSEUSD', 'CELOUSD',
       'KDAUSD', 'KSMUSD', 'ACHUSD', 'DARUSD', 'RNDRUSD', 'SYSUSD',
       'RADUSD', 'ILVUSD', 'LDOUSD', 'RAREUSD', 'LSKUSD', 'DGBUSD',
       'REEFUSD', 'ALICEUSD', 'FORTHUSD', 'ASTRUSD', 'BTRSTUSD', 'GALUSD',
       'SANDUSD', 'BALUSD', 'POLYXUSD', 'GLMUSD', 'CLVUSD', 'TUSDUSD',
       'QNTUSD', 'STGUSD', 'AXLUSD', 'KAVAUSD', 'APTUSD', 'MASKUSD',
       'BOSONUSD', 'PONDUSD', 'MXCUSD', 'JAMUSD', 'PROMUSD', 'DIAUSD',
       'LOOMUSD', 'STMXUSD', 'SHIBUSD', 'TRACUSD', 'POLYXUSDT',
       'IOSTUSDT', 'IOSTUSD', 'ARBUSDT', 'ARBUSD', 'FLOKIUSDT',
       'FLOKIUSD', 'XECUSDT', 'XECUSD', 'BLURUSDT', 'BLURUSD'])

trading_pair_array1.sort()

trading_pair_array = trading_pair_array1
#%%

import datetime

def print_current_time():
    now = datetime.datetime.now()
    current_minute = now.minute
    current_second = now.second
    print(now, current_minute, current_second)
    
    # Take the current minute and get the remainder of the product when divided by 5.
    # Take that output and subtract it from 5.  
    # This is the number of minutes until the next 5 minute interval mark hits.
    # Take this above value and multiply it by 60 (seconds in a minute)
    # Take this value and subtract the current second...this ensures we hit the next 5 
    # ...minute interval right on time.
    # Lastly, subtract 15 seconds as this will put the sleep time 15 right before the next
    # ...5 minute interval.  
    # I need to test the time it takes to complete the API call.  This value will take place
    #  of the 15 second.
    seconds_left = (5 - (current_minute % 5)) * 60 - 2 - current_second
    print('Current time and second: {} {} and Seconds until 15 seconds before the 5 min mark: {}'\
          .format(current_minute, current_second, seconds_left))
    
    # Wait until the next 5-minute interval minus 15 seconds
    time.sleep(1)
    
    
    # Print the current time
    print(now.hour, now.minute, now.second, now.microsecond==0)

# Run the script indefinitely
while True:
    print_current_time()

#%% two functrions and run cell
# Run below line for error code: 'Cannot run the event loop while another loop is running'
nest_asyncio.apply()

async def process_trading_pair(semaphore, trading_pair):
    url = f'https://api.binance.us/api/v3/klines?interval=5m&limit=1&symbol={trading_pair}'
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                data = await response.json()
                # Insert trading pair into the 0 index location of the .JSON output
                data[0].insert(0, trading_pair)
                return data[0]

async def main():
    global df_json
    semaphore = asyncio.Semaphore(20)
    # Array of trading pairs
    # trading_pairs = trading_pair_array
    # Gather all the coroutines for each trading pair
    # trading_pair_array was pulled in from crypto_binance_apy.py
    coroutines = [asyncio.create_task(process_trading_pair(semaphore, pair)) for pair in trading_pair_array]
    # Run the tasks
    values = await asyncio.gather(*coroutines)
    # Set Elapsed Time and print message
    df_json = pd.DataFrame(values)
    print(df_json.head())
    print(df_json.shape)

# NOTE: It is faster to use .get_event_loop(main()) than to use .run(main())
# Set the Time Loop counter
s = time.perf_counter()
asyncio.run(main())
# Create an event loop
# loop = asyncio.new_event_loop()
# Run the coroutines concurrently
# loop.run_until_complete(main())
elapsed = time.perf_counter() - s
print('Elapsed time: {}'.format(elapsed))
#%%
"""
Hello World of asyncio

Output:
one
one
one
two
two
two
/Users/derekfrost/Projects/examples/Examples/Example_Asyncio.py execute in 1.0017185839997182 seconds
"""
async def count():
    print('one')
    await asyncio.sleep(1)
    print('two')

async def main():
    await asyncio.gather(count(), count(), count())
    
if __name__ == "__main__":
    import time
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print('{} execute in {} seconds'.format(__file__, elapsed))
    
#%% Example of a .gather() with many coroutines
# Link: www.superfastpython.com/asyncio-gather

# Coroutine used for task
async def task_coro(value):
    # report a message
    print('task {} executing'.format(value))
    # sleep for 1 seconds
    await asyncio.sleep(1)
    
# Cortoutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # run the tasks
    await asyncio.gather(task_coro(0),
                         task_coro(1),
                         task_coro(2))
    # report a message
    print('main done')
    
# Start the asyncio program
s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print('Elapsed time: {}'.format(elapsed))

#%% Example of a gather() with many coroutines in a list
# This example is very similar to what I am attempting to do with trading_pair_array

# Link: www.superfastpython.com/asyncio-gather

# Coroutine used for task
async def task_coro1(value):
    # report a message
    print('task {} executing'.format(value))
    # sleep for 1 seconds
    await asyncio.sleep(1)
    
# Cortoutine used for the entry point
async def main():
    # report a message
    print('main starting')
    # Create many routines
    coros = [task_coro1(i) for i in range(10)]
    # run the tasks
    # When using .gather it is necessary to pass in the coroutine name with a '*'
    await asyncio.gather(*coros)
    # report a message
    print('main done')
    
# Start the asyncio program
s = time.perf_counter()
asyncio.run(main())
elapsed = time.perf_counter() - s
print('Elapsed time: {}'.format(elapsed))