user_value = input('\nEnter subject name: ')

def thisismyfunct(subject):
	"""this is my notes on how the user input for this module works when called by the <function>.__doc__ ."""
	print('mynotes on: ', subject)
	
thisismyfunct(user_value)
print(thisismyfunct.__doc__)
print('*' * 18)

def subtract(num1, num2):
	result =  num1 - num2
	return	result
	'''
A return statement is requried if the output of the function is to be used/displayed outside of the function.
NOTE: Run the above subtract function with and without the return statement.
With return = the output is printed IF the function is included in a print function (ie print(subtract())).  
If the function is just called:
	subtract()
	- then this only returns what actions are called in the function
Return is also used if the variable inside the function needs to referenced inside another function.
Without return = the output is None	
'''
	
r = subtract(10, 5)
print('Output from the RESULT being included or excluded from the function: ', r, ', ', type(r))
print('*' * 18)
guns = ['AK', 'STI', 'glock', 'cz', 'm4', 'remington 700', 'Tanfoglio', 'Nighthawk']


def guns_list(guns):
	length = len(guns)
	for i in range(0,length):
		return_guns = guns[i]
		print(i, return_guns)	
	return return_guns #return variable set to be called with either a print function or called inside another function (SEE: guns_list(guns)

print('*' * 18, '\n')


def gun_function():
	return_guns = guns_list(guns) #return_guns being called from another variable inside another function
	print('Return Guns: ', return_guns)
gun_function()


long_guns = ['M4']
def find_empty_lists(long_guns):
	if len(long_guns) == 0:
		print('empty list')
		return	None
	
	else:
		return_guns = len(long_guns)
		print(return_guns, long_guns[0])
	return return_guns
find_empty_lists(long_guns)	


print('*' * 18, '\n')

def print_function(*args):
#NOTE: the above *args variable allows the user to type in the passable argument VICE hard coding in the specific arguements that would e need to be passed to the function.
#NOTE: the variable can be named anything.  It does not have to be args.  The only requriement is that the variable argument starts w a *.
#NOTE: the return type for this *args is a tuple
	args_type = type(args)
	print(args_type)
	print(args)
	
print_function('\t', 'bob','chris','derek')
