#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 23:57:39 2022

@author: derekfrost
"""
"""
Create Function, within a Class, that takes in a time/channel pair;
checks to see if pair is already in dict;
call out to API (API not created to just make up API call)
REF: https://curious-joe.net/post/2022-03-11-oop-in-python-elements-of-class/oop-python-understanding-class/
REF: https://realpython.com/python3-object-oriented-programming/
"""
import time
import numpy as np

# A Class will have two (2) components: Attributes AND Actions
# Functions that exist inside a Class are METHODS
class ChannelTime:
    
    # Create the dictionary to hold time & channel
    timechan = {}
    
    # Class Attributes Below (AKA: Member Variables)
    #__init__ is a special method that calls self
    # 'self' is the instance
    def __init__(self, epoch_time, channel):  # <- Constructor. 
        self.epoch_time = epoch_time  # <- Instance Var.
        self.channel = channel  # <- Instance Var.
    
    # Class Actions Below: (AKA: Member Functions OR Method)
    def checkChannel(self):
        print('{} + {}'.format(self.epoch_time, self.channel))
        
        # If time key in timechan dictionary then pass
        if self.epoch_time in self.timechan :
            print('Epoch time key is already in dictionary.')
            pass
        else:
            # Set dictionary key/value pair
            self.timechan[self.epoch_time] = self.channel
        print('timechan: ', self.timechan)
        
    # Representation of the object, used for debugging and logging
    def __repr__(self):
        return "{} {}".format(self.epoch_time, self.channel)
    
    # Readable representation to be displayed to the user.
    def __str__(self):
        return f"{self.epoch_time} ++ {self.channel}"
            
#%%
# A unique static time used to test the key in the dictionary
unique_time = 1650687785.941256

unique_time1 = time.time()

# Create a random channel freq number
ran_chan = np.random.randint(1000,5000,1).item()
ran_chan = 4007

# Create a instance called chan1
chan1 = ChannelTime(unique_time, ran_chan)

repr(chan1)

str(chan1)


ChannelTime.checkChannel(chan1)

chan1.checkChannel()        
