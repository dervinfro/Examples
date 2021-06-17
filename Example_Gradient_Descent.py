from tqdm import tqdm
from time import sleep

'''
NOTE: Graph shows that when y = 0 that x = -5.  The intent of this function will be to iterate through a loop and find the how many loops it takes to get to the local minimia
	https://towardsdatascience.com/implement-gradient-descent-in-python-9b93ed7108d1
Equation: y = (x+5)^2
Derivative of y to x: dy/dx = 2 * (x+5)
Initialize: x = 3
Loop:
	x - (learning_rate) * (dy/dx)

'''


def grad_descent(x_var):
	learning_rate = 0.003 #learning rate
	precision = 0.00001 #tells us when to stop the while loop
	max_iters = 40000 #maximum number of iterations
	previous_step_size = 1
	iters = 0 #iteration counter for the while loop
	deriv_func = lambda x: 2 * (x_var + 5)
	
	while precision < previous_step_size and iters < max_iters:
		sleep(0.002)
		prev_x_var = x_var
		x_var = x_var - learning_rate * deriv_func(x_var)
		previous_step_size = abs(x_var - prev_x_var) #abs(1-5) returns 4 NOT -4
#		print("previous step: {0:.7f}".format(previous_step_size))
		iters = iters+1
		print("Iteration: ", iters, "\nX value is: ", x_var)
		
		

		
	print("Local minima occurs at: ", x_var)
	
grad_descent(3)	
	