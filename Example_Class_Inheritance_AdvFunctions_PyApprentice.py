#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 00:40:29 2021

@author: user
"""
#%% The repr and str Special Methods

# =============================================================================
# The str method is a readable method for the end user, 
# this is not used for any other operations
# The repr method is an unambiguous representation, 
# it is mainly used for debugging etc.
# =============================================================================

class Competition:
	
	def __init__(self, name, prize):
		self.__name = name
		self.__prize = prize
		
rowing = Competition('rowing', 10000)

# Memory Location Output below
# Output: <__main__.Competition object at 0x7fa984ead6d8>
# This output is uninformed and vague
print(rowing)

# Memory Location Output below
# Output: Out[11]: <__main__.Competition at 0x7fa984ead6d8>
rowing


class Competition:
	
	def __init__(self, name, prize):
		self.__name = name
		self.__prize = prize
		
# repr method
# This method determines how an object is represented when you print out this
# object on the screen using the Print Function
# This Method will Return the object of the format below
	def __repr__(self):
		return "('{}', {})".format(self.__name, self.__prize)
	
	
archery = Competition('archery',5000)

# Output: ('archery', 5000)
# Much more informed output of the 'archery' instance
print(archery)

# Output: Out[14]: "('archery', 5000)"
repr(archery)

# Output: Out[15]: "('archery', 5000)"
str(archery)


class Competition:
	
	def __init__(self, name, prize, country):
		self.__name = name
		self.__prize = prize
		self.__country = country
		
	def get_name_country(self):
		return '{} {}'.format(self.__name, self.__country)
	
	def __repr__(self):
		return "Competition: {} held in {}, prize: {}" \
			.format(self.__name, self.__country, self.__prize)
			
	def __str__(self):
		return '{} {}'.format(self.get_name_country(), self.__prize)
	

archery1 = Competition('archery', 6000, 'UK')

# Output: Out[17]: Competition: archery held in UK, prize: 6000
# repr Method was invoked above for the output
archery1

# Output: archery UK 6000
# str Method was invoked above for the output
print(archery1)


print(repr(archery1))

print(str(archery1))

#%% The add Special Method

# Methods for numerical operations

# Output: 3
1 + 2

# Output: 3
int.__add__(1,2)

# Output: ab
'a' + 'b'

# Output: ab
str.__add__('a','b')

class Savings:
 	
 	def __init__(self, amount):
 		 self.__amount = amount
		
s1 = Savings(10000)

s2 = Savings(20000)

# Output: TypeError: unsupported operand type(s) for +: 'Savings' and 'Savings'
# the + operator will not work for the Savings Class object instances
s1 + s2

class Savings2:
	
	def __init__(self, amount):
		self.__amount = amount
		
	def __add__(self, other):
		return self.__amount + other.__amount
	
s1 = Savings2(10000)

s2 = Savings2(50000)

# Output: Out[53]: 20000
s1 + s2

# Output: Out[63]: 20000
# Different format as above, however same output
# this __add__ is in ref to the line 126 in the class Savings2
s1.__add__(s2)


#%% The sub Special Method

# Method for Subtraction

class MethodSub:
	
	def __init__(self, number):
		self.__number = number
		
	def __sub__(self, other):
		return self.__number - other.__number
	
num1 = MethodSub(10)

num2 = MethodSub(8)

num1 - num2

# Output same as above
# this __sub__ is in ref to the line 154 in the class MethodSub
num1.__sub__(num2)


#%% The mul Special Method

1.0 * 2.1

# float is a builtin Class - __mul__ is the Special Method
# float.__mul__(1.0,2.1)

# Output: TypeError: descriptor '__mul__' requires a 'float' object but received a 'int'
# float.__mul__(1, 2.1)


class Savings:
	
	def __init__(self, amount):
		self.__amount = amount
		
	def __add__(self, other):
		return self.__amount + other.__amount
	
	def __mul__(self, other):
		if type(other) == int or type(other) == float:
 			return self.__amount * other
		else:
 			raise ValueError("Can only multiply by int or float")
			
s1 = Savings(100)

s2 = Savings(2000)

# Output: ValueError: Can only multiply by int or float
s1 * s2

s1 * 40

# Out[148]: 300
s1.__mul__(3)
#%% Special Methods for Other Operations

# Floor divison - return whole integer
# Output: 3
10 // 3

class MethodFloorDiv:
	
	def __init__(self, number):
		self.__number = number
		
	def __floordiv__(self, other):
		return self.__number // other.__number
	
# Instance of the MethodFloorDiv Class
num1 = MethodFloorDiv(10)

# Instance of the MethodFloorDiv Class
num2 = MethodFloorDiv(3)

# Output: 3
num1 // num2

# Output: 3
num1.__floordiv__(num2)

#%%
# Method of modulo

# Output: 0
4 % 2

# Output: 1
5 % 2

class MethodMod:
	
	def __init__(self, number):
		self.__number = number
		
# __mod__ take in input argument "other"
# this variable expects to have a property of __number
	def __mod__(self, other):
		return self.__number % other.__number
	
num1 = MethodMod(10)

num2 = MethodMod(3)
	
# Output: 1
num1 % num2

# Output: 1
num1.__mod__(num2)

int.__mod__(5,2)



#%% Power 

6**2

int.__pow__(6,2)


help(int.__pow__(6,2))


#%% Len() Method

len('test')

str.__len__('test')

some_list = [13,5,7,9,10]

len(some_list)

class Participants:
	
	def __init__(self):
		self.__participants = []
		self.index = 0
		
	def add_participants(self, name):
		self.__participants.append(name)
		
	def __len__(self):
		return len(self.__participants)
	
	def __iter__(self):
		self.__index = 0
		return self
	
	def __next__(self):
		if self.__index == len(self.__participants):
			raise StopIteration
			
		p = self.__participants[self.__index]
		
		self.__index += 1
		
		return p
	
p = Participants()

len(p)

p.add_participants('Rowan')
 
len(p)

list.__dict__

p.__dict__
#%% Custom Iterators Using Special Methods

for number in some_list:
	print(number)
	
p.add_participants('Derek')
p.add_participants('Crystal')
p.add_participants('Henry')

# Output: 4
p.__len__()

for x in p:
	print(x)

# Output: Out[205]: <__main__.Participants at 0x7fa985fc92e8>
iter(p)

# Output: Out[206]: 'Rowan'
next(p)

# Output: Out[207]: 'Derek'
next(p)

# Output: Out[208]: 'Crystal'
next(p)

# Output: Out[209]: 'Henry'
next(p)

# Output: StopIteration
next(p)

#%% Defining Properties on Classes

class Wrestler:
	
	def __init__(self):
		self.__name = ''
		
	def set_name(self, name):
		self.__name = name
		
	def get_name(self):
		return self.__name
	
w1 = Wrestler()

w1.set_name('Rowan')

# Output: Out[222]: 'Rowan'
w1.get_name()

# Output: AttributeError: 'Wrestler' object has no attribute 'name'
w1.name

w1.__dict__

# Output: Out[227]: 'Rowan'
w1._Wrestler__name


#%%

class Wrestler:
	
	def __init__(self):
		self.__name = ''
		
	def set_name(self, name):
		print('setter method called')
		self.__name = name
		
	def get_name(self):
		print('getter method called')
		return self.__name
	
	def del_name(self):
		print('deleter method called')
		
		del self.__name
	
# 	Setting a property function is invoked using four input arguements:
# 	(fget, fset, fdel, doc)

	name = property(get_name, set_name, del_name)
	
w = Wrestler()

# Output: setter method called
w.name = 'Rowan'

# Output: getter method called
# .....Out[237]: 'Rowan'
w.name

# Output: deleter method called
del w.name

#Output: AttributeError: 'Wrestler' object has no attribute '_Wrestler__name'
w.name

#%% Defining Properties Using Decorators

class Wrestler:
	
	def __init__(self, name):
		self.__name = name
		
# @ property is a Decorator
# This is the method I want to invoke when the name property is accessed	
	@property	
	def name(self):
		print('getter method called')
		return self.__name
	
# @name is the Decorator
# .setter indicates to Python that this is the set function
	@name.setter
	def name(self, value):
		print('setter method called')
		self.__name = value
		
		
	@name.deleter
	def name(self):
		print('deleter method called')
		del self.__name


w = Wrestler('Rowan')

w.name

w.__dict__

del w.name

w.name


#%% Class Methods

class Competition:
	
# This is a class variable and NOT an instance variable
	__raise_amount = 1.04
	
# 	Name and Prize are instance variables
	def __init__(self, name, prize):
		self.__name = name
		self.__prize = prize
		
	def raise_pirze(self):
		self.__prize == self.__prize * self.__raise_amount
		
	def print_details(self):
		print('Name: {}, prize: {}'.format(self.__name, self.__prize))
		
# The decorator (@classmethod) indicates that this is a class method
# Class Methods have access to the State of the Class.
# The input arguement is in ref to the Class and NOT an object or an 
# instance of the Class
	@classmethod
	def get_raise_amount(cls):
		return cls.__raise_amount
	
# The decorator (@classmethod) indicates that this is a class method
	@classmethod
	def set_raise_amount(cls, amount):
		cls.__raise_amount = amount
		
# The decorator (@classmethod) indicates that this is a class method
	@classmethod
	def from_str(cls, competition_str):
		name, prize = competition_str.split('-')
		
		return cls(name, prize)
	
	
sprint = Competition('sprint', 1000)

# Output: Out[3]: 1.04
Competition.get_raise_amount()

# Output: Out[4]: 1.04
sprint.get_raise_amount()


sprint.set_raise_amount(1.06)

# Output: Out[6]: 1.06
sprint.get_raise_amount()

swimming_str = 'Swimming-8000'

name, prize = swimming_str.split('-')

swimming = Competition(name, prize)

# Name: Swimming, prize: 8000
swimming.print_details()

archery_str = 'Archery-9000'

archery = Competition.from_str(archery_str)

# Output: Name: Archery, prize: 9000
archery.print_details()

#%% Static Methods

class Rectangle:
	
	def area(x,y):
		return x * y

Rectangle.area = staticmethod(Rectangle.area)


print('The area of a rectangle is: ', Rectangle.area(15, 10))








#%%% Static Method cont.

class Rectangle:
	
	@staticmethod
	def area(x,y):
		return x * y

print('The area of a rectangle is: ', Rectangle.area(15, 18))


#%% Abstract Base Class





















