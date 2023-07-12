#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 22:14:41 2023

@author: derekfrost
"""
# https://stackoverflow.com/questions/71542947/how-can-i-fix-task-was-destroyed-but-it-is-pending
import asyncio
import nest_asyncio

nest_asyncio.apply()

async def delay(n):
    print(f"sleeping for {n} second(s)")
    await asyncio.sleep(n)
    print(f"done sleeping for {n} second(s)")


loop = asyncio.get_event_loop()
t1 = loop.create_task(delay(1))
t2 = loop.create_task(delay(2))
loop.run_until_complete(t1)
loop.close()

#%%
async def main():
    t1 = asyncio.create_task(delay(1))
    t2 = asyncio.create_task(delay(2))
    await t2

"""
asyncio.run(): This method was introduced in Python 3.7 and is a higher-level 
convenience function provided by asyncio. It creates a new event loop, 
runs the specified coroutine, and closes the event loop once the coroutine completes.

Advantages:

Simplicity: asyncio.run() provides a straightforward way to run an asynchronous 
program without worrying about creating and managing an event loop manually.
Automatic cleanup: When the provided coroutine is finished, asyncio.run() 
ensures the event loop is properly closed, freeing up any resources associated with it.
Default settings: asyncio.run() sets up a basic event loop with reasonable defaults, 
making it easier to get started with asynchronous programming.
"""
asyncio.run(main())