#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#%% Section 1
"""
Created on Thu Nov 25 01:37:05 2021

@author: user
"""

import streamlit as st
import time

#%%
x = 0

p = st.empty()

# st.title('This is a WHILE Loop test')
# st.header('We will see how this runs w multiple lines.')

while True:
    with p.container():
        st.header(f'This is a WHILE1 Loop test {x}')
        st.write(f"Your VALUE is {x}")
        st.write('test')
    time.sleep(1)
    x += 1