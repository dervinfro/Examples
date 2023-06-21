#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 22:14:27 2023

@author: derekfrost
"""

#it is clearly seen that self and obj is referring to the same object
'''
'self' represents the instance of the Class.
By using 'self', we can access the attributes and the methods of the class.

NOTE: The first argument of every Class Method, including init, is always a 
reference to teh current instance of the class.

https://www.geeksforgeeks.org/self-in-python-class/
'''
class check:
	def __init__(self):
		print("Address of self = ",id(self))

obj = check()
print("Address of class object = ",id(obj))

# this code is Contributed by Samyak Jain
