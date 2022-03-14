#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 20 00:51:40 2022

@author: derekfrost
"""

import time
import datetime

while True:
    time1 = datetime.datetime.now()
    
    time.sleep(5)
    
    time2 = datetime.datetime.now()
    
    print(time2 - time1)
    print(time2)