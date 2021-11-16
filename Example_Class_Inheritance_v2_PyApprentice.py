#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 00:00:26 2021

@author: user
"""

# =============================================================================
# Inheriting form the Object Base Class
# =============================================================================
# No body defined - Most Common Method for a Class - inheritence implied
class Shape:
	pass

#%% Shape - Inheritence Implied
# Inheritence implied
class Shape():
	pass

#%% Shape Class - Inheritence Explicit
# 'object' keyword in Python
# Shape inherits from the Class 'object' - inheritence explicit
class Shape(object):
	pass

#%% Shape Class inherits from buit in object
# Shape class inherits from the built in object class
class Shape:
	
	def __init__(self, shape_type, color='red'):
		
# Set as instance variables NOT class variables
		self.__type = shape_type
		self.__color = color
		
	def get_type(self):
		return self.__type
	
	def get_color(self):
		return self.__color
	
	def get_area(self):
		pass
	
	def get_perimeter(self):
		pass
	
	
#%% 
circle = Shape('circle')

# __main__.Shape
type(circle)


circle.get_type()

circle.get_color()

square = Shape('square', color='blue')

# __main__.Shape
type(square)

square.get_type()

square.get_color()

#%% 
# =============================================================================
# Modeling is-a Relationship Using Subclasses
# =============================================================================

s = Shape('circle')

# This will return nothing, since this method does not have an action in the Class
s.get_area()

# This will return nothing, since this method does not have an action in the Class
s.get_perimeter()

#%%
# Class Inheritence uses the Syntax below
# Shape =  Base Class (Parent or Super Class)
# Circle = Derived Class (Child or SubClass of Shape Class)
class Circle(Shape):
	pass

# TypeError: __init__() missing 1 required positional argument: 'shape_type'
circle = Circle()

circle = Circle('circle')

# __main__.Circle - this shows an instance of the Circle Class
type(circle)

#%%
# =============================================================================
# Invoking Base Class Methods from SubClasses
# =============================================================================

class Circle(Shape):
	
	def __init__(self, color='green'):
		Shape.__init__(self, 'circle', color)
		
		
class Square(Shape):
	
	def __init__(self, color):
		Shape.__init__(self,'square', color)
		
circle = Circle()

square = Square('Orange')

circle.get_type(), square.get_type()

circle.get_color()

square.get_color()

#%%
# =============================================================================
# Defining Implementations of Base Class Methods
# =============================================================================

import math

class Circle(Shape):
	
	def __init__(self, radius):
		Shape.__init__(self, 'circle')
		
		self.__radius = radius
		
	def get_area(self):
		return math.pi  * self.__radius * self.__radius 
	
	def get_perimeter(self):
		return 2 * math.pi * self.__radius


c = Circle(10)
 
c.get_area()

c.get_perimeter()

class Square(Shape):
	
	def __init__(self, side):
		Shape.__init__(self, 'square')
		
		self.__side = side
			
	def get_area(self):
		return self.__side * self.__side 
	
	def get_perimeter(self):
		return 4 * self.__side 
	
	
	
s = Square(10)

s.get_area()

s.get_perimeter()


#%%
# =============================================================================
# Superclass and Subclass Hierarchies
# =============================================================================

class Competition:
	
# Class Variable NOT Instance Variable
# Same value for all instances of this Class
	__raise_amount = 1.10
	
	def __init__(self, name, prize):
		self.__name = name
		self.__prize = prize
# Getter
	def get_name(self):
		return self.__name
	
# Getter
	def get_prize(self):
		return self.__prize
	
	def raise_price(self):
		self.__prize = self.__prize * self.__raise_amount
		
comp = Competition('race',100)

# __main__.Competition - This shows an instance of the Competition class.
type(comp)

# Returns prize value: 100
comp.get_prize()

# Inherits from class Competition(builtins.object)
help(Competition)

Competition.__dict__

#%%% Creating a Subclass
class Sprint(Competition):
	pass

help(Sprint)

Competition.__dict__

Sprint.__dict__


sprint = Sprint('100m', 700)

type(sprint)

sprint.__dict__

sprint.get_name()

sprint.get_prize()

#%%% Creating an Object of a Parent Class
# New instance
chess = Competition('Chess', 1000)

# getter
chess.get_prize()

# getter
chess.get_name()

# raise the price
chess.raise_price()

# getter
chess.get_prize()

#%% Definigg Methods in a Subclass

# Competition = Parent Class // Cycling = Child Class
class Cycling(Competition):
	
# Instance Variables NOT Class Variables 
	def __init__(self, name, prize, country):
# super() = Reference the Parent (Competition) of the current Child (Cycling) Class
		super().__init__(name, prize)
		
		self.__country = country
		
	def get_country(self):
		return self.__country
	
cycling = Cycling('10km',7400, 'USA')


cycling.get_country()

cycling.get_prize()

type(cycling)

cycling.__dict__

# Return boolean TRUE
issubclass(Cycling, Competition)

#%% Multiple Inheritence

# A class can be derived from more than one class, that is called multiple inheritence.

class Father:
	pass

class Mother:
	pass

# Child1 = Child Class
# Mother, Father = Parent Class
class Child1(Mother, Father):
	pass

# Interesting Artifact in help function: Method resolution order
help(Child1)

# Child2 = Child Class
# Mother, Father = Parent Class 
class Child2(Father, Mother):
	pass

# Interesting Artifact in help function: Method resolution order
help(Child2)

class Father:
	
	def height(self):
		print('I have inherited my height from my father')
		
		
class Mother:
	
	def intelligence(self):
		print('I have inherited my intelligence from my Mother')
		
class Child(Mother, Father):
	
	def experience(self):
		print('My experiences are all my own')
		
c = Child()

# .height() inherited from the Father Class
c.height()

# .intelligence() inherited from the Mother Class
c.intelligence()


c.experience()


class Employee:
	
	
	def __init__(self, name, age):
		self.__name = name
		self.__age = age

	def show_name(self):
		print(self.__name)
		
	def show_age(self):
		print(self.__age)
		
		
class Salary:
	
	def __init__(self, salary):
		self.__salary = salary
		
	def get_salary(self):
		print(self.__salary)
		
# Database = Child Class
# Employee, Salary = Parent Class
class Database(Employee, Salary):
	
	def __init__(self, name, age, salary):
		Employee.__init__(self, name, age)
		Salary.__init__(self, salary)
		
emp1 = Database('Rowan',2, 5000)

# Inherit the .show_name() from teh Employee Class
emp1.show_name()

# Inherit the .show_age() from the Employee Class
emp1.show_age()

# Inherit the .get_salary from the Salary Class
emp1.get_salary()

# Look at the outputs of help to see Method resolution order
help(Database)

#%% Multilevel Inheritence

class Grandparent:
	
	def height(self):
		print('I have inherited my height from my grandparent')
		
class Parent(Grandparent):
	
	def intelligence(self):
		print('I have inherited my intelligence from my parent')
		
class Child(Parent):
	
	def experience(self):
		print('My experiences are all my own')
		
# Look at the output of help(Child) to see the Method resolution order
help(Child)

c = Child()

# Inherited from grandparent Class
c.height()

# Inherited from parent Class
c.intelligence()

# Inherited from Child Class
c.experience()

class Grandparent(object):
	
	def __init__(self, city):
		self.__city = city
		
	def get_city(self):
		return self.__city
	
class Parent(Grandparent):
	
	def __init__(self, city, lastname):
		Grandparent.__init__(self, city)
		
		self.__lastname = lastname

	def get_lastname(self):
		return self.__lastname
	
p1 = Parent(city='Billings', lastname='Frost')

# .get_city() is inherited from the Grandparent Class
p1.get_city()

p1.get_lastname()

class Person(Parent):
	
	def __init__(self, city, lastname, firstname):
		Parent.__init__(self, city, lastname)
		
		self.__firstname = firstname
		
	def get_firstname(self):
		return self.__firstname
	
person = Person('Billings','Frost','Rowan')

person.get_city(), person.get_firstname(), person.get_lastname()

# Look at the output of help() to see the Method resolution Order
help(Person)

p1.__dict__

p1.__weakref__


#%% Polymorphism - Part 1

# =============================================================================
# Polymorphism describes a pattern in object oriented programming in which 
# classes have different functionality while sharing a common interface.
# =============================================================================

class Hominidae():
	
	def communication(self):
		print('They use auditory calls and visual cues')

	def walk(self):
		print('They are knuckle-walkers, used to hang and swing from one tree to another')
		
class Human(Hominidae):
	
	def communication(self):
		print('They use language to communicate')
		
	def walk(self):
		print('The are bipeds')
		
class Gorilla(Hominidae):
	
	def communication(self):
		print('They use 25 distinct ways to communicate')
		
	def walk(self):
		print('They are knuckle walkers')
		
hominidae = Hominidae()

human_1 = Human()

gorilla_1 = Gorilla()

hominidae.communication()

human_1.communication()

gorilla_1.communication()

hominidae.walk()

human_1.walk()

gorilla_1.walk()

