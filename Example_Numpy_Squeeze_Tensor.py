import numpy as np
import torch

############
## RANDOM ##
############
x_ran = np.random.rand(10,1) #establish a random numpy array
x_torch_ran = torch.rand(10,1)

print("NP Random: \n", x_ran, 
"\nNP Random Shape: ", x_ran.shape, 
"\nNP Random Type: ", type(x_ran)) #print x_ran, shape and type
print()
print("Torch Random: ", x_torch_ran)
print("Torch Random Shape: ", x_torch_ran.shape)
print("Torch Random Type: ", type(x_torch_ran))
print()

#############
## SQUEEZE ##
#############
x_sqz = np.squeeze(x_ran) #establish squeeze variable x_sqz

#Squeeze = removes the tensor dimensions or axes of one.  SEE Shape output for verification
print("SQUEEZE: \n", x_sqz, 
"\nSqueeze Shape: ", x_sqz.shape, 
"\nSqueeze Type: ", type(x_sqz)) #print x_sqz, shape and type
print("NP Squeeze of Torch: ", np.squeeze(x_torch_ran.numpy()))

print()

##################
## TORCH TENSOR ##
##################
x_torch = torch.tensor(x_sqz) #establish torch tensor of a squeeze variable

print('X torch.tensor of squeeze: \n', x_torch, 
'\nX Torch Type: ', type(x_torch)) #print tensor and type: <class 'torch.Tensor'>
print('torch.numpy: \n', x_torch.numpy())
print()

###############
## UNSQUEEZE ##
###############
x_unsqz = torch.tensor(x_sqz).unsqueeze(1) #establish unsqueeze object from squeeze object

print("Unsqueeze: \n", x_unsqz )
