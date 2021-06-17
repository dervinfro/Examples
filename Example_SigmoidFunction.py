import numpy as np
import matplotlib.pyplot as plt

from matplotlib import pyplot 


input = np.linspace(-10, 10, 100)

def sigmoid(X):
	val = 1/(1 + np.exp(-X))
	return val

output = sigmoid(input)

plt.plot(input,output)
plt.xlabel("x label")
plt.ylabel("y label")
plt.title("Sigmoid Function")
plt.show()

'''
NOTE: See the Sigmoid function example in the following link: https://medium.com/towards-artificial-intelligence/building-neural-networks-from-scratch-with-python-code-and-math-in-detail-i-536fae5d7bbf
'''