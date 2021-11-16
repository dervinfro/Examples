#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:54:09 2021

@author: user
"""
# =============================================================================
# https://www.kite.com/python/answers/how-to-find-the-moving-average-of-a-list-in-python
# =============================================================================

import numpy as np

numbers = [1,3,5,7,9,11]
window_size = 3

i = 0

# This FOR loop iterates through the 'numbers' list;
    # sets the window size to 3 which will show us 3 values at each iteration;
# Print the 'numbers' list - start at the range iteration;
    # end at the 'i' plus the window size.
# Print the numpy mean value of the current window iteration
for x in range(len(numbers)):
    print('{} : {}'.format(numbers[x:i + window_size],
                           np.mean(numbers[x:i + window_size])))
    i += 1
    

    