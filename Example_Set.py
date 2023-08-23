
"""
Set = unordered collection of unique elements
cannot contain lists or dictionaries
Sets can only contain immutable data
Sets do not have a lookup ability
== is an equality check
= is an assignment operator

SEE: leet_217.py
"""

import numpy as np

set_str = {'CZ','Glock','STI','Tanfoglio','BUL','Infinity'}
set_str2 = {'springfield','Nighthawk','STI','Limcat'}
print('Set String: ', set_str)

#Sets have no order, hence we can't call index ie set_str[1]
# Function Update will update multiple values to Set
set_str.update(['Dan Wesson', 'springfield','STI','Limcat'])
print('Set String 2: ', set_str2)

# Union: Return elements from one Set OR the other Set
set_str | set_str2

# Intersection: Return elements from one Set and the other Set
set_str & set_str2

# Difference: Will show results of left had Set
set_str - set_str2

# Systemic Difference: Return where Sets are not equal
set_str ^ set_str2

#%%
    """The big difference here is that 'array' will print out 10 integers...some might be duplicates.
    If I were to pass that array into the set() method, the result would be that it would only show
    the unique values AND it would drop the duplicates.
    """
# Ten random integers
array = np.random.randint(0, 10, 10)
# ie [6 1 6 0 0 2 2 8 4 7]

set(array)
# ie {0, 1, 2, 4, 6, 7, 8}
