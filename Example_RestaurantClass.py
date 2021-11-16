# =============================================================================
# Classes represent real-world things and situations
# The Class defines the general behavior of the whole category
# The Class is a set of instructions on how to make an instance.
# This Rest Class has two variables.
# =============================================================================

class Rest():
	
    # Special Method 
	def __init__(self, name, cuis_type):
		self.name = name
		self.cuis_type = cuis_type
		
    # Special Method
	def desc_rest(self):
		print(self.name.title() + " (<- variable) is the Restaurant name.")
		print(self.cuis_type.title() + " (<- variable) is the Cuisine type.")
		
    # Special Method
	def open_rest(self):
		print(self.name.title() + " (<- variable) is open.")
        
    # Special Method
	def close_rest(self):
		print(self.name.title() + ' (<- variable) is closed.')

# Rest() requires two positional arguements: 'Mic Ds', 'fast food'
# If args missing: __init__() missing 2 required positional arguments
restaurant = Rest('Mic Ds', 'fast food')
print("First Class Variable : {} \nSecond Class Variable: {}".format(restaurant.name, restaurant.cuis_type))
restaurant.desc_rest()
restaurant.open_rest()
restaurant.close_rest()
