#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  4 00:02:37 2022

@author: derekfrost
"""

import datetime
import time
import psutil


#%% Print out the time

while True:
    
    print(psutil.virtual_memory())
    # if minute divided by 5 = 0...return True
    if datetime.datetime.now().minute % 5 == 0:
        # if True...print
        print(time.asctime())
        print('This time is at true 5 minute intervals')
    # if False...pass and print 
    else:
        print(time.asctime())
        print('This is some off time that is not a true 5 minute intervals.')
        
    time.sleep(30)
    

#%% Print out seconds every 5 seconds
"""
The IF statement requires time.sleep() for this 5 second interval to operate correctly.
If time.sleep() is not present, the results print out 
"""
while True:
    if time.localtime().tm_sec % 5 == 0:
        time.sleep(5)
        print(time.localtime().tm_sec)

