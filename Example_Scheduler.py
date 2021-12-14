#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 26 22:53:06 2021

@author: user
"""

import sched
import time
import schedule


#%% Schedule Function To Run

# 
scheduler = sched.scheduler(time.time, time.sleep)

# Create a Function to pass to scheduler.enter
def print_sched_time(data):
    print('Time: {}'.format(time.ctime()))
    print('Passing {} into function'.format(data))
    # print('Event:', time.ctime(), ' - ', data)

# Print Start Time
print('Start: {}'.format(time.ctime()))


def infinite_loop():
    while True:
        # Scheduler.enter to pass(delay, pri., func name * func arg)
        # 5 - The delay timer
        # 1 - Priority...not relevant with only one .enter()
        # print_sched_time - Name of Function to run.
        # argument to pass to the function above.
        scheduler.enter(5, 1, print_sched_time, argument=('dataframe',))
        
        # Run the scheduler
        scheduler.run()
        
infinite_loop()