#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 23 10:07:28 2023

@author: derekfrost
https://superfastpython.com/asyncio-semaphore/
"""

# SuperFastPython.com
# example of using an asyncio semaphore
from random import random
import asyncio
import nest_asyncio
import time

# Run below line for error code: 'Cannot run the event loop while another loop is running'
nest_asyncio.apply()
 
# task coroutine
async def task(semaphore, number):
    # acquire the semaphore
    async with semaphore:
        # generate a random value between 0 and 1
        value = random()
        # block for a moment
        await asyncio.sleep(value)
        # report a message
        print(f'Task {number} got {value}')
 
# main coroutine
async def main():
    # create the shared semaphore
    semaphore = asyncio.Semaphore(15)
    # create and schedule tasks
    tasks = [asyncio.create_task(task(semaphore, i)) for i in range(1000)]
    # wait for all tasks to complete
    # Advantage of .wait is that it performs tasks in chunks vs .gather is all at once.
    _ = await asyncio.wait(tasks)
 
s = time.perf_counter()
# start the asyncio program
asyncio.run(main())
elapsed = time.perf_counter() - s
print('Elapsed time: {}'.format(elapsed))
