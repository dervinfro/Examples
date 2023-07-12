#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 00:36:48 2023

@author: derekfrost
"""

import random

# Generate a random integer between 1 and 5
# This random integer is a mirror of the amount of trading pairs that are
# ...available for an Open Order in the Crypto_Project_V4.py script.
random_integer = random.randint(1, 5)

# Initialize a list to store the weighted random values
weighted_values = []

# Calculate the remaining sum needed to reach 1000
# This value mimics what would be the capital amount to be used for each of the
# ...Open Orders.  
remaining_sum = 1000

# Loop through the random_integer
for _ in range(random_integer):
    # Generate a random weight between 1 and the remaining sum
    weight = random.randint(1, remaining_sum)

    # Append the weight to the weighted_values list
    weighted_values.append(weight)

    # Update the remaining sum
    remaining_sum -= weight

# Calculate the last weight to ensure the total sum is 1000
last_weight = 1000 - sum(weighted_values)
weighted_values.append(last_weight)

# Display the weighted values and their sum
# This value mimics how much each trading pair would receive in capitial to when
# ...submitting an Open Order.
print(weighted_values)
print(sum(weighted_values))

