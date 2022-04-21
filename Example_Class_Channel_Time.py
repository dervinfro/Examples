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

class ChannelTime:
    def __init__(self):
        self.__dict = {}
        
    def checkChannel(self, epoch_time, channel):
        self.epoch_time = epoch_time
        self.channel = channel
        timechan = self.__dict__ = {}
        if time in timechan:
            pass
        else:
            timechan.update({epoch_time: channel})
        
        print(timechan)
            
#%%
ChannelTime.checkChannel(time.time(), "12345")
        
    
        