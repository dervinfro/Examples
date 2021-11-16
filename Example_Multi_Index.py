#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 00:05:20 2021

@author: user
"""
import pandas as pd
import numpy as np


arrays = [ ['bar', 'bar', 'baz', 'foo', 'foo', 'foo',   'qux'],
           ['one', 'two', 'one', 'one', 'two', 'three', 'one']]
tuples = list(zip(*arrays))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(7, 3), index=index, columns=['A', 'B', 'C'])


df.groupby(level='first').tail(1)

