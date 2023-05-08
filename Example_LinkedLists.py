#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 22 22:19:24 2022

@author: derekfrost
"""

"""
Linked Lists
- Each element is called a Node
- Every Node has two parts: Data & Next
- The last Node has two parts: Data & None
- The first Node is called Head
"""
from collections import deque # Double End Queue

llist = deque([1,2,2,1])

def link_list(ll):
    return list(ll) == list(ll)[::-1]