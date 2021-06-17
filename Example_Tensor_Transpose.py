import numpy as np
import torch

x = np.random.rand(2,4)
#y = torch.tensor(x)
z = np.transpose(x) 
print(x , '\n\n', z)
