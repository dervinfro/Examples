#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 23:43:10 2022

@author: derekfrost
"""

class NewClass:
    
    # Constructor
    def __init__(self, df):
        self.df = df
        
    # Instance Method
    def rsi(self, close_price, periods, ema=True):
        self.close_price = close_price
        self.periods = periods
        self.ema = ema
        
        self.delta = self.close_price.diff(periods)
        
        self.up = self.delta.clip(lower=0)
        self.down = -1 * self.delta.clip(lower=0)
        
        if self.ema == True:
            
            self.ma_up = self.up.ewm(com = periods -1, adjust=True, min_periods=periods).mean()
            self.ma_down = self.down.ewm(com = periods -1, adjust=False).mean()
        else:
            self.ma_up = self.up.rolling(com = periods -1, adjust=False, min_periods=periods).mean()
            self.ma_down = self.down.rolling(window = [periods], adjust=False).mean()  # <- Adjust my face on this
            
        self.rsi = self.ma_up/self.ma_down
        
        self.rsi = 100 - (100/(1 + self.rsi))
        
        return self.rsi
        
        