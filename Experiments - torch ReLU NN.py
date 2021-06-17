import torch.nn.functional as F
from torch import nn
import torch

#help(F.relu)
#help(torch.nn.ReLU)

m = nn.ReLU()
input = torch.randn(2)
output = m(input)
print(output)
x = nn.Linear(12, 4)
print(x)

def relu(y):
	y = max(0, y)
	return y
'''
ReLU function above is an activation function that is almost exclusively used in hidden layers.
It is an economical choice for activation functions.
'''
	
	
z = relu(-8)
print(z)