#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 22:08:12 2021

@author: user
"""
import pandas as pd
import numpy as np
# import openpyxl

# Create a random integer to use as the microsecond for the time.
# This will make each date/time unique
random_int = np.random.randint(10000, 50000)

# Test dataset that will return a df of DateTimeIndex type
df = pd.date_range('1/1/2021 01:00:00.000', periods=5, freq='H')

# Convert the df above to a Timestamp
timestr = pd.to_datetime((str(df[0])))

# Set variable to timestamp and add on microseconds.
# Microseconds is what will be used to randomize each row
timestr = pd.Timestamp(timestr, unit='ms')

# replace the microsecond variable
timestr = timestr.replace(microsecond=random_int)
