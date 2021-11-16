# =============================================================================
# Class defining Dog
# __init__ has two required variables (name & age)
# Any future instance of the Dog Class will require both variables.
# .title() will capitalize the 'name' variable.
# A Class will have two (2) components: Attributes AND Actions
# =============================================================================

class Dog():
	"""A simple attempt to model a dog"""
	
# 	Class Attributes Below (AKA: Member Variables)
	def __init__(self, name, age):
		"""initialize name and age attributes"""
		self.name = name
		self.age = age
	
# 	Class Actions Below (AKA: Member Functions OR Method)
	def sit(self):
		"""simulate a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")
		
	def roll_over(self):
		"""simulate a dog rolling over in response to a command"""
		print(self.name.title() + " rolled over")
		
		

#%%
# =============================================================================
# Three different instances of the Dog Class
# NOTE: The my_dog3 will produce the following error:
# 	TypeError: __init__() missing 2 required positional arguments: 'name' and 'age'
# 	This makes sense in that the (def __init__) is indicating that the Dog class requires two inputs.
# =============================================================================
try:
	my_dog = Dog('bodhi', 6)
	my_dog2 = Dog('nala', 10)
	my_dog3 = Dog()
	
	print(my_dog.name.title(), my_dog.age)
	my_dog.sit()
	my_dog.roll_over()
	
	print('\n' + my_dog2.name.title(), my_dog.age)
	my_dog2.sit()
	my_dog2.roll_over()
	
	# print(my_dog3.name.title(), my_dog3.age)
	# my_dog3.sit()
	# my_dog3.roll_over()
	
except TypeError:
	print("This is a TypeError...missing attributes from Dog Class")
	
except:
	print("This is an unknown error.")