#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 00:17:42 2022

@author: derekfrost
"""
# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/
from collections import Counter
from itertools import combinations
x = 'bbbb'
y = 'abccab'
z = 'pewkzzww'
s = "pwwkew"
t = (5,6)
u = "abcabcbb"


#%%
"""
The endstate for this problem is to get two numbers that properly represent the numbers
needed for a slice of a string.  In our case, we want all two number combos (non-repeating)
for the length of the string in question.
We need the two number returned as integers (SEE: i & j)
We then count the number of values in the string.
Any count > 1 is a repeating number, which is then passed.
Else we condition check the output count for the largest value.
We then return the largest value
"""
def longestSubstringWoRepeatingChar(string:str):
    output_count = 0
    for i, j in combinations(range(len(string) + 1), 2):
        # print(s[i:j], list(Counter(s[i:j]).values()))
        output = list(Counter(string[i:j]).values())
        if len(output) <= output_count:
            pass
        elif any(num > 1 for num in output):
            pass
        else:
            if sum(output) > output_count:
                output_count = sum(output)
            else:
                pass
    return output_count


