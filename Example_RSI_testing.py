#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 23:58:31 2023

@author: derekfrost
"""

import pandas as pd
import numpy as np

data = {
    'open_time': [
        '2023-06-15 00:20:00', '2023-06-15 00:25:00', '2023-06-15 00:30:00', '2023-06-15 00:35:00',
        '2023-06-15 00:40:00', '2023-06-15 00:45:00', '2023-06-15 00:50:00', '2023-06-15 00:55:00',
        '2023-06-15 01:00:00', '2023-06-15 01:05:01', '2023-06-15 01:10:00', '2023-06-15 01:15:00',
        '2023-06-15 01:20:00', '2023-06-15 01:25:01', '2023-06-15 01:30:00', '2023-06-15 01:35:01',
        '2023-06-15 01:40:00', '2023-06-15 01:45:00', '2023-06-15 01:50:00', '2023-06-15 01:55:01',
        '2023-06-15 02:00:01', '2023-06-15 02:05:00', '2023-06-15 02:10:00', '2023-06-15 02:15:00',
        '2023-06-15 02:20:00', '2023-06-15 02:25:00', '2023-06-15 02:30:00', '2023-06-15 02:34:59',
        '2023-06-15 02:40:00', '2023-06-15 02:45:00'
    ],
    'close': [
        52.4, 52.4, 52.4, 53.2, 53.2, 53.2, 53.2, 53.2, 53.2, 53.2, 53.2, 53.2, 53.2, 53.5, 53.5, 53.5, 53.5,
        53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.5, 53.0
    ]
}

df = pd.DataFrame(data)
df['open_time'] = pd.to_datetime(df['open_time'])
df = df.set_index('open_time')

def calculate_rsi(data, period=14):
    close_delta = data['close'].diff()
    gain = close_delta.mask(close_delta < 0, 0)
    loss = abs(close_delta.mask(close_delta > 0, 0))
    average_gain = gain.rolling(window=period).mean()
    average_loss = loss.rolling(window=period).mean()
    rs = average_gain / average_loss
    rsi = 100 - (100 / (1 + rs))
    return rsi

df['rsi_14'] = calculate_rsi(df, period=14)

