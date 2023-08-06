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
from dataclasses import dataclass

# A Class will have two (2) components: Attributes AND Actions
# Functions that exist inside a Class are METHODS
@dataclass
class ChannelTime:
    # With @dataclass there is no need for "def __init__" Constructor
    epoch_time: int =  0 # <- Instance Variable
    channel: int = 0 # <- Instance Variable
    # Create the dictionary to hold time & channel
    '''
    timechan: This is a class-level variable, defined outside of any method. 
    It is shared among all instances of the class. Class-level variables are 
    prefixed with the class name (cls) to distinguish them from instance 
    variables. When you access a class-level variable, you use cls.variable_name.
    '''
    timechan = {}
    
    def instanceMethod(self):
        print('Instance Epoch Time: ', self.epoch_time)
        print('Instance Channel: ', self.channel)
        
    # Class Actions Below: (AKA: Member Functions OR Method)
    '''
    epoch_time and channel: These are local variables within the checkChannel method. They are passed as arguments when the method is called, and they are used only within the scope of the method. These variables don't have any relation to the class itself and are specific to each invocation of the method.
    '''
    @classmethod
    def checkChannel(cls, epoch_time, channel):
        print('{} + {}'.format(epoch_time, channel))
        
        # If time key in timechan dictionary then pass
        if epoch_time in cls.timechan :
            print('Epoch time key is already in dictionary.')
            pass
        else:
            # Set dictionary key/value pair
            cls.timechan[epoch_time] = channel
        print('timechan: ', cls.timechan)
            
#%%
# A unique static time used to test the key in the dictionary
unique_time = 1650687785.941256

unique_time1 = time.time()

# Create a random channel freq number
ran_chan = 4007
ran_chan1 = np.random.randint(1000,5000,1).item()

# Repr works due to the @dataclass being imported and used above Class
repr(chan1)

# Str works due to the @dataclass being imported and used above Class
str(chan1)

# Create a instance called chan1
chan1 = ChannelTime(unique_time1, ran_chan1)
chan1.instanceMethod()

# Class decorator @classmethod does not require Instance object
ChannelTime.checkChannel(unique_time, ran_chan)