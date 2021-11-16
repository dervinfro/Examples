#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 22:41:26 2021

@author: user
"""

a, b = 0, 1

print(a)
for x in range(10):
    c = a + b
    print(c)
    a = b
    b = c
    