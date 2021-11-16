"""
https://realpython.com/pandas-settingwithcopywarning/
"""

import copy

#create a list of lists
a = [[1,1,1,1],[2,2,2,2],[3,3,3,3]]

#Create a shallow copy of the list
shallow_a = copy.copy(a)

#Create a deep copy of the list
deep_a = copy.deepcopy(a)

#Modify an element of the shallow copy
shallow_a[1][0] = 0

#Modify an element of the deep copy
deep_a[1][0] = 99

print('Original: {}'.format(a))
print('Shallow: {}'.format(shallow_a))
print('Deep: {}'.format(deep_a))
print()
#ID below uses the memory address.
print(id(a[1]))
print(id(shallow_a[1]))
print(id(deep_a[1]))
