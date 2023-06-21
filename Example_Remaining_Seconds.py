#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 14:56:08 2023

@author: derekfrost
"""

import datetime
import time
import numpy as np
import asyncio
import aiohttp
import nest_asyncio
#%%
trading_pair_array = np.array(['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'LTCUSDT', 'BNBUSDT', 'ADAUSDT',
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

trading_pair_array.sort()
#%%
nest_asyncio.apply()

async def process_trading_pair(trading_pair):
    url = f'https://api.binance.us/api/v3/klines?interval=5m&limit=1&symbol={trading_pair}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.json()
            print(trading_pair, '\n', 
                  datetime.datetime.utcfromtimestamp(data[0][0] / 1000), '\n',
                  datetime.datetime.utcfromtimestamp(data[0][6] / 1000))
            print(data)

async def main():
    # print main message
    # print('main starting')
    # Array of trading pairs
    # trading_pairs = trading_pair_array
    # Gather all the coroutines for each trading pair
    # trading_pair_array was pulled in from crypto_binance_apy.py
    coroutines = [process_trading_pair(pair) for pair in trading_pair_array]
    # Run the tasks
    await asyncio.gather(*coroutines)
    # Set Elapsed Time and print message
    # print('main done')
'''
# NOTE: It is faster to use .get_event_loop(main()) than to use .run(main())
# Set the Time Loop counter
s = time.perf_counter()
# Create an event loop
loop = asyncio.get_event_loop()
# Run the coroutines concurrently
loop.run_until_complete(main())
elapsed = time.perf_counter() - s
print('Elapsed time: {}'.format(elapsed))
'''
#%%
"""
DATE: 17JUN2023
When this script executes, prints out the Minute - Second - The # of seconds until we hit
that pre 15 second 5 minute interval.  
This is a running example of how I need my code to work when I make my API call.
The issue that I am currently having with my API it take 40+ seconds for the FOR loop to 
loop through all 294 coins to pull in the Kline data.  That is too long.  Looking into
Asyncio to see if I can speed up my process.

"""
print('While Loop run time', time.ctime())
while True:
    try:
        now = datetime.datetime.now().replace(microsecond=0)
        current_minute = now.minute
        current_second = now.second
        # Get remainder value of the current minute divided by five.
        # 5 minute interval minus the remainder
        # Multiply by the number of seconds in a minute (60)
        # Minus the number of seconds (4) before the five minute interval hits.
        # Minus the current second.
        remaining_seconds = (5 - (current_minute % 5)) * 60 - 4 - current_second
        if remaining_seconds == 0:
            # resp = requests.get('https://api.binance.us/api/v3/klines?interval=5m&limit=1&symbol=BTCUSD')
            # print(resp.json())
            # NOTE: It is faster to use .get_event_loop(main()) than to use .run(main())
            # Set the Time Loop counter
            s = time.perf_counter()
            # Create an event loop...do not use .get_event_loop...deprecated.
            loop = asyncio.new_event_loop()
            # Run the coroutines concurrently
            loop.run_until_complete(main())
            elapsed = time.perf_counter() - s
            print('Elapsed time: {}'.format(elapsed))
        else:
            # print(now.minute, now.second, remaining_seconds)
            pass
        # time.sleep(1)
    except Exception as e:
        exception_error = str(e) + ' ' + time.ctime()
        print('Error: ', exception_error)