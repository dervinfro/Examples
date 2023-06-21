#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 16 23:12:16 2023

@author: derekfrost
"""
# https://stackoverflow.com/questions/63021166/how-to-restart-a-python-program-after-it-crashes#:~:text=If%20you%20want%20to%20restart,run%20it%20again%20with%20python.

"""
*** how to restart a python program after it crashes ***
"""
from time import sleep

def run_forever():
    try:
        # Create infinite loop to simulate whatever is running
        # in your program
        while True:
            print("Hello!")
            sleep(10)

            # Simulate an exception which would crash your program
            # if you don't handle it!
            raise Exception("Error simulated!")
    except Exception:
        print("Something crashed your program. Let's restart it")
        # run_forever() # Careful.. recursive behavior
        # Recommended to do this instead
        handle_exception()

def handle_exception():
    # code here
    while True:
        print("Hello..HC")
        sleep(10)
    pass

run_forever()
