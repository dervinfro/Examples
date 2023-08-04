#Recursion: invoke a function from within the function itself
import sys
import random
import math
from functools import cache


print("recursions limit: ", sys.getrecursionlimit())
#default limit set to 1000
#A limit on how many times a function can call upon itself

def hello(name):
	print('hello', name)
	hello(name)
	
def increment(num):
	print(num, end = ' ')
	increment(num + 1)
	
def decrement(num):
	if num == 0:
		print('decrement done.')
		return
		
	print(num)
	decrement(num -1)
	
decrement(10)

def recursive_sum(num):
	if num == 0:
		return 0
		
	result = num + recursive_sum(num - 1)
	return result
	
print('Recursive sum: ', recursive_sum(4))

def factorial(number):
	if number < 0:
		print('Factorial does not exist for negative number: ', number)
		return
		
	if number == 0:
		return 1
			
	return number * factorial(number - 1)
		
print('Factorial: ', factorial(2))
print('*' * 25)
@cache
def fibonacci(number, fib_series):
	if number < 2:
		print(number)
		return
		
	l = len(fib_series)
	
	new_number = fib_series[l - 1] + fib_series[l - 2]
	
	fib_series.append(new_number)
	
	print('Series so far', fib_series)
	
	fibonacci(number - 1,fib_series)
	
series = [0,1]
print('Fib series: ', fibonacci(10, series))
print('series: ', series)
print('*' * 25)

# %%
"""
A common use case for decorators is to implement caching, 
where the result of a function is stored after its first computation 
so that subsequent calls with the same arguments can be returned 
from the cache instead of recomputing the result.
"""
@cache
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

def main():
    for i in range(400):
        print(i, fib(i))

print('done')
 
if __name__ == '__main__':
    main()


#%%
#Generator: 
#	create a sequence that iterate over.
#	returns a generator object
#	has a yeild statement instead of a return statment

def generator():
	n = 1
	print('one')
	yield 1
	
	n += 1
	print('two')
	yield 2
	
	n += 1
	print('three')
	yield 3
	
	n += 1
	print('four')
	yield 4
	
g = generator()
print('generator: ', next(g))

print('*' * 25)
def gen_even():
	
	num = 0
	while True:
		num += 1
		yield 2 ** num
	
		
ge = gen_even()
print('Generator Even: ', next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))
print(next(ge))

print('*' * 25)
#Closures: nested function within a function that carry with them local state

#%%
def nested_helloFN():
	def hello():
		print('Hello Nested Fuction 1')
	hello()
	
nested_helloFN()

def get_hellofn():
	def hello():
		print('Hello Nested Function 2')
	return hello 
	
hellofn = get_hellofn()

print('Print Function: ', hellofn)
#<function get_hellofn.<locals>.hello at 0x103441e18> - the previous local statement indicates that this this is a closure
#The local state information associated with a closure remains even if the outer functions is no longer in Python memory
hellofn()


#%%
def greet(name, message):
	annotations = ('+','*','-','/')
	annotate = random.choice(annotations)
	
	def greeting():
		print(annotate * 25)
		print(message, name)
		print(annotate * 25)
		
	return greeting
print('\n')
greet_msg = greet('John', 'Function Example')
greet_msg()

print('\n')
#Decorators: Add functionality to existing code without having to have modify code
#Decorators cont: pass the message print fuction as the input argument
def print_msg():
	print('hello decorator - using @highlighted to print this function')

def highlighted(func):
	annotations = ('+','*','-','/')
	annotate = random.choice(annotations)
	
	def highlight():
		print(annotate * 25)
		func()
		print(annotate * 25)
		
	return highlight   
	
hm = highlighted(print_msg)
#When reffing the func of print_msg ensure that you are not using the double parans '()' in the highlighted function variable.
#Doing so will kick out an error code setting the variable of hm.
#Only use the double parans when envoking a function....ie hm()
hm()
@highlighted
def next_msg():
	print('@highlited message output - See the @ to envoke the decorator function')
next_msg()
print('\n')

def area_circle(radius):
	return math.pi * radius * radius
#	
#def perimeter_circle(radius):
#	return 2 * math.pi * radius
#	
#def diameter_circle(radius):
#	return 2 * radius
#	
print('Area: ', area_circle(-1))
#print('Perimeter: ', perimeter_circle(5))
#print('Diameter: ', diameter_circle(5))

def error_check(func):
	
	def calculate(r):
		if r <= 0:
			raise ValueError('Radius input cannot be neg value.  This a decorator for error checking.')
		return func(r)
	return calculate
	
area_circle_safe = error_check(area_circle)
#peri_circle_safe = error_check(perimeter_circle)
#dia_circle_safe = error_check(diameter_circle)
print('Long version of Area Circle: ', area_circle_safe(5))

#NOTE: The following four lines is code is the ideal method for calling a decorator.
#NOTE: The previous lines of code are the long, drawn out method for calling a decorator
@error_check
def area_circle(radius):
	return math.pi * radius * radius
print('Area Circle: ', area_circle(5))


	


	
