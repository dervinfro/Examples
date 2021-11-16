#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 23:50:16 2021

@author: user
https://stackoverflow.com/questions/52785579/pandas-dataframe-multiindex-merge/52785602
"""

import pandas as pd
import numpy as np

arrays = [['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
            ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]
tuples = list(zip(*arrays))
index1 = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])
index2 = pd.MultiIndex.from_tuples(tuples, names=['third', 'fourth'])

s1 = pd.DataFrame(np.random.randn(8), index=index1, columns=['s1'])
s2 = pd.DataFrame(np.random.randn(8), index=index2, columns=['s2'])

# An option for multi index merge
s1.merge(s2,  left_index=True, right_index=['third','fourth'])

# A second option for multi index merge
s1.loc[:, 's2'] = s2

# A third option
s1.combine_first(s2)