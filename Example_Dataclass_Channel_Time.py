#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 23:11:45 2022

@author: derekfrost
"""

from dataclasses import dataclass
import time
import numpy as np
#%%

@dataclass
class ChannelTime:
    timechan: {}  # <- Error with this: AttributeError: type object 'ChannelTime' has no attribute 'timechan'
    
    epoch_time: float = 0.0
    channel: int = 0
    
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
        
#%%

time1 = time.time()

random_channel = np.random.randint(1000,6000,1).item()

chan1 = ChannelTime(time1, random_channel)
