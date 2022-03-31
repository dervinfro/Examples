#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 29 21:51:39 2021

@author: user
"""

def palin(val1):
    return val1 == val1[::-1]

val1 = 'mom'

palin_boolean = palin(val1)
if palin_boolean == True:
    print('Yes..palin')
else:
    print('No...palin')