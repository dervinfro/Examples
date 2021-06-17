import torch
import math
import matplotlib.pyplot as plt
import numpy as np
import sys
sys.path.insert(1, '/Users/user/Downloads/Python Airdroped 13MAY2020/')
import plot_graph_helper

epoch = 10
y_values = []
x_values = []
for x in range(epoch):
	x_values.append(x+1)
	math_log = math.log(x+1)
	y_values.append(math_log)
	
	
#below is my python file/function to import, and call, the capability to plot a graph.
#call the import -> call the function -> variable
print(x_values, type(x_values), '--', y_values, type(y_values))
plot_graph_helper.plot_helper(epoch, x_values, y_values)
