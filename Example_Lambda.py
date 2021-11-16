#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 23:14:56 2021

@author: user
"""

import numpy as np
import pandas as pd


#%%

# Set the x variable to 20 numbers between the values of 1 and 10
x = np.random.randint(1,10,20)

df = pd.DataFrame()

# =============================================================================
# Lambda x: x
# <Keyword> <bound variable>: <body>
# Lamba can only take expressions and NOT statements in the body
# =============================================================================

# Testing out the single line lambda function WITHOUT the FOR loop
lamb_output = (lambda x: np.square(x))(x)

# Same line as above except WITHOUT the np.square function
z = (lambda a: x**2)(x)

#%%
# =============================================================================
# This function takes two variables.
# The reason for this is that I wanted to test if the <variable> needed
#  to be the same as the <body>...it does not
# =============================================================================
def lamb_func(var_1, var_2):
	y = (lambda z: var_2 *10)(var_2)
	print('var 1 & 2', var_1, var_2)
	return y
	
print(lamb_func('a',lamb_output))

#%%

# Pass the Lambda function two bound variables of: 5 & 6
lamb_var = lambda c, d: c**d
print("Lambda Function using 5**6 equals output of: ", lamb_var(5,6))

# %%
