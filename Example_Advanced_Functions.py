import math
import os
import random



country = 'USA' #Global
city = 'Sterling' #Global
#The above are global variables that are defined and placed outside a function


def some_func():
	country = 'Mexico'
#Country is now a local variable being that it is within the function.
#A fuction will always call the local variable (of the same name) before a global variable.
#Local variable cannot be REF'd outside of the function
	print('Country: ', country)
	print('City: ', city)
	
some_func()
print(country, city)
print('*' * 25, '\n')

def some_func1():
	global country
#	"""Using the keyword global, I'm able to call the above global variable and ref it directly in the function"""
	country = country + ' - North America'
	print('Global REF: ', country)
	print(city)

some_func1()
print('*' * 25, '\n')

def savings(name, salary, expense, ir):
	print('Name: ', name)
	savings = salary - expense
	print('Savings: ', savings)
	print('IR: ', ir)
	
savings('Jeff', 100000, 50000, 1.05)
print('*' * 25, '\n')

#help('modules') - will show all of the installed modules

print('Pi: ', math.pi)
c = math.ceil(10.1)
f = math.floor(10.1)
p = math.pow(2, 4)
s = math.sqrt(18)
print('\nCeiling: ',c,'\nFloor: ', f,'\nPower: ', p,'\nSquare Root: ', s)

u = os.environ['USER']
pwd = os.getcwd()
print('\nUser: ', u, '\nCurrent Working Dir: ',  pwd)
ld = os.listdir('/Users/user/Downloads')
print('List Dir: ', ld)

print('*' * 25, '\n')
print('Random module and function: ', random.random())
print('Random int between 0-1000: ', random.randint(0, 1000))
print('*' * 25, '\n')
#First Class: Fuctions can be assigned to variables.
#See the greet = hello line below

def hello(name):
	print('Name: ', name)

hello('derek First Class')
greet = hello
greet('derek also First Class')

print('*' * 25, '\n')
"""Lambdas are just functions with no names"""
#i.e. Lambda<input arguments>:<expression>
cube_of = lambda x:x * x * x
result = cube_of(5)
print('Lambda: ',result)

add = lambda x,y: x + y
sub = lambda x,y: x - y
mul = lambda x,y: x * y
div = lambda x,y: x / y

def calc(*args, operation=add):
	return operation(*args)
#	if operation == 'add':
#		return add(*args)
#	if operation == 'sub':
#		return sub(*args)
#	if operation == 'mul':
#		return mul(*args)
#	if operation == 'div':
#		return div(*args)
#*args = a variable length argument
			
print('Output of calc function using *args input: ', calc(5, 5, operation=add))
print('*' * 25, '\n')
print('Lambda Output: ',(lambda x:x*5)(10))
print('Lambda Output: ',(lambda x,y:x ** y)(2, 5))
print('*' * 25, '\n')
def check_if_even(x):
	assert x % 2 == 0
		
print('Check if even: ', check_if_even(4))
print('*' * 25, '\n')
num_list = [1,5,6,8,9]
output_list = list(filter(lambda x:x >= 5, num_list))
print(output_list)
output_list1 = list(filter(lambda x:x % 2 == 0, num_list))
print(output_list1)

