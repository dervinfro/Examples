#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df = pd.read_csv("/Users/user/Downloads/ML Analytics/ML Analytics - Course 3/social_honeypot_sample.csv")

#%% One Line Conditional Operator
# =============================================================================
# FOR Loop through DataFrame index values
# One line conditional: IF/THEN/ELSE
# IF TRUE: returns list of UserID field value and UserID column name
# IF FALSE: returns list of TweetID field value and TweetID column name
# Print list values of 0 and 1: UserID/Column Name OR TweetID/Column Name 
# =============================================================================
for x in df.index.values:
    
    result = [df.iloc[x]['UserID'], df.columns[0]] if df.iloc[x]['UserID'] < df.iloc[x]['TweetID'] else [df.iloc[x]['TweetID'], df.columns[1]]

    print('Greater is: ', x, result[0], result[1])
    
    

