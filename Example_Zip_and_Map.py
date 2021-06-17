import numpy as np

x = np.random.randint(1,10,20)
xlist = list(x)
xlist3 = list(x * 3)
print('X List: ', xlist, sep='\n')
print('')
print('X List (Cubed): ', xlist3, sep='\n')
print('')

y = zip(xlist, xlist3)
print("Y: ", list(y), sep='\n') #xlist and xlist3 are put into paired tuples.  All of the entire pairs are put into list as per 'list(y)'

def my_func(n):
	return n ** 5 
	
a = map(my_func, (2,4,6,8)) # a tuple is passed in.
print('A: ', a, sep='\n') #result of print(a) returns the location of the object a
print('list(a): ', list(a), sep='\n') #returns: [32, 1024, 7776, 32768] - variables are passed to the my_func via the map method

z = map(my_func, xlist) # a list is passed in.
print('list(z): ', list(z), sep='\n')