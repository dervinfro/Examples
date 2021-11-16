#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 00:15:59 2021

@author: user
"""

# =============================================================================
# Try and Except Blocks
# =============================================================================
# print(varaible)

# Comment out the line below to see what the except block prints out.
# variable = 1

try:
	print(variable)
	
except NameError:
	print("This is an error due to 'variable' not being defined")
	
except:
	print("Unknown error")