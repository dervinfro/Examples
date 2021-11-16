#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 16 23:39:22 2021

@author: user
"""
# =============================================================================
# Classes as Custom Data Types 
# =============================================================================
class Student: 
	pass

type(Student)

# Instance of Student() in object_1
object_1 = Student()

# Second instance of Student() in object_2
object_2 = Student()

# Instance of Student() object returns: <__main__.Student at 0x7fa266e68cc0>
# Stored in memory space: 0x7fa266e68cc0
object_1

# Instance of Student() object_2 returns: <__main__.Student at 0x7fa266a2ceb8>
# Stored in memory space: 0x7fa266a2ceb8
object_2

# Pass in object and class and it returns: True 
isinstance(object_1, Student)

# Set object_3 to a dictionary type
object_3 = {}

# Pass in object and class and it returns: False
isinstance(object_3, Student)

#%%
# =============================================================================
# Associating Attributes with Classes
# =============================================================================

# Attributes associated using the dot notation
object_1.name = 'Michael'

object_1.email = 'devifr@gmail.com'

# Attribute returns: Michael
object_1.name

object_2.name = 'Chad'

object_2.email = 'chad@xyz.com'

object_3 = Student()

class Student:
	name = ''
	score = 0
	active = True
	
s1 = Student()

s1.name, s1.score, s1.active

s1.name = 'John'

s1.score = 50

s1.name, s1.score

s2 = Student()

s2.name, s2.score, s2.active

s2.name = 'Lily'

s2.active = False

s2.name, s2.active, s2.score

#%%
# =============================================================================
# Initializing Class Objects
# =============================================================================

# Functions that exist inside a Class are METHODS
class Student:
	
	def __init__(self): #__init__ is a special method that calls self
	
		print('Initialized Called')
		
# Initialize object to Class
s1 = Student()	


#%%
# =============================================================================
# Passing Arguments for Initialization	
# =============================================================================
class Student:
	def __init__(self,name):
		self.name = name
		self.mail = name + "." + "@xyz.com"
		
s1 = Student('Kyle')

print(s1)

s1.name		
s1.mail

#%%
# =============================================================================
# Defining Addiotnial Methods in Classes
# =============================================================================
class Student:
	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.mail = first + "." + last + "xyz@com"
		
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
	
	def uppercase(self):
		self.first = self.first.upper()
		self.last = self.last.upper()
	
s1 = Student('Rowan','Frost')

# Alternate way to ref method within Class
Student.fullname(s1)

# Primary way to ref object -> dot notation to fullname() method
print(s1.fullname())

s1.fullname # Bound method...notice the missing "()"

s1.uppercase()

s1.fullname()

#%%
# =============================================================================
# Introducing Class Variables
# =============================================================================

class Competition:
	
# 	This is a class variable NOT an instance variable.
	raise_amount = 1.04
	
	def __init__(self, name, prize):
		self.name = name
		self.prize = prize

# Change Competition.raise_amount to raise_amount...see the error (Undefined name)
	def raise_prize(self):
		self.prize = self.prize * Competition.raise_amount
		
		
# debate = Competition('Debate', 500)

# print(debate.raise_amount)

# Competition.raise_amount		

essay = Competition('Essay', 500)	 

# Output: 500
essay.prize		

# Raise the price by 1.04
essay.raise_prize()

# Output: 520
essay.prize

#%%
# =============================================================================
# Class Variables and Instance Variables
# =============================================================================

class Competition:
	
# 	This is a class variable NOT an instance variable.
	raise_amount = 1.04
	
	def __init__(self, name, prize):
# 		Set as instance variables NOT class variables
		self.name = name
		self.prize = prize

# 
	def raise_prize(self):
		self.prize = self.prize * self.raise_amount


simulation = Competition('simulation', 100)

simulation.prize

simulation.raise_prize()

simulation.prize

# Special Attribute: dictionary of the Class Instance
# two keys ('simulation', 104)
# instance variables (name,prize)
simulation.__dict__

# Special Attribute: dictionary of the actual Class
Competition.__dict__

# New instance of the Competiton class in the instance object racing
racing = Competition('Racin', 1000)

racing.raise_amount

# Set raise_amount to a new value using Class object: Competition
Competition.raise_amount = 1.05

# Run the Special Attribute dictionary to confirm the new .raise_amount value
Competition.__dict__

# Output: 1.05
# .raise_amount variable of the Class updated on this instance.
simulation.raise_amount

# Output: 1.05
# .raise_amount variable of the Class updated on this instance.
racing.raise_amount

# Instance variable of .raise_amount set to 10
simulation.raise_amount = 10

# Output: (1.05, 10, 1.05)
Competition.raise_amount, simulation.raise_amount, racing.raise_amount

# Special Attribute: dictionary of the simulation instance
# Output: {'name': 'simulation', 'prize': 104.0, 'raise_amount': 10}
simulation.__dict__

#%%
# =============================================================================
# Class Varible Memory Sharing
# =============================================================================
class Competition:
	
# 	This is a class variable NOT an instance variable.
	participants = []
	
	def __init__(self, name, prize):
		
# 		Instance Variables
		self.name = name
		self.prize = prize
		
# Set instance of the Class
debate = Competition('debate',500)

debate.participants

# Append the Class Variable
Competition.participants.append('John')

Competition.participants

# Append the instance variable.
debate.participants.append('alice')

# Refer to the same list in Python Memory
# Output: ['John', 'alice']
debate.participants

# Set a new instance of the Class.
essay = Competition('Essay',456)

# Refer to the same list in Python Memory
# Output: ['John', 'alice']
essay.participants

# debate.participants.append('lilly')

# debate.participants

# essay.participants

Competition.__dict__

debate.__dict__

#%%
# =============================================================================
# Instance Variables
# =============================================================================
class Competition:
	
	def __init__(self, name, prize):
		self.name = name
		self.prize = prize
# 		Set participants as an instance variable NOT class variable
		self.participants = []
		
debate = Competition('debate',500)

debate.participants

# Error: type object 'Competition' has no attribute 'participants'
# Reason: 'participants' is associated with an instance and NOT the class.
Competition.participants

debate.participants.append('alice')

# 
debate.participants

essay = Competition('essay',456)

# Empty participants list
essay.participants

# Append essay participants list
essay.participants.append('Mike')

essay.participants

Competition.__dict__

essay.__dict__

debate.__dict__


#%%
# =============================================================================
# Getters and Setters for Private Variables
# =============================================================================

class Dog:
	
# __init__ method initializes the name and breed of the Dog class
	def __init__(self, name, breed):
		
# 		Set as instance variables NOT class variables
		self.name = name
		self.breed = breed
		
	def print_details(self):
		print('My name is {} and I am a {}'.format(self.name, self.breed))

# Set the instance of the d1 object to the Dog Class.		
d1 = Dog('Bodhi','pitbull')

d1.print_details()

# Access the name instance variable
d1.name = 'nala'

d1.print_details()

# Access the breed instance variable
d1.breed = 'mexican street mutt'

d1.print_details()

Dog.__dict__

# Output: {'name': 'nala', 'breed': 'mexican street mutt'}
# This is significant, as the key values will change when the "hack" is used
d1.__dict__

# Variable Hack
# All Instance and Class Variables in Python are public...this could be a issue
# See below..with the hack.


class Dog1:
	
# __init__ method initializes the name and breed of the Dog class
	def __init__(self, name, breed):
		
# 		Set as instance variables NOT class variables
		self.__name = name
		self.__breed = breed
		
	def print_details(self):
		print('My name is {} and I am a {}'.format(self.__name, self.__breed))
		
dg1 = Dog1('bodhi','pitbull')

# Output: {'_Dog1__name': 'bodhi', '_Dog1__breed': 'pitbull'}
# Notice the key value is now _ClassName__KeyName
dg1.__dict__

#%%
# =============================================================================
# Making Variable Private
# =============================================================================

class Dog:
	"""
	This is a class which defines the dog.
	"""
	
# 	This is a class variable NOT an instance variable.
	__species = 'canine'
	
# __init__ method initializes the name and breed of the Dog class
	def __init__(self,name,breed):
		
# 		Set as instance variables NOT class variables
# 	    Variables are starting with a '__' so they are private using the "hack"
# 	    The '__' are used to ensure that the variables are not used outside the Class
		self.__name = name
		self.__breed = breed
		self.__tricks = []
		
	def print_details(self):
		print('My name is {} and I am {} and I can do tricks {}'
			.format(self.__name, self.__breed, self.__tricks))
		
	def change_name(self, name):
		self.__name = name

# Getter Function		
	def get_name(self):
		return self.__name__
	
# Setter (or Update) Functions
	def set_name(self, name):
		self.__name = name

# Getter Function		
	def get_breed(self):
		return self.__breed
	
# Setter (or Update) Functions
	def set_breed(self, breed):
		self.__breed = breed
		
# Setter (or Update) Functions
	def add_trick(self, trick):
		self.__tricks.append(trick)
		
# Set the instance of the d1 instance to the Dog Class.
d1 = Dog('Nemo','Husky')

d1.print_details()

d1.add_trick('roll over')

d1.print_details()

d1.set_breed('Lab')

d1.print_details()	

#%%
# =============================================================================
# Create a Class to Represent a Student	
# =============================================================================

class Student:
	"""
	This is a class for a Student.
	It will take the following variables: Name, GPA, Clubs and  Active(boolean)
	"""
# __init__ method initializes the name and gpa of the Student Class.
	def __init__(self, name, gpa):
		self.__name = name
		self.__gpa = gpa
		self.__clubs = set()
		self.__active = True
		
# Setter (or Updater) Function
	def set_name(self, name):
		self.__name = name
		
# Setter (or Updater) Function
	def set_gpa(self, gpa):
		self.__gpa = gpa
	
# Setter (or Updater) Function
	def add_club(self, club):
		self.__clubs.add(club)

# Setter (or Updater) Function
	def remove_club(self, club):
		self.__clubs.remove(club)	
		
# Setter (or Updater) Function
	def set_active(self, active):
		self.__active = True
		
	def print_details(self):
		print('Student: ', self.__name)
		print(self.__gpa, self.__clubs, self.__active)
		

s = Student('james', 3.5)

s.add_club('Yoga')

s.print_details()

s.add_club('yoga')

s.print_details()

s.set_gpa(3.9)

s.print_details()

#%%
# =============================================================================
# Parse Student Details from a Dictionary
# =============================================================================

# You have student details in a dictionary format i.e a list of dictionaries. Write a method to convert these 
# to instances of the student class. Return a list of instances from a function

student_details_list = [
    {'name': 'Nina', 'gpa': 3.6, 'clubs': ['tennis', 'chess']},
    {'name': 'Emily', 'gpa': 3.9, 'clubs': ['tennis'], 'active': False},
    {'name': 'Michael', 'gpa': 3.2, 'clubs': ['football', 'chess']},
    {'name': 'Joe', 'gpa': 3.9, 'is_honors_student': True}
]


def get_student(student_details_list):
	student_list = []
	
	for student_details in student_details_list:
		
		if 'name' not in student_details or 'gpa' not in student_details:
			continue
		
		s = Student(student_details['name'], student_details['gpa'])
		
		if 'clubs' in student_details:
			for club in student_details['clubs']:
				s.add_club(club)
				
		if 'active' in student_details:
			s.set_active(student_details['active'])
			
		student_list.append(s)
		
	return student_list


students = get_student(student_details_list)

# Output: Four instances of the Student Class in the student_list
"""
[<__main__.Student at 0x7fa984f32e48>,
 <__main__.Student at 0x7fa985f14668>,
 <__main__.Student at 0x7fa985f145c0>,
 <__main__.Student at 0x7fa985f148d0>]
"""
students
 

for student in students:
	print(student.print_details())
	
	
#%%
# =============================================================================
# Exercises 
# =============================================================================
