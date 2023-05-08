#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May  3 23:45:22 2022

@author: derekfrost
"""
# https://realpython.com/introduction-to-python-generators/

import sys
import itertools

# Generator Comprehension...similar to a List Comprehension
nums_squared_gc = (i ** 2 for i in range(10000))
print(sys.getsizeof(nums_squared_gc))

# %%

mylist = [1, 2, 3, 4]
iterator = iter(mylist)

# %%
iterator1 = itertools.count(start=0, step=1)
repeat = itertools.repeat(2, 10)
print(list(next(iterator1) for _ in range(5)))
print(list(next(repeat) for _ in range(15)))

# %%
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    print(next(iterator))

# %% Count
# Python program to demonstrate
# infinite iterators

# for in loop
for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")

# %% Cycle

# Python program to demonstrate
# infinite iterators
count = 0

# for in loop
for i in itertools.cycle('AB '):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1

# %% Cycle - 2

# Python program to demonstrate
# infinite iterators

random_list = ['lotion', 'skin', 'hose', 'again']

# defining iterator
iterators = itertools.cycle(random_list)

# for in loop
for i in range(6):
    # Using next function
    print(next(iterators), end=" ")

# %% Repeat

# using repeat() to repeatedly print number 
print("Printing the numbers repeatedly : ")
print(list(itertools.repeat(25, 4)))

# %% Product

# import the product function from itertools module
from itertools import product

print("The cartesian product using repeat:")
print(list(product([1, 2], repeat=2)))
print()

print("The cartesian product of the containers:")
print(list(product(['geeks', 'for', 'geeks'], '2')))
print()

print("The cartesian product of the containers:")
print(list(product('AB', [3, 4])))

# %% Permutations

# import the product function from itertools module
from itertools import permutations

print("All the permutations of the given list is:")
print(list(permutations([1, 'geeks'], 2)))
print()

print("All the permutations of the given string is:")
print(list(permutations('AB')))
print()

print("All the permutations of the given container is:")
print(list(permutations(range(3), 2)))

# %% Combinations

# import combinations from itertools module

from itertools import combinations

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(['A', 2], 2)))
print()

print("All the combination of string in sorted order(without replacement) is:")
print(list(combinations('AB', 2)))
print()

print("All the combination of list in sorted order(without replacement) is:")
print(list(combinations(range(2), 1)))

# %% Combinations with replacements

# import combinations from itertools module

from itertools import combinations_with_replacement

print("All the combination of string in sorted order(with replacement) is:")
print(list(combinations_with_replacement("AB", 2)))
print()

print("All the combination of list in sorted order(with replacement) is:")
print(list(combinations_with_replacement([1, 2], 2)))
print()

print("All the combination of container in sorted order(with replacement) is:")
print(list(combinations_with_replacement(range(2), 1)))

# %% Accumulate

import itertools
import operator

# initializing list 1
li1 = [1, 4, 5, 7]

# using accumulate()
# prints the successive summation of elements
print("The sum after each iteration is : ", end="")
print(list(itertools.accumulate(li1)))

# using accumulate()
# prints the successive multiplication of elements
print("The product after each iteration is : ", end="")
print(list(itertools.accumulate(li1, operator.mul)))

# %% Chain

# Python code to demonstrate the working of
# and chain()

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# using chain() to print all elements of lists
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain(li1, li2, li3)))

# %% Chain From Iterable

# Python code to demonstrate the working of
# chain.from_iterable()

# initializing list 1
li1 = [1, 4, 5, 7]

# initializing list 2
li2 = [1, 6, 5, 9]

# initializing list 3
li3 = [8, 10, 5, 4]

# initializing list of list
li4 = [li1, li2, li3]

# using chain.from_iterable() to print all elements of lists
print("All values in mentioned chain are : ", end="")
print(list(itertools.chain.from_iterable(li4)))

# %% Compress

# Python code to demonstrate the working of
# and compress()

# using compress() selectively print data values
print("The compressed values in string are : ", end="")
print(list(itertools.compress('GEEKSFORGEEKS', [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0])))

# %% DropWhile

# Python code to demonstrate the working of
# dropwhile()

# initializing list
li = [2, 4, 5, 7, 8]

# using dropwhile() to start displaying after condition is false
print("The values after condition returns false : ", end="")
print(list(itertools.dropwhile(lambda x: x % 2 == 0, li)))

# %% Filter False (filterfalse)

# Python code to demonstrate the working of
# filterfalse()

# initializing list
li = [2, 4, 5, 7, 8]

# using filterfalse() to print false values
print("The values that return false to function are : ", end="")
print(list(itertools.filterfalse(lambda x: x % 2 == 0, li)))

# %% isslice

# Python code to demonstrate the working of
# islice()

# initializing list
li = [2, 4, 5, 7, 8, 10, 20]

# using islice() to slice the list acc. to need
# starts printing from 2nd index till 6th skipping 2
print("The sliced list values are : ", end="")
print(list(itertools.islice(li, 1, 6, 2)))

# %% starmap

# Python code to demonstrate the working of
# starmap()

# initializing tuple list
li = [(1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10, 1)]

# using starmap() for selection value acc. to function
# selects min of all tuple values
print("The values acc. to function are : ", end="")
print(list(itertools.starmap(min, li)))

# %% Takewhile

# Python code to demonstrate the working of
# takewhile()

# initializing list
li = [2, 4, 6, 7, 8, 10, 20]

# using takewhile() to print values till condition is false.
print("The list values till 1st false value are : ", end="")
print(list(itertools.takewhile(lambda x: x % 2 == 0, li)))

# %% Tee

# Python code to demonstrate the working of
# tee()

# initializing list
li = [2, 4, 6, 7, 8, 10, 20]

# storing list in iterator
iti = iter(li)

# using tee() to make a list of iterators
# makes list of 3 iterators having same values.
it = itertools.tee(iti, 3)

# printing the values of iterators
print("The iterators are : ")
for i in range(0, 3):
    print(list(it[i]))

# %% Zip Longest (ziplongest)

# Python code to demonstrate the working of
# zip_longest()

# using zip_longest() to combine two iterables.
print("The combined values of iterables is : ")
print(*(itertools.zip_longest('GesoGes', 'ekfrek', fillvalue='_')))
